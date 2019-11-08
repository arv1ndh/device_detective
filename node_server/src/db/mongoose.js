const mongoose = require('mongoose')
const Schema = mongoose.Schema;
require('dotenv').config()

var my_URI = process.env.MONGODB_URI;

//connect to database
console.log('Attempting connection...')
mongoose.connect(my_URI, {useUnifiedTopology: true, useNewUrlParser: true, useCreateIndex: true})
.then(()=> {
    console.log("MongoDB Connected...")
    const db = mongoose.connection;
    const collection = db.collection("posts");
    const changeStream = collection.watch();
 // start listen to changes
    changeStream.on("change", function(event) {
    console.log('Change has occured');
    console.log(JSON.stringify(event));
    });
})
.catch((e) => console.log('There is an error here: '+e))


