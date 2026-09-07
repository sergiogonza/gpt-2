const {corpus}=require('./corpus');

function tokenize(text){
 return (text||'').toLowerCase().split(/\s+/).filter(x=>x.length>2);
}

function score(query,text){
 const q=tokenize(query);
 const t=tokenize(text);
 const common=q.filter(x=>t.includes(x)).length;
 return common/(q.length||1);
}

function retrieve(query){
 return corpus
  .map(doc=>({...doc,score:score(query,doc.title+' '+doc.text)}))
  .filter(doc=>doc.score>0)
  .sort((a,b)=>b.score-a.score)
  .slice(0,5);
}

module.exports={retrieve};
