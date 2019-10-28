const mongoose = require('mongoose')
const Schema = mongoose.Schema;
require('dotenv').config()

//heroku didnt like using an inermediate value. must put it directly into the mongoos.connect()
var my_URI = process.env.MONGODB_URI;

//connect to database
console.log('Attempting connection...')
mongoose.connect("mongodb+srv://mobileapp:thisisatest@cluster0-kdfv3.mongodb.net/tests?retryWrites=true&w=majority", {useUnifiedTopology: true, useNewUrlParser: true, useCreateIndex: true})
.then(()=> {console.log("MongoDB Connected...")})
.catch((e) => console.log('There is an error here: '+e))


