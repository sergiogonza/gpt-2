const cosine = (a,b)=>{
 const dot=a.reduce((s,x,i)=>s+x*b[i],0);
 const na=Math.sqrt(a.reduce((s,x)=>s+x*x,0));
 const nb=Math.sqrt(b.reduce((s,x)=>s+x*x,0));
 return dot/(na*nb);
};

exports.handler = async(event)=>{
 const query=JSON.parse(event.body || '{}');
 const vector=query.embedding || [];
 const db=require('../../data/vector-db.json');

 const results=db.map(item=>({
  id:item.id,
  text:item.text,
  score:cosine(vector,item.embedding)
 })).sort((a,b)=>b.score-a.score);

 return {
  statusCode:200,
  body:JSON.stringify({results:results.slice(0,5)})
 };
};
