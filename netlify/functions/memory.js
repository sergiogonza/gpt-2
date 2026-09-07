exports.handler = async (event) => {
  const body = JSON.parse(event.body || '{}');

  const memory = {
    timestamp: new Date().toISOString(),
    input: body.input || '',
    feedback: body.feedback || null
  };

  return {
    statusCode: 200,
    body: JSON.stringify({
      stored: true,
      memory
    })
  };
};
