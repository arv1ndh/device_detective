const mongoose = require('mongoose')
const Schema = mongoose.Schema;
const validator = require('validator')

var deviceSchema = new Schema ({
  ua_string: String,
  browser: {
    family:  String,
    version: Array,
    version_string: String,
  },
  os: {
    family:  String,
    version: Array,
    version_string: String,
  },
  device: {
    family: String,
    brand: String,
    model: String,
  },
is_mobile: Boolean,
is_tablet: Boolean,
is_touch_capable: Boolean,
is_pc: Boolean,
is_bot: Boolean,
time: String,
mac: String
},{collection: 'posts'})

const Device = mongoose.model('Device', deviceSchema);

module.exports = Device

















/*
  const one = new Device({
      name: 'Johns Phone',
      vendor: 'Apple',
      type: 'iPhone',
      version: 5.2,
      os: {
        name: 'iOS',
        version: 3.2
    },
    browser: {
        name: 'Safari',
        vendor: 'Apple',
        engine: '',
        version: 8.1,

    },
      isBot: false,
      isCrawler: false,
      hasTouchScreen: true,
      app:{
          name: 'unknown',
          version: 0
      }})

  const two = new Device({
      name: 'Alexs Andorid',
      vendor: 'Samsung',
      type: 'Galaxy or mobile',
      version: 3.8,
      os:{
        name: 'AndroidOS',
        version: 9.8,
      },
      browser:{
        name: 'Google Chrome',
        vendor: 'Google',
        engine: 'Chrome',
        version: 5.2,
      },
      isBot: false,
      isCrawler: false,
      hasTouchScreen: true,
      app: {
        name: 'Test',
        version: 5.6
      }
      })

  const three = new Device ({
      name: 'Ajs iPad',
      vendor: 'Apple',
      type: 'iPad Pro or tablet',
      version: 3.8,
      os:{
        name: 'iOS',
        version: 10.8,
      },
      browser:{
        name: 'Safari',
        vendor: 'Apple',
        engien: '',
        version: 3.2,
      },
      isBot: false,
      isCrawler: false,
      hasTouchScreen: true,
      app:{
        name: 'Test222',
        version: 98.6
      }})

  const four = new Device({
      name: '565876414',
      vendor: 'Unkown',
      type: 'Unknown',
      version: 0,
      os:{
        name: 'Unknown',
        version: 0,
      },
      browser:{
        name: 'Google Chrome',
        vendor: 'Google',
        engine: 'Chrome',
        version: 5.2,
      },
      isBot: false,
      isCrawler: false,
      hasTouchScreen: false,
      app:{
        name: '',
        version: 0
      }})

  const five = new Device({
      name: 'Lala Laptop',
      vendor: 'Apple',
      type: 'Laptop',
      version: 2.3,
      os:{
        name: 'MacOS',
        version: 5.6,
      },
      browser:{
        name: 'Google Chrome',
        vendor: 'Google',
        engine: 'Chrome',
        version: 5.2,
      },
      isBot: false,
      isCrawler: false,
      hasTouchScreen: false,
      app:{
        name: '',
        version: 0
      }})
    
      const six = new Device({
        name: 'Random2',
        vendor: 'Apple',
        type: 'mobile',
        version: 2.3,
        os: {
            name: 'macOS',
            version: 96.3
        },
        browser: {
            name: 'Safari',
            vendor: 'Apple',
            engine: 'Unknown',
            version: 100.3,
    
        },
        isBot: false,
        isCrawler: false,
        hasTouchScreen: true,
        app:{
            name: 'hell.com',
            version: 52.3,
        }
    
    })
var devices = [one, two, three,four, five, six]

module.exports = devices

*/