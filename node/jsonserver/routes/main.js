const express = require('express');
const bodyParser = require('body-parser');
const XMLHttpRequest = require('xhr2');

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));


app.get('/Hello', (req, res) => {
    res.send('Hello World!!')
});

app.get('/getData', (req, res) => {
    const xhr = new XMLHttpRequest();
    xhr.open("GET", "https://localhost:5000/users", );
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send()

    xhr.onload = () => {
    if (xhr.status === 200) {
        const res = JSON.parse(xhr.response);
        console.log(res);
    } else {
        console.log(xhr.status, xhr.statusText);
    }
    res.send(xhr.response);
};
});

app.post("/postData", (req, res) => {
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "https://localhost:5000/users");
    if (xhr.readyState == 4 && xhr.status == 200) {
        try {
            xhr.open("POST", "https://localhost:5000/users",true);
            xhr.setRequestHeader("content-type", "application/json; charset=utf-8");

            xhr.onload = () => {
                if (xhr.status === 200) {
                    const rest = JSON.parse(xhr.response);
                    console.log(res);
                } else {
                    console.log(xhr.status, xhr.statusText);
                }
                res.send(xhr.response);
            };

            xhr.onerror = () => {
                console.log("Network Erorr");
                res.status(500).send("Network Error");
            };
        }

});

module.exports = app;