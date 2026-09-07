exports.handler = async function(event) {
  if (event.httpMethod !== "POST") {
    return {
      statusCode: 405,
      body: JSON.stringify({error: "Method not allowed"})
    };
  }

  const api = process.env.GPT2_API_URL;

  if (!api) {
    return {
      statusCode: 500,
      body: JSON.stringify({error: "GPT2_API_URL missing"})
    };
  }

  const response = await fetch(`${api}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: event.body
  });

  const data = await response.text();

  return {
    statusCode: response.status,
    headers: {
      "Content-Type": "application/json"
    },
    body: data
  };
};
