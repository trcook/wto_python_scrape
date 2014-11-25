#!/usr/bin/env node


// load filesystem module
var fs = require("fs");

// read JS file and execute it
var data = fs.readFileSync("disputes.js", {encoding: "utf8"});
eval(data);

// write data out to files
fs.writeFile("disputes.json", JSON.stringify(ds_array));

