import 'package:flutter/material.dart';
import 'package:carousel_slider/carousel_slider.dart';

import 'carousel_card.dart';
import '../models/devices.dart';

class Carousel extends StatefulWidget {
  @override
  _CarouselState createState() => _CarouselState();
}

class _CarouselState extends State<Carousel> {
  static List<Device> devices = createTestDevice();
  List<int> counter = new List<int>.generate(devices.length, (i) => i + 0);

  @override
  Widget build(BuildContext context) {
    return CarouselSlider(
      autoPlay: true,
      autoPlayInterval: Duration(seconds: 3),
      autoPlayAnimationDuration: Duration(milliseconds: 1500),
      pauseAutoPlayOnTouch: Duration(seconds: 5),
      enlargeCenterPage: true,
      aspectRatio: 2.0,
      height: MediaQuery.of(context).size.height * 0.2,
      items: counter.map((i) {
        return Builder(
          builder: (BuildContext context) {
            return Container(
              width: MediaQuery.of(context).size.width * 0.4,
              margin: EdgeInsets.symmetric(horizontal: 1.0),
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(20.0),
                color: Theme.of(context).primaryColor,
              ),
              child: CarouselCard(device: devices[i]), //
            );
          },
        );
      }).toList(),
    );
    ;
  }
}
