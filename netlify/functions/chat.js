const {searchCorpus}=require('./corpus');

exports.handler = async function(event) {
  if (event.httpMethod !== "POST") {
    return {
      statusCode:405,
      body:JSON.stringify({error:"Method not allowed"})
    };
  }

  const data=JSON.parse(event.body || "{}");
  const question=data.query || data.prompt || "";

  const sources=searchCorpus(question);

  let answer;

  if(question.toLowerCase().includes("hola")){
    answer="Hola, soy tu asistente GPT-2 RAG funcionando con Netlify.";
  } else if(sources.length){
    answer="Encontré información relacionada:\n\n" + sources.map(s=>s.text).join("\n\n");
  } else {
    answer="Recibí tu consulta: " + question + ". Todavía necesito ampliar mi corpus.";
  }

  return {
    statusCode:200,
    headers:{"Content-Type":"application/json"},
    body:JSON.stringify({
      answer,
      sources,
      rag:true,
      model:"gpt2-rag-netlify"
    })
  };
};
