import React from 'react';
import {AbsoluteFill,CanvasImage,Easing,interpolate,spring,staticFile,useCurrentFrame,useVideoConfig} from 'remotion';
export type Props={kind:string;kicker:string;title:string;choices:string[];image:string;source:string};
const teal='#54E0C6',white='#F7FAFC',ease={extrapolateLeft:'clamp' as const,extrapolateRight:'clamp' as const,easing:Easing.bezier(.16,1,.3,1)};
const Cup=()=> <svg width="90" height="80" viewBox="0 0 90 80"><path d="M15 24h48v27c0 25-48 25-48 0zM65 29h9c19 0 17 27-10 24M10 74h61M29 5v10M48 5v10" fill="none" stroke={teal} strokeWidth="4" strokeLinecap="round"/></svg>;
const Shop=()=> <svg width="120" height="100" viewBox="0 0 132 112"><path d="M12 42 27 12h78l15 30v19H12zM22 62v41h88V62M42 103V74h24v29M81 76h15v15H81" fill="none" stroke={teal} strokeWidth="5" strokeLinejoin="round"/></svg>;
export const StoryCard:React.FC<Props>=({kind,kicker,title,choices,image,source})=>{
const f=useCurrentFrame(),{fps,durationInFrames:d}=useVideoConfig();
const r=spring({frame:f,fps,config:{damping:19,stiffness:210,mass:.65}});
const enter=interpolate(f,[0,5],[.15,1],ease),exit=interpolate(f,[d-6,d-1],[1,0],ease);
const panel:React.CSSProperties={position:'absolute',left:90,top:210,width:900,height:910,boxSizing:'border-box',background:'linear-gradient(150deg,#11273D,#071321)',border:'2px solid #2F6E70',borderRadius:32,boxShadow:'0 26px 75px #0006',padding:52,color:white};
const titleStyle:React.CSSProperties={fontSize:84,fontWeight:800,lineHeight:1.07,letterSpacing:-2,whiteSpace:'pre-line',marginTop:32};
return <AbsoluteFill style={{fontFamily:'ReferenceSans',color:white,opacity:exit}}>
<style>{`@font-face{font-family:ReferenceSans;src:url('${staticFile('fonts/reference-bold.ttf')}');font-weight:700 900;}@font-face{font-family:ReferenceSans;src:url('${staticFile('fonts/reference-regular.ttf')}');font-weight:400 600;}`}</style>
<AbsoluteFill style={{backgroundColor:'rgba(5,12,22,.46)',opacity:enter}}/>
<div style={{position:'absolute',inset:0,opacity:enter,translate:`0 ${interpolate(r,[0,1],[64,0])}px`,scale:interpolate(r,[0,1],[.94,1])}}>
{(kind==='ap'||kind==='reuters')&&<>
<div style={{position:'absolute',left:110,top:100,fontSize:44,fontWeight:700,letterSpacing:1,color:teal}}>{kicker}</div>
<div style={{position:'absolute',left:120,top:190,width:840,height:960,backgroundColor:'white',borderRadius:22,overflow:'hidden',boxShadow:'0 24px 65px #0008',rotate:`${interpolate(f,[0,12],[-2,0],ease)}deg`}}>
<CanvasImage src={staticFile(image)} style={kind==='ap'?{position:'absolute',width:1988,height:1118,left:-272,top:-116}:{position:'absolute',width:2254,height:1268,left:-301,top:-158}}/>
<div style={{position:'absolute',left:16,top:kind==='ap'?68:139,height:8,width:interpolate(f,[7,17],[0,kind==='ap'?590:790],ease),backgroundColor:'#FFDD70'}}/>
</div><div style={{position:'absolute',left:120,top:1162,fontSize:32,fontWeight:700}}>{source}</div></>}
{kind==='hanoi'&&<>
<div style={{position:'absolute',left:100,top:170,fontSize:44,color:teal,fontWeight:700}}>{kicker}</div>
<div style={{position:'absolute',left:100,top:260,fontSize:84,fontWeight:800,letterSpacing:-2}}>{title}</div>
<div style={{position:'absolute',left:75,top:410,width:930,height:620,overflow:'hidden',borderRadius:24,boxShadow:'0 24px 65px #0008',rotate:`${interpolate(f,[0,15],[-2,0],ease)}deg`}}><CanvasImage src={staticFile(image)} style={{width:930,height:620,objectFit:'contain',scale:interpolate(f,[0,d],[1,1.035],ease)}}/></div>
<div style={{position:'absolute',left:100,top:1080,fontSize:34}}>{source}</div></>}
{['ap','reuters','hanoi'].indexOf(kind)===-1&&<div style={{...panel,...(kind==='question'?{top:270,height:770}:{})}}>
<div style={{fontSize:kind==='meals'?36:40,color:teal,fontWeight:700}}>{kicker}</div><div style={titleStyle}>{title}</div>
{kind==='store'&&<div style={{marginTop:36}}>{choices.map((s,i)=><div key={s} style={{display:'flex',gap:32,alignItems:'center',height:148,opacity:interpolate(f,[i*23,i*23+8],[0,1],ease),translate:`${interpolate(f,[i*23,i*23+8],[26,0],ease)}px 0`}}><Shop/><div style={{fontSize:56,fontWeight:700}}>{s}</div></div>)}</div>}
{kind==='question'&&<><div style={{position:'absolute',left:52,bottom:90,height:10,width:interpolate(f,[8,17],[0,690],ease),backgroundColor:'#FFDD70'}}/><div style={{position:'absolute',left:52,bottom:32,fontSize:30,color:'#AFC8D5'}}>{source}</div></>}
{kind==='food'&&<div style={{marginTop:38}}>{choices.slice(f<54?0:3,f<54?3:6).map((s,i)=><div key={s} style={{height:148,display:'flex',alignItems:'center',gap:30,borderTop:'1px solid #34616A',opacity:interpolate(f%54,[i*3,i*3+7],[0,1],ease),translate:`${interpolate(f%54,[i*3,i*3+7],[26,0],ease)}px 0`}}><div style={{width:64,height:64,borderRadius:32,border:'2px solid '+teal,display:'flex',alignItems:'center',justifyContent:'center',fontSize:32,color:teal}}>{i+(f<54?1:4)}</div><div style={{fontSize:60,fontWeight:700}}>{s}</div></div>)}</div>}
{kind==='coffee'&&<div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:28,marginTop:62}}>{choices.map((s,i)=><div key={s} style={{height:240,border:'1px solid #2F6E70',borderRadius:20,display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'center',gap:28,opacity:interpolate(f,[i*5,i*5+8],[0,1],ease),scale:interpolate(f,[i*5,i*5+8],[.9,1],ease)}}><Cup/><div style={{fontSize:48,fontWeight:700}}>{s}</div></div>)}</div>}
{kind==='meals'&&<div style={{display:'flex',justifyContent:'space-between',gap:40,marginTop:92}}>{choices.map((s,i)=><div key={s} style={{display:'flex',alignItems:'center',flexDirection:'column',gap:40,opacity:interpolate(f,[i*9,i*9+8],[0,1],ease)}}><div style={{width:290,height:290,border:'5px solid '+teal,borderRadius:145,display:'flex',alignItems:'center',justifyContent:'center',boxShadow:'0 0 45px #54E0C622'}}><div style={{width:220,height:220,borderRadius:110,border:'1px solid #54E0C699'}}/></div><div style={{fontSize:58,fontWeight:700}}>{s}</div></div>)}</div>}
</div>}
</div></AbsoluteFill>;};
