const API = "/api/chat";
let lastResponse = "";

async function sendMessage(){
  const input=document.getElementById("input");
  const chat=document.getElementById("chat");
  const text=input.value;
  if(!text) return;

  chat.innerHTML += `<div class="message user">${text}</div>`;
  input.value="";

  try{
    const response=await fetch(API,{
      method:"POST",
      headers:{"Content-Type":"application/json"},
      body:JSON.stringify({query:text})
    });
    const data=await response.json();
    lastResponse=data.answer || data.response || "Respuesta recibida";
    chat.innerHTML += `<div class="message assistant">${lastResponse}</div>`;
  }catch(e){
    chat.innerHTML += `<div class="message assistant">API no configurada todavía.</div>`;
  }
}

async function feedback(value){
 await fetch("/api/feedback",{
  method:"POST",
  headers:{"Content-Type":"application/json"},
  body:JSON.stringify({rating:value,response:lastResponse})
 });
}
