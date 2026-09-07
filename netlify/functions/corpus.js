const knowledge = require('../../corpus/knowledge.json');

function searchCorpus(query){
  const q=(query || '').toLowerCase();

  return knowledge.filter(item =>
    item.title.toLowerCase().includes(q) ||
    item.text.toLowerCase().includes(q) ||
    q.split(' ').some(word => word.length > 3 && item.text.toLowerCase().includes(word))
  ).slice(0,3);
}

module.exports={searchCorpus, corpus:knowledge};
