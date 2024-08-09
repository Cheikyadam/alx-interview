#!/usr/bin/node
const util = require('util');
const request = require('request');

const requestPromise = util.promisify(request);
async function fetchData (url) {
  try {
    const response = await requestPromise(url);
    const data = JSON.parse(response.body);
    console.log(data.name);
  } catch (error) {
    console.error('An error occurs', error);
  }
}

async function fetchCharacters (urls) {
  for (const url of urls) {
    await fetchData(url);
  }
}

if (process.argv.length === 3) {
  const movieId = process.argv[2];
  request('https://swapi-api.alx-tools.com/api/films/' + movieId, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const jsonResp = JSON.parse(body);
      fetchCharacters(jsonResp.characters);
    }
  });
}
