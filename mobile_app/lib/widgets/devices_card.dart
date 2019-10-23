import 'package:flutter/material.dart';

import '../models/devices.dart';

class DeviceCard extends StatelessWidget {
  final Device device;
  DeviceCard(this.device);

  @override
  Widget build(BuildContext context) {
    return Container(
        color: Theme.of(context).accentColor,
        child: Text(device.name), //
        decoration: BoxDecoration(
          borderRadius: BorderRadius.all(
            Radius.circular(15),
          ),
        ));
  }
}
