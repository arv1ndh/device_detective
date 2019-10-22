// rm -i -rf .git (how to remove git. Must be done in the root folder of the project to remove the tracking of the project)
const express = require('express')

require('./db/mongoose')
const Device = require('./models/devices')
require('dotenv').config()

const app = express()
const port = process.env.PORT || 3000

app.use(express.json())
app.post('/devices', async (req, res) =>{
    const device = new Device(req.body)

    try{
        console.log('Attempting add a device to NetworkDevices')
        await device.save()
        console.log('Successfully added device')
        res.status(201).send(device)
    } catch (error){
        console.log('Error occured: ' + error)
        res.status(400).send(error)
    }
})


//fetch all
app.get('/devices', async (req, res) =>{
    try {
        console.log('Attempting search for all devices')
        const devices = await Device.find({})
        console.log('Successfully searched for all devices')
        res.send(devices)
    } catch (error) {
        console.log('Error occured: ' + error)
        res.status(500).send()
    }

})

//fetch specific type of device (mobile, tablet or pc)
app.get('/devices/:type', async (req, res) =>{
    const _type = req.params.type
   
    try {
        console.log('Attempting search for devices of type: '+ _type)
        const devices = await Device.find({type: _type})
        console.log('Successfully searched for all devices')
        if(devices.length == 0){
            console.log('There were no devices of type "'+_type+'".')
            return res.status(404).send('There were no devices of type "'+_type+'".')
        }
        res.send(devices)
    } catch (error) {
        console.log('Error occured: ' + error)
        res.status(500).send()
    }
})


app.listen(port, () => {
    console.log("Server is up on port " + port)
})