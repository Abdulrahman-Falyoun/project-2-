import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'package:grammarsolver/const.dart';
import 'cameraScreen.dart';
import 'ButtonInBottom.dart';

class ProblemScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        elevation: 10,
        title: Text(
          'Problem',
          style: englishbuttontextstyle,
        ),
        backgroundColor: appcolor,
      ),
      body: SafeArea(
        child: Padding(
            padding: EdgeInsets.symmetric(
              horizontal: 20.0,
            ),
            child: ProblemText()),
      ),
    );
  }
}

class ProblemText extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.spaceAround,
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: <Widget>[
        Expanded(
          child: Container(
            padding: EdgeInsets.all(10),
            margin: EdgeInsets.symmetric(vertical: 10, horizontal: 5),
            height: 200,
            width: double.infinity,
            decoration: BoxDecoration(
//              color: Color(0xFFe0e0e0),
              borderRadius: BorderRadius.circular(10),
            ),
//            child: istext == true
//                ? Text(
//                    newtext,
//                    style: englishnormaltextstyle,
//                  )
//                : Image.file(
//                    imagefile,
//                    fit: BoxFit.cover,
//                    height: 300,
//                    width: MediaQuery.of(context).size.width,
//                    alignment: Alignment.topCenter,
//                  ),
            child: imagefile == null
                ? Text(
                    newtext,
                    style: englishnormaltextstyle,
                  )
                : Image.file(
                    imagefile,
                    fit: BoxFit.cover,
                    height: 300,
                    width: MediaQuery.of(context).size.width,
                    alignment: Alignment.topCenter,
                  ),
          ),
        ),
        SizedBox(
          height: 2,
          child: Container(
            color: appcolor,
          ),
        ),
        SizedBox(
          height: 5,
        ),
        ButtonInBottom()
      ],
    );
  }
}
