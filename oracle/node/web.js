var oracledb = require('oracledb');
var dbConfig = require('./dbConfig');
var express = require('express');
var path = require('path');
var bodyParser = require('body-parser');
const { queryObjects } = require('v8');

oracledb.initOracleClient({libDir:'/opt/oracle/instantclient_21_13'})

var app = express();
app.set('Port',process.env.PORT || 3000);
app.set(bodyParser.urlencoded({extenede:true}));
app.set(bodyParser.json());

oracledb.autoCommit = true;

app.get('/', function(req,res){
    res.send('Web Server Started~!!');
})

app.get('/dbTestSelect', function(req,res){
    oracledb.getConnection(
        {
            user:dbConfig.user,
            password: dbConfig.password,
            connectString: dbConfig.connectString
        }, 
        function(err, connection){
            if(err) {
                console.error(err.message);
                return;
            }
            let qurey = 'select * from usertbl';

            connection.execute(query, [],
                function (err,result){
                    if(err){
                        console.error(err.message);
                        doRelease(connection);
                        return;
                    }
                    console.log(result.metaData);
                    console.log(result.rows);
                })
            })
            function doRelease(connection,rowList) {
                connection.release(
                    function (err) {
                        if(err) {
                            console.error(err.message);
                        }
                        console.log('List size :' + rowList.length);
                        res.send(rowList);
                    }
                )
            }
})        


app.all('*', function(req, res) {
    res.status(404).send('<h1>404 Not Found</h1>');
})

app.listen(app.get('Port'), function() {
    console.log('3000 Port: Server started~!!')
})