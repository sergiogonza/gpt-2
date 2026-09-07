const vectors = require('../../data/vector-index.json');

function score(a,b){
 const aa=a.toLowerCase();
 const bb=b.toLowerCase();
 return aa.split(' ').filter(x=>bb.includes(x)).length;
}

exports.handler = async(event)=>{
 const q=JSON.parse(event.body||'{}').query||'';
 const results=vectors.map(v=>({
  ...v,
  score:score(q,v.text)
 })).sort((a,b)=>b.score-a.score);

 return {
  statusCode:200,
  body:JSON.stringify({results})
 };
};
