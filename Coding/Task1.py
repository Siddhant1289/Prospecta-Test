'''To create an API that lists the title and description based on the category passed as an input parameter, you could make a GET request to the endpoint https://api.publicapis.org/entries and include a query parameter for the category. The query parameter would be passed in the URL itself, and the server would then filter the entries based on that category and return the appropriate entries.'''

const express = require('express');
const app = express();
const fetch = require('node-fetch');

app.get('/entries', (req, res) => {
    const category = req.query.category;
    fetch(`https://api.publicapis.org/entries?category=${category}`)
        .then(response => response.json())
        .then(data => {
            const entries = data.entries.map(entry => {
                return {
                    API: entry.API,
                    Description: entry.Description
                }
            });
            res.status(200).json({ entries });
        })
        .catch(error => {
            console.log(error);
            res.status(500).json({ error });
        });
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});

'''This code uses the Express.js framework to create a server, and the fetch package to make the GET request to the https://api.publicapis.org/entries endpoint. The server listens for GET requests to the /entries endpoint, and when a request is received, it extracts the category query parameter from the request's query string. It then uses this parameter to construct the URL for the GET request to the https://api.publicapis.org/entries endpoint, which is made using the fetch function. The server then awaits the response from the API, which it converts to JSON, and then uses the json data to create a new array with the entries containing only the API and description. The server then sends this new array as a JSON response to the client.'''