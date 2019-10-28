import 'package:flutter/material.dart';

import '../models/devices.dart';

class CarouselCard extends StatefulWidget {
  final Device device;
  CarouselCard({Key key, this.device}) : super(key: key);

  @override
  _CarouselCardState createState() => _CarouselCardState();
}

class _CarouselCardState extends State<CarouselCard> {
  String getImage(Device d) {
    int type = d.deviceType;
    String image;
    if (type == 1) {
      image = 'assets/images/smartphone.png';
      return image;
    } else if (type == 2) {
      image = 'assets/images/smartphone.png';
      return image;
    } else if (type == 3) {
      image = 'assets/images/tablet.png';
      return image;
    } else if (type == 4) {
      image = 'assets/images/laptop.png';
      return image;
    }
    image = 'assets/images/question.png';
    return image;
  }

  String deviceText(Device d) {
    String text = '';
    // name, devicetype, osname, browsername
    String type;
    if (d.deviceType == 1) {
      // add all types and make it enum
      type = 'Mobile';
    } else if (d.deviceType == 2) {
      type = 'Mobile';
    } else if (d.deviceType == 3) {
      type = 'Tablet';
    } else if (d.deviceType == 4) {
      type = 'PC';
    } else {
      type = 'Unknown';
    }
    text = 'Name: ' +
        d.name +
        '\n' +
        'Type: ' +
        type +
        '\n' +
        'OS: ' +
        d.osName +
        '\n' +
        'Browser: ' +
        d.browserName +
        '\n';

    return text;
  }

  @override
  void initState() {
    super.initState();

    // Additional initialization of the State
  }

  Widget build(BuildContext context) {
    return Container(
      child: Row(
        children: <Widget>[
          Padding(
            padding: const EdgeInsets.all(20.0),
            child: Image.asset(getImage(widget.device)),
          ),
          Text(
            deviceText(widget.device),
            style: TextStyle(color: Colors.white),
          )
        ],
      ),
    );
  }
}

//Icons made by "https://www.flaticon.com/authors/freepik"
/*



  Container(
      child: Row(
        children: <Widget>[
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Image.asset(),
          ),
          Text(
            'test',
            style: TextStyle(color: Colors.white),
          )
        ],
      ),
    );
 */
