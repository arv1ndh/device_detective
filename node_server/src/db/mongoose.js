const mongoose = require('mongoose')
const Schema = mongoose.Schema;
require('dotenv').config()

//heroku didnt like using an inermediate value. must put it directly into the mongoos.connect()
//var my_URI = process.env.MONGODB_URI;

//connect to database
mongoose.connect(process.env.MONGODB_URI, {useUnifiedTopology: true, useNewUrlParser: true, useCreateIndex: true})
.then(()=> {console.log("MongoDB Connected...")})
.catch((e) => console.log('There is an error here: '+e))


