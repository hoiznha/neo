const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const users = [
    {id : 1, name : 'User1'},
    {id : 2, name : 'User2'},
    {id : 3, name : 'User3'},
]

app.get('/Hello', (req, res) => {
    res.send('Hello World!!')
})

//request x , response o
app.get('/api/users',(req,res) => {
    res.json({ok: true,users:users})
})

//query string, request o , response o
app.get('/api/users/user',(req,res) => {
    let user = "";
    const { user_id,name } = req.query;

    if (req.query.name == null) {
        user = users.filter(data => data.id == user_id);
    } else {
        user = users.filter(data => data.id == user_id && data.name == name);
    }
    res.json({ok: false, users:user})
})

//query params(path params), request o , response o
app.get('/api/users/:user_id',(req,res) => {
    let user_id = req.params.user_id

    const user = users.filter(data => data.id == user_id);
    res.json({ok: false, users:user})
})

//post, request o , response o -> 다시해보기
app.post('/api/users/userBody', (req, res) => {
    const id = req.body.id;
    const user = users.filter(data => data.id == id);
    res.json({ok: false, users:user})
})

//post, request o, response o
app.post('/api/users/add', (req, res) => {
    const { id, name }= req.body;
    const user = users.concat({id, name});
    res.json({ok: true, users:user})    
})

// put request o, response o
app.put('/api/users/update', (req, res) => {
    const { id, name }= req.body;
    const user = users.map(data => {
        if (data.id == id) data.name = name
        return {
            id: data.id,
            name: data.name 
        }
    })
    res.json({ok: true, users:user})    
})

// patch, request params & body o, response o
app.patch('/api/users/update/:id', (req, res) => {
    const { id }= req.params;
    const { name } = req.body;
    const user = users.map(data => {
        if (data.id == id) data.name = name
        return {
            id: data.id,
            name: data.name 
        }
    })
    res.json({ok: true, users:user})    
})

//delete, request o, response o
app.delete('/api/users/delete', (req, res) => {
    const { id }= req.params;
    const user = users.filter(data => data.id != id);
    res.json({ok: true, users:user})    
})

module.exports = app;