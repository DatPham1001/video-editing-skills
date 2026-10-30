"""Produce ChatCut adds for one evidence overlay and blur on every intersecting clip.

Input clips: [{"id": "current native item id", "fromFrame": 100,
               "durationInFrames": 60}] (endFrame can replace durationInFrames).
No network calls or project mutations. Re-read native clips before using output.
"""
import argparse
import json
from pathlib import Path

def integer(value, label):
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(label + ' must be an integer')
    return value

def plan(clips, asset_id, start, duration, track):
    integer(start, 'fromFrame'); integer(duration, 'durationInFrames')
    if start < 0 or duration < 18 or not asset_id or not track:
        raise ValueError('Require nonnegative start, duration >=18f, asset id and overlay track')
    end = start + duration
    spans, ids = [], set()
    for clip in clips:
        ident = clip['id']
        if not ident or ident in ids:
            raise ValueError('Empty or duplicate original clip id')
        ids.add(ident)
        a = integer(clip['fromFrame'], 'clip.fromFrame')
        b = integer(clip['endFrame'], 'clip.endFrame') if 'endFrame' in clip else a + integer(clip['durationInFrames'], 'clip.durationInFrames')
        if a < 0 or b <= a:
            raise ValueError('Invalid original clip range')
        lo, hi = max(start, a), min(end, b)
        if lo < hi:
            spans.append((lo, hi, ident))
    spans.sort()
    cursor = start
    for lo, hi, _ in spans:
        if lo != cursor:
            raise ValueError('Background clips have a gap or overlap; re-read the target range')
        cursor = hi
    if cursor != end:
        raise ValueError('Background clips do not cover the whole overlay')
    adds = [{'type':'video','assetId':asset_id,'trackId':track,'fromFrame':start,
             'durationInFrames':duration,'sourceStartFromInSeconds':0,
             'left':0,'top':0,'width':1080,'height':1920,'fit':'contain'}]
    adds += [{'type':'effect','assetId':'builtin:fx-gaussian-blur',
              'targetItemId':ident,'fromFrame':lo,'durationInFrames':hi-lo,
              'propertyOverrides':{'radius':180}} for lo, hi, ident in spans]
    return {'adds':adds}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--clips',required=True,type=Path)
    parser.add_argument('--asset-id',required=True)
    parser.add_argument('--from-frame',required=True,type=int)
    parser.add_argument('--duration',required=True,type=int)
    parser.add_argument('--overlay-track',required=True)
    parser.add_argument('--output',required=True,type=Path)
    args=parser.parse_args()
    try:
        result=plan(json.loads(args.clips.read_text(encoding='utf-8-sig')),args.asset_id,args.from_frame,args.duration,args.overlay_track)
    except (ValueError,KeyError,TypeError) as exc:
        parser.error(str(exc))
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f"Planned 1 overlay and {len(result['adds'])-1} per-clip blur effects; no edits committed.")

if __name__=='__main__':
    main()
