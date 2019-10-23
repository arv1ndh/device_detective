import 'package:flutter/material.dart';

class Logo extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      margin: EdgeInsets.all(20),
      child: Column(
        children: <Widget>[
          Container(
            //height: MediaQuery.of(context).size.height * 0.2,
            //width: MediaQuery.of(context).size.width,
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                Text(
                  'Device Detective',
                  style: TextStyle(fontWeight: FontWeight.bold, fontSize: 32),
                ),
                Image.asset('assets/images/search.png',
                    width: MediaQuery.of(context).size.width * 0.2,
                    height: MediaQuery.of(context).size.height * 0.2),
              ],
            ),
          ),
          Container(
              margin: EdgeInsets.all(20),
              //height: MediaQuery.of(context).size.height * 0.3,
              width: MediaQuery.of(context).size.width * 0.5,
              child: Column(
                children: <Widget>[
                  Text(
                    'Project Summary',
                    style: TextStyle(fontWeight: FontWeight.bold),
                    textAlign: TextAlign.center,
                  ),
                  Container(
                    child: Text(
                      'Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
                      'sed do eiusmod tempor incididunt ut '
                      'labore et dolore magna aliqua. Sem viverra aliquet'
                      ' eget sit amet. A cras semper auctor neque vitae tempus quam '
                      'pellentesque. Commodo ullamcorper a lacus vestibulum sed. '
                      'Vestibulum mattis ullamcorper velit sed ullamcorper morbi '
                      'tincidunt. Dictum fusce ut placerat orci nulla pellentesque. '
                      'Amet aliquam id diam maecenas ultricies mi eget.',
                      textAlign: TextAlign.center,
                    ),
                  ),
                ],
              )),
        ],
      ),
    );
  }
}

//Icons made by https://www.flaticon.com/authors/freepik
