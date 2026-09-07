function tokenize(text){
  return (text || '').toLowerCase().split(/\s+/).filter(Boolean);
}

function similarity(a,b){
  const A=new Set(tokenize(a));
  const B=new Set(tokenize(b));
  const intersection=[...A].filter(x=>B.has(x)).length;
  return intersection / Math.max(A.size,B.size,1);
}

exports.handler=async function(event){
  const body=JSON.parse(event.body || '{}');
  const score=similarity(body.query || '', body.document || '');

  return {
    statusCode:200,
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify({
      similarity:score,
      engine:'semantic-vector-lite'
    })
  };
};
