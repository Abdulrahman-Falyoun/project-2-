import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'package:grammarsolver/const.dart';

class ExplainScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        elevation: 10,
        title: Text(
          'Explanation',
          style: englishbuttontextstyle,
        ),
        backgroundColor: appcolor,
      ),
      body: SafeArea(
        child: Explanation(),
      ),
    );
  }
}

class Explanation extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[
        Align(
          alignment: Alignment.centerRight,
          child: Padding(
            padding: EdgeInsets.symmetric(horizontal: 20.0),
            child: Text(
              'explain solution way',
              style: englishnormaltextstyle,
            ),
          ),
        ),
        Expanded(
          child: Container(
            decoration: BoxDecoration(
              color: appcolor,
              borderRadius: BorderRadius.circular(10.0),
            ),
            child: Wrap(
              children: <Widget>[
                Center(
                  child:
                      Text('basic grammer used', style: englishbuttontextstyle),
                ),
              ],
            ),
            margin: EdgeInsets.only(top: 400),
            width: double.infinity,
            height: 30,
          ),
        ),
      ],
    );
  }
}
