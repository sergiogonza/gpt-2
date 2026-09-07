// Lightweight semantic vector engine for Netlify
// Uses local JSON vectors until FAISS backend is enabled.

function tokenize(text='') {
  return text.toLowerCase()
    .replace(/[^a-z0-9áéíóúñ ]/g,' ')
    .split(/\s+/)
    .filter(x=>x.length>2);
}

function vectorize(text='') {
  const tokens=[...new Set(tokenize(text))];
  const map={};
  tokens.forEach(t=>map[t]=1);
  return map;
}

function similarity(a,b){
  const va=vectorize(a);
  const vb=vectorize(b);
  const keys=new Set([...Object.keys(va),...Object.keys(vb)]);
  let dot=0,na=0,nb=0;
  keys.forEach(k=>{
    dot+=(va[k]||0)*(vb[k]||0);
    na+=(va[k]||0)**2;
    nb+=(vb[k]||0)**2;
  });
  return na&&nb ? dot/(Math.sqrt(na)*Math.sqrt(nb)) : 0;
}

module.exports={similarity,vectorize};
