const fs = require('fs');
const path = require('path');

function tokenize(text=''){
  return text.toLowerCase().match(/[a-záéíóúñ0-9]+/g) || [];
}

function similarity(a,b){
  const A=new Set(tokenize(a));
  const B=new Set(tokenize(b));
  if(!A.size || !B.size) return 0;
  let common=0;
  A.forEach(x=>{if(B.has(x)) common++});
  return common / new Set([...A,...B]).size;
}

function rankDocuments(query,docs){
  return docs.map(d=>({...d,score:similarity(query,d.text)}))
    .sort((a,b)=>b.score-a.score);
}

module.exports={rankDocuments};
