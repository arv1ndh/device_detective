const mongoose = require('mongoose')
const pusher = require('pusher')
const bodyParser = require("body-parser")
const Schema = mongoose.Schema;
require('dotenv').config()
const io = require('../index')

var my_URI = process.env.MONGODB_URI;

var channels_client = new pusher({
    appId: process.env.appId,
    key: process.env.key,
    secret: process.env.secret,
    cluster: process.env.cluster,
    encrypted: process.env.encrypted
  });
//connect to database
console.log('Attempting connection...')
mongoose.connect(my_URI, {useUnifiedTopology: true, useNewUrlParser: true, useCreateIndex: true})
.then(()=> {
    console.log("MongoDB Connected...")
    const db = mongoose.connection;
    const collection = db.collection("posts");
    const changeStream = collection.watch();

 // start listen to changes
    changeStream.on("change", function(change) {
    console.log('Change has occured');
    console.log(JSON.stringify(change));
    if(change.operationType === 'insert') {
        channels_client.trigger(
          'my-channel',
          'inserted', 
          {
            message: 'device added'
          }
        ); 
      }

    });
})
.catch((e) => console.log('There is an error here: '+e))

