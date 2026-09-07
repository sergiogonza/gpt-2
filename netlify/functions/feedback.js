exports.handler = async function(event) {
  if (event.httpMethod !== "POST") {
    return {statusCode:405, body:"Method not allowed"};
  }

  const data=JSON.parse(event.body || "{}");

  return {
    statusCode:200,
    headers:{"Content-Type":"application/json"},
    body:JSON.stringify({
      saved:true,
      memory_record:{
        query:data.query || "",
        response:data.response || "",
        rating:data.rating || null,
        timestamp:data.timestamp || new Date().toISOString()
      }
    })
  };
};
