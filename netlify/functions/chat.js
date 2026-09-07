exports.handler = async function(event) {
  if (event.httpMethod !== "POST") {
    return {
      statusCode: 405,
      body: JSON.stringify({error:"Method not allowed"})
    };
  }

  const data = JSON.parse(event.body || "{}");
  const question = data.query || data.prompt || "";

  let answer;

  if (question.toLowerCase().includes("hola")) {
    answer = "Hola, soy tu asistente GPT-2 RAG funcionando con Netlify Functions.";
  } else {
    answer = "Recibí tu consulta: " + question + ". El motor GPT-2 y RAG serán conectados en la siguiente fase.";
  }

  return {
    statusCode: 200,
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      answer,
      sources: [],
      rag: false,
      model: "netlify-function-placeholder"
    })
  };
};
