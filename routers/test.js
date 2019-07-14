var express = require('express')
var router = express.Router()
var path = require('path')
var exec = require('child_process').exec;

var count = 0;
var location = ['Hack1.py']
router.get("/", function(req, res, next){
    res.render('test')
})

router.post("/sent", function (req, res, next) {
    console.log(req.body.keyword);
    script_path = 
    child = exec("python ./scripts/"+location[0]+ " " + req.body.keyword, function (error, result, stderr) {
        console.log("script : "+ result)
        if (error !== null) {
            console.log('exec error: ' + error);
        }          
        res.render('result', data)
    });
    data = {keyword : req.body.keyword}
    /*
    setTimeout(function() {
        res.render('result', data)
      }, 3000);
      */
});

module.exports = router