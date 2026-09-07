const corpus = [
  {
    id: "ai-basics",
    title: "Inteligencia artificial",
    text: "La inteligencia artificial es un campo de la computacion que permite crear sistemas capaces de analizar datos, reconocer patrones y generar respuestas."
  },
  {
    id: "rag-basics",
    title: "Retrieval Augmented Generation",
    text: "RAG combina un modelo generativo con una base de conocimiento externa para recuperar informacion relevante antes de responder."
  },
  {
    id: "gpt2",
    title: "GPT-2",
    text: "GPT-2 es un modelo de lenguaje basado en Transformers entrenado para predecir texto y generar respuestas.">
  }
];

function searchCorpus(query){
  const q=query.toLowerCase();
  return corpus.filter(item=>
    item.text.toLowerCase().includes(q) ||
    item.title.toLowerCase().includes(q)
  ).slice(0,3);
}

module.exports={searchCorpus, corpus};
