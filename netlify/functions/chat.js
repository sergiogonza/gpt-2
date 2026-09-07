const {searchCorpus}=require('./corpus');
const {similarity}=require('./vector');

exports.handler = async function(event) {
  if (event.httpMethod !== "POST") {
    return {statusCode:405,body:JSON.stringify({error:"Method not allowed"})};
  }

  const data=JSON.parse(event.body || "{}");
  const question=data.query || data.prompt || "";

  let sources=searchCorpus(question)
    .map(item=>({...item,score:similarity(question,item.text+' '+item.title)}))
    .sort((a,b)=>b.score-a.score)
    .slice(0,3);

  let answer;

  if(question.toLowerCase().includes("hola")){
    answer="Hola, soy tu asistente GPT-2 RAG funcionando con Netlify.";
  } else if(sources.length && sources[0].score>0){
    answer="Contexto recuperado por RAG:\n\n" + sources.map(s=>s.text).join("\n\n");
  } else {
    answer="Recibí tu consulta: " + question + ". El sistema RAG necesita más conocimiento para responder.";
  }

  return {
    statusCode:200,
    headers:{"Content-Type":"application/json"},
    body:JSON.stringify({
      answer,
      sources,
      rag:true,
      embeddings:"local-semantic-v1",
      model:"gpt2-rag-netlify"
    })
  };
};
