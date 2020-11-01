var express = require('express');
var router = express.Router();
const { PythonShell } = require("python-shell");


console.log('dirname : ' + __dirname);

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/a/:port', function(req, res, next) {
  console.log('dirname : ' + __dirname);
  let options = {
    scriptPath: "",
    args: [req.params.port, req.query.d]
  };

  PythonShell.run("..\\python\\ardulight_arg.py", options, function(err, data) {
    if (err) {
      console.log(err)
      res.send({result: "error"});
    } else {
      if(data[0].indexOf(`[${req.params.port}]`) != -1) {
        res.send({result: "ok"});
      } else {
        res.send({result: "error"});
      }
      
    }

  });

  console.log(req.params.port)
  console.log(req.query.d)

  
});

module.exports = router;
