import React from 'react';
import {AbsoluteFill, CanvasImage, Easing, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';

export type EvidenceRegion = {
  image: string; imageWidth: number; imageHeight: number;
  crop: {x:number; y:number; width:number; height:number};
  left:number; top:number; width:number;
};
export type EvidenceProps = {
  kicker:string; publisher:string; source:string;
  regions:EvidenceRegion[]; summary:string; note:string; summaryTop:number;
};
const ease={extrapolateLeft:'clamp' as const,extrapolateRight:'clamp' as const,easing:Easing.bezier(.16,1,.3,1)};

// Frozen evidence-remotion-v1 timing and geometry. Only article content/crops vary.
export const EvidenceCardV1:React.FC<EvidenceProps>=({kicker,publisher,source,regions,summary,note,summaryTop})=>{
  const f=useCurrentFrame(),{fps,durationInFrames:d}=useVideoConfig();
  const r=spring({frame:f,fps,config:{damping:19,stiffness:210,mass:.65}});
  const enter=interpolate(f,[0,5],[.15,1],ease);
  const exit=interpolate(f,[d-6,d-1],[1,0],ease);
  return <AbsoluteFill style={{fontFamily:'ReferenceSans',color:'#F7FAFC',opacity:exit}}>
    <style>{`@font-face{font-family:ReferenceSans;src:url('${staticFile('fonts/reference-bold.ttf')}');font-weight:700 900;}@font-face{font-family:ReferenceSans;src:url('${staticFile('fonts/reference-regular.ttf')}');font-weight:400 600;}`}</style>
    <AbsoluteFill style={{backgroundColor:'rgba(5,12,22,.46)',opacity:enter}}/>
    <div style={{position:'absolute',inset:0,opacity:enter,translate:`0 ${interpolate(r,[0,1],[64,0])}px`,scale:interpolate(r,[0,1],[.94,1])}}>
      <div style={{position:'absolute',left:110,top:100,fontSize:44,fontWeight:700,letterSpacing:1,color:'#54E0C6'}}>{kicker}</div>
      <div style={{position:'absolute',left:120,top:190,width:840,height:960,backgroundColor:'white',borderRadius:22,overflow:'hidden',boxShadow:'0 24px 65px #0008',rotate:`${interpolate(f,[0,12],[-2,0],ease)}deg`}}>
        <div style={{position:'absolute',left:32,top:28,fontSize:30,fontWeight:700,color:'#34616A'}}>{publisher}</div>
        {regions.map((region,i)=>{
          const s=region.width/region.crop.width;
          return <div key={i} style={{position:'absolute',left:region.left,top:region.top,width:region.width,height:region.crop.height*s,overflow:'hidden'}}>
            <CanvasImage src={staticFile(region.image)} style={{position:'absolute',left:-region.crop.x*s,top:-region.crop.y*s,width:region.imageWidth*s,height:region.imageHeight*s}}/>
          </div>;
        })}
        <div style={{position:'absolute',left:32,top:summaryTop-42,fontSize:27,fontWeight:700,color:'#34616A',letterSpacing:1}}>TÓM TẮT BIÊN TẬP</div>
        <div style={{position:'absolute',left:32,top:summaryTop,right:32,fontSize:54,fontWeight:800,lineHeight:1.13,whiteSpace:'pre-line',color:'#0B1627'}}>{summary}</div>
        <div style={{position:'absolute',left:32,top:summaryTop+142,height:8,width:interpolate(f,[7,17],[0,700],ease),backgroundColor:'#FFDD70'}}/>
        <div style={{position:'absolute',left:32,top:summaryTop+182,right:32,fontSize:34,fontWeight:400,lineHeight:1.25,whiteSpace:'pre-line',color:'#34616A'}}>{note}</div>
      </div>
      <div style={{position:'absolute',left:120,top:1162,fontSize:32,fontWeight:700}}>{source}</div>
    </div>
  </AbsoluteFill>;
};
