const mongoose = require('mongoose')
const Schema = mongoose.Schema;
require('dotenv').config()


var my_URI = process.env.MONGODB_URI;

console.log('mongoose file')
//connect to database
mongoose.connect(my_URI, {useUnifiedTopology: true, useNewUrlParser: true, useCreateIndex: true})
.then(()=> {console.log("MongoDB Connected...")})
.catch((e) => console.log('There is an error here: '+e))


