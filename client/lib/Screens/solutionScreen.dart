import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'package:grammarsolver/const.dart';
import 'package:grammarsolver/Screens/cameraScreen.dart';
import 'package:auto_size_text/auto_size_text.dart';

class SolutionScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        elevation: 10,
        title: Text(
          'Solution',
          style: englishbuttontextstyle,
        ),
        backgroundColor: appcolor,
      ),
      body: SafeArea(
        child: Solution(),
      ),
    );
  }
}

class Solution extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[
        Expanded(
          child: Container(
            child: Align(
              alignment: Alignment.centerRight,
              child: Padding(
                padding: EdgeInsets.symmetric(horizontal: 20.0),
                child: ListView(
                  scrollDirection: Axis.vertical,
                  shrinkWrap: true,
                  children: solutionWay != null
                      ? solutionWay.map<Widget>((document) {
                          return ListTile(
                            title: Text(
                              document,
                              textAlign: TextAlign.center,
                              style: englishnormaltextstyle,
                            ),
                          );
                        }).toList()
                      : solutiontext,
                ),
              ),
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
                Padding(
                  padding:
                      EdgeInsets.symmetric(horizontal: 20.0, vertical: 20.0),
                  child: ListView(
                    scrollDirection: Axis.vertical,
                    shrinkWrap: true,
                    children: [
                      Text(
                        solutiontext,
                        style: englishbuttontextstyle,
                      ),
                    ],
                  ),
                ),
              ],
            ),
            margin: EdgeInsets.only(top: 120),
            width: double.infinity,
            height: 30,
          ),
        ),
      ],
    );
  }
}
