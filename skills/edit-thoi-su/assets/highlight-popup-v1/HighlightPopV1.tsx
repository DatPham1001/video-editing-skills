import React from 'react';
import {AbsoluteFill,Easing,interpolate,spring,staticFile,useCurrentFrame,useVideoConfig} from 'remotion';

export type HighlightProps={lines:string[];fontSize:number;accent:string;accentAt:number;tag:string};
const ease={extrapolateLeft:'clamp' as const,extrapolateRight:'clamp' as const,easing:Easing.bezier(.16,1,.3,1)};
export const HighlightPopV1:React.FC<HighlightProps>=({lines,fontSize,accent,accentAt,tag})=>{
  const f=useCurrentFrame(),{fps,durationInFrames:d}=useVideoConfig();
  const p=spring({frame:f,fps,config:{damping:19,stiffness:210,mass:.65}});
  const exit=interpolate(f,[d-6,d-1],[1,0],ease);
  const enter=interpolate(f,[0,5],[0,1],ease);
  const pulse=interpolate(f,[accentAt,accentAt+3,accentAt+10],[0,1,0],{extrapolateLeft:'clamp',extrapolateRight:'clamp'});
  return <AbsoluteFill style={{fontFamily:'ReferenceSans',opacity:exit}}>
    <style>{`@font-face{font-family:ReferenceSans;src:url('${staticFile('fonts/reference-bold.ttf')}');font-weight:700 900;}`}</style>
    <AbsoluteFill style={{background:'rgba(5,12,22,.36)',opacity:enter}}/>
    <div style={{position:'absolute',left:70,top:730,width:940,height:460,boxSizing:'border-box',borderRadius:28,border:'2px solid #2F6E70',background:'linear-gradient(145deg,rgba(17,39,61,.95),rgba(7,19,33,.95))',boxShadow:'0 24px 65px #0008',padding:42,opacity:enter,translate:`0 ${interpolate(p,[0,1],[64,0])}px`,scale:interpolate(p,[0,1],[.74,1]),display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'center'}}>
      {tag&&<div style={{position:'absolute',top:30,left:24,right:24,textAlign:'center',color:'#54E0C6',fontSize:30,fontWeight:700,letterSpacing:1}}>{tag}</div>}
      <div style={{width:'100%',textAlign:'center',paddingTop:tag?20:0}}>
        {lines.map((line,i)=><div key={i} style={{color:i===lines.length-1?accent:'#F7FAFC',fontSize,fontWeight:800,lineHeight:1.12,letterSpacing:-1,whiteSpace:'nowrap',opacity:interpolate(f,[i*4,i*4+5],[0,1],ease),translate:`0 ${interpolate(f,[i*4,i*4+7],[24,0],ease)}px`,scale:i===lines.length-1?1+pulse*.025:1,textShadow:i===lines.length-1?`0 0 ${12+pulse*20}px ${accent}55`:'0 4px 18px #0009'}}>{line}</div>)}
      </div>
      <div style={{position:'absolute',height:8,left:100,bottom:36,width:interpolate(f,[Math.max(4,accentAt-3),Math.max(4,accentAt-3)+8],[0,736],ease),background:accent,borderRadius:4}}/>
    </div>
  </AbsoluteFill>;
};

