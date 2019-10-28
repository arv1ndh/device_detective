import 'package:flutter/cupertino.dart';

import '../widgets/carousel_card.dart';

class Device {
  final String name;
  final String vendor;
  final String type;
  final double version; // or double?
  final String osName;
  final double osVersion;
  final String browserName;
  final double browserVersion;
  final String browserVendor;
  final String browserEngine;
  final bool isBot;
  final bool isCrawler;
  final bool hasTouchScreen;
  final String appName;
  final double appVersion;

  Device(
      {this.name,
      this.vendor,
      this.type,
      this.version,
      this.osName,
      this.osVersion,
      this.browserName,
      this.browserVersion,
      this.browserVendor,
      this.browserEngine,
      this.isBot,
      this.isCrawler,
      this.hasTouchScreen,
      this.appName,
      this.appVersion});

  String get deviceName {
    return name;
  }

  String get deviceVendor {
    return vendor;
  }

  int get deviceType {
    int numType = 0;
    if (type == 'iPhone') {
      // add all types and make it enum
      numType = 1;
    } else if (type == 'Galaxy or mobile') {
      numType = 2;
    } else if (type == 'iPad Pro or tablet') {
      numType = 3;
    } else if (type == 'Laptop') {
      numType = 4;
    } else if (type == 'Unknown') {
      numType = 0;
    }

    return numType;

    //return deviceType;
  }

  double get deviceVersion {
    return version;
  }

  String get deviceOsName {
    return osName;
  }

  double get deviceOsVersion {
    return osVersion;
  }

  String get deviceBrowserName {
    return browserName;
  }

  double get deviceBrowserVersion {
    return browserVersion;
  }

  String get deviceBrowserVendor {
    return browserVendor;
  }

  String get deviceBrowserEngine {
    return browserEngine;
  }

  bool get deviceIsBot {
    return isBot;
  }

  bool get deviceIsCrawler {
    return isCrawler;
  }

  bool get deviceHasTouchScreen {
    return hasTouchScreen;
  }

  String get deviceAppName {
    return appName;
  }

  double get deviceAppVersion {
    return appVersion;
  }
}

List<Device> createTestDevice() {
  List<Device> devices = [];
  var one = new Device(
      name: 'Johns Phone',
      vendor: 'Apple',
      type: 'iPhone',
      version: 5.2,
      osName: 'iOS',
      osVersion: 3.2,
      browserName: 'Safari',
      browserVendor: 'Apple',
      browserEngine: '',
      browserVersion: 8.1,
      isBot: false,
      isCrawler: false,
      hasTouchScreen: true,
      appName: 'unknown',
      appVersion: 0);

  var two = new Device(
      name: 'Alexs Andorid',
      vendor: 'Samsung',
      type: 'Galaxy or mobile',
      version: 3.8,
      osName: 'AndroidOS',
      osVersion: 9.8,
      browserName: 'Google Chrome',
      browserVendor: 'Google',
      browserEngine: 'Chrome',
      browserVersion: 5.2,
      isBot: false,
      isCrawler: false,
      hasTouchScreen: true,
      appName: 'Test',
      appVersion: 5.6);

  var three = new Device(
      name: 'Ajs iPad',
      vendor: 'Apple',
      type: 'iPad Pro or tablet',
      version: 3.8,
      osName: 'iOS',
      osVersion: 10.8,
      browserName: 'Safari',
      browserVendor: 'Apple',
      browserEngine: '',
      browserVersion: 3.2,
      isBot: false,
      isCrawler: false,
      hasTouchScreen: true,
      appName: 'Test222',
      appVersion: 98.6);

  var four = new Device(
      name: '565876414',
      vendor: 'Unkown',
      type: 'Unknown',
      version: 0,
      osName: 'Unknown',
      osVersion: 0,
      browserName: 'Google Chrome',
      browserVendor: 'Google',
      browserEngine: 'Chrome',
      browserVersion: 5.2,
      isBot: false,
      isCrawler: false,
      hasTouchScreen: false,
      appName: '',
      appVersion: 0);

  var five = new Device(
      name: 'Lala Laptop',
      vendor: 'Apple',
      type: 'Laptop',
      version: 2.3,
      osName: 'MacOS',
      osVersion: 5.6,
      browserName: 'Google Chrome',
      browserVendor: 'Google',
      browserEngine: 'Chrome',
      browserVersion: 5.2,
      isBot: false,
      isCrawler: false,
      hasTouchScreen: false,
      appName: '',
      appVersion: 0);

  devices.add(one);
  devices.add(two);
  devices.add(three);
  devices.add(four);
  devices.add(five);

  return devices;
}

/*
List<Widget> deviceWidgets(List<Device> devices) {
  List<Widget> widgets;

  for (var i = 0; i < devices.length; i++) {
    CarouselCard card = new CarouselCard(devices[i]);
    widgets.add(card);
  }

  return widgets;
}

 */
