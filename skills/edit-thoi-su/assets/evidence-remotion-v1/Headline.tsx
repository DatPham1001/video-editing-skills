import React from 'react';
import {AbsoluteFill,Easing,interpolate,staticFile,useCurrentFrame,useVideoConfig} from 'remotion';
export const Headline:React.FC<{title:string;accent:string}>=({title,accent})=>{
 const frame=useCurrentFrame(),{durationInFrames}=useVideoConfig();
 const opt={extrapolateLeft:'clamp' as const,extrapolateRight:'clamp' as const,easing:Easing.bezier(.16,1,.3,1)};
 return <AbsoluteFill style={{opacity:interpolate(frame,[durationInFrames-5,durationInFrames-1],[1,0],opt),fontFamily:'HeadlineSans'}}>
  <style>{`@font-face{font-family:HeadlineSans;src:url('${staticFile('fonts/reference-bold.ttf')}');font-weight:700;}`}</style>
  <div style={{position:'absolute',left:90,top:25,width:900,fontSize:86,fontWeight:700,lineHeight:1.08,letterSpacing:-2,color:'#FFFFFF',textShadow:'0 5px 22px #000C',whiteSpace:'pre-line',opacity:interpolate(frame,[0,5],[0,1],opt),translate:`0 ${interpolate(frame,[0,7],[24,0],opt)}px`}}>{title}</div>
  <div style={{position:'absolute',left:90,top:title.indexOf('\n')>=0?225:135,height:8,width:interpolate(frame,[4,12],[0,240],opt),backgroundColor:accent,boxShadow:'0 0 20px #54E0C655'}}/>
 </AbsoluteFill>;
};
