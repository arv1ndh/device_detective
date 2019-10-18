const mongoose = require('mongoose')
const Schema = mongoose.Schema;
require('dotenv').config()


var my_URI = process.env.MONGODB_URI;
const DB_NAME = 'NetworkDevices'
const COLLECTION_NAME = 'devices'

//connect to database
mongoose.connect(my_URI, {useUnifiedTopology: true, useNewUrlParser: true, useCreateIndex: true})
.then(()=> {console.log("MongoDB Connected...")})
.catch((e) => console.log(e))


