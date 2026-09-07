// FAISS compatible lightweight index for Netlify
// Keeps the same interface used by FAISS: add vectors and search nearest neighbors

const store = require('../../data/vector-index.json');

function cosine(a,b){
 const dot=a.reduce((s,x,i)=>s+x*b[i],0);
 const na=Math.sqrt(a.reduce((s,x)=>s+x*x,0));
 const nb=Math.sqrt(b.reduce((s,x)=>s+x*x,0));
 return na && nb ? dot/(na*nb) : 0;
}

function search(queryVector, k=5){
 return store
  .map(item=>({
    ...item,
    similarity: cosine(queryVector,item.embedding || [])
  }))
  .sort((a,b)=>b.similarity-a.similarity)
  .slice(0,k);
}

exports.handler=async(event)=>{
 const body=JSON.parse(event.body||'{}');
 return {
  statusCode:200,
  body:JSON.stringify({
    engine:'faiss-compatible-index',
    dimension:body.vector?.length || 0,
    results:search(body.vector||[])
  })
 };
};
