const {retrieve}=require('./retriever');

exports.handler = async function(event) {
  if(event.httpMethod!=="POST"){
    return {statusCode:405,body:JSON.stringify({error:"Method not allowed"})};
  }

  const data=JSON.parse(event.body||"{}");
  const question=data.query || data.prompt || "";

  const sources=retrieve(question);

  let answer;

  if(question.toLowerCase().includes('hola')){
    answer='Hola, soy tu asistente GPT-2 RAG funcionando con Netlify.';
  } else if(sources.length){
    answer='Encontré contexto relevante:\n\n'+sources.map(s=>s.text).join('\n\n');
  } else {
    answer='No encontré suficiente contexto todavía. Puedes ampliar el corpus.';
  }

  return {
    statusCode:200,
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify({
      answer,
      sources,
      rag:true,
      retriever:'semantic-lite-v2',
      model:'gpt2-rag-netlify'
    })
  };
};
