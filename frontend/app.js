const API = window.ENV_API_URL || "/api/chat";
const FEEDBACK_API = window.ENV_FEEDBACK_URL || "/api/feedback";
let lastResponse = "";
let lastQuestion = "";

async function sendMessage(){
  const input=document.getElementById("input");
  const chat=document.getElementById("chat");
  const text=input.value.trim();
  if(!text) return;

  lastQuestion=text;
  chat.innerHTML += `<div class="message user">${text}</div>`;
  input.value="";

  try{
    const response=await fetch(API,{
      method:"POST",
      headers:{"Content-Type":"application/json"},
      body:JSON.stringify({query:text, prompt:text, rag:true, memory:true})
    });

    if(!response.ok) throw new Error("API error");

    const data=await response.json();
    lastResponse=data.answer || data.response || "Respuesta recibida";

    chat.innerHTML += `<div class="message assistant">${lastResponse}</div>`;
  }catch(e){
    chat.innerHTML += `<div class="message assistant">Backend no conectado. Configura API_URL en Netlify.</div>`;
  }
}

async function feedback(value){
 try{
  await fetch(FEEDBACK_API,{
   method:"POST",
   headers:{"Content-Type":"application/json"},
   body:JSON.stringify({
     query:lastQuestion,
     response:lastResponse,
     rating:value,
     timestamp:new Date().toISOString()
   })
  });
 }catch(e){
  console.log("Feedback pendiente");
 }
}
