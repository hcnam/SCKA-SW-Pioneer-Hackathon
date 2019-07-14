var express = require('express');
var app = express();
var path = require('path')
var exec = require('child_process').exec;
var bodyParser = require('body-parser')
app.use(bodyParser.urlencoded({extended: false}))
app.use(bodyParser.json())

app.use(express.static('public'));

app.set('views', path.join(__dirname, 'views'))
app.set('view engine', 'ejs');

app.get('/', function(req,res){
    res.render('index')
});

app.use(function (err, req, res, next) {
	console.error(err);
	res.end("<h1>ERROR!</h1>")
});

var result = require('./routers/result')
app.use('/result', result)

var test = require('./routers/test')
app.use('/test', test)

app.listen(3000, function () {
  console.log('port:3000 is operating..');
});

