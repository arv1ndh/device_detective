import 'package:flutter/material.dart';

import '../models/devices.dart';
import './devices_card.dart';

class DevicesScreen extends StatelessWidget {
  List<Device> devices = createTestDevice();

  //might want to use list with builder method not grid view

  @override
  Widget build(BuildContext context) {
    return GridView(
      //children: devices.map((devData) => DeviceCard(devData)).toList(),
      children: <Widget>[
        Text('Hello'),
        Text('Hello'),
        Text('Hello'),
        Text('Hello'),
        Text('Hello'),
        Text('Hello'),
        Text('Hello'),
        Text('Hello'),
        Text('Hello'),
        Text('Hello'),
        Text('Hello'),
        Text('Hello'),
      ],
      gridDelegate: SliverGridDelegateWithMaxCrossAxisExtent(
        maxCrossAxisExtent: 200,
        childAspectRatio: 3 / 2,
        crossAxisSpacing: 20,
        mainAxisSpacing: 20,
      ),
    );
  }
}
