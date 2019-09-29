//jshint esversion:6
const express = require('express');
const bodyParser = require('body-parser');
const request = require('request');
const app = express();

app.use(express.static(__dirname));
app.use(bodyParser.urlencoded({extended: true}));

app.get("/", function(rec, res) {
  res.render("index");
});

// Process a submitted form
app.post('/', function(req, res){

});

app.listen(process.env.PORT || 8080, function() {
  console.log("Server hosted on magic port 8080");
});
