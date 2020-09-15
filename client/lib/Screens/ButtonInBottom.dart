import 'package:flutter/material.dart';
import 'package:grammarsolver/const.dart';
import 'cameraScreen.dart';
import 'problemScreen.dart';

class ButtonInBottom extends StatefulWidget {
  @override
  _ButtonInBottomState createState() => _ButtonInBottomState();
}

class _ButtonInBottomState extends State<ButtonInBottom> {
  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[
        RaisedButton(
          onPressed: () {
            showDialog(
              context: context,
              builder: (_) => SimpleDialog(
                title: Center(
                  child: Text(
                    'Hint',
                    style: englishnormaltextstyle,
                  ),
                ),
                elevation: 10,
                children: <Widget>[
                  SizedBox(
                    height: 2,
                    child: Container(
                      color: appcolor,
                    ),
                  ),
                  Container(
                    width: 220,
                    height: 180,
                    child: Center(
                      child: Text(
                        '${(solutionWay == null) ? solutiontext : solutionWay[0]}',
                        style: englishnormaltextstyle,
                      ),
                    ),
                  ),
                  Padding(
                    padding: EdgeInsets.symmetric(vertical: 1, horizontal: 10),
                    child: RaisedButton(
                      color: appcolor,
                      elevation: 3,
                      child: Text(
                        'Back',
                        style: englishbuttontextstyle,
                      ),
                      onPressed: () {
                        Navigator.pop(context);
                      },
                    ),
                  ),
                ],
              ),
            );
          },
          color: appcolor,
          child: Text(
            'Hint',
            style: englishbuttontextstyle,
          ),
        ),
        SizedBox(
          width: 10,
        ),
        RaisedButton(
          onPressed: () {
            Navigator.pushNamed(context, '/solution');
          },
          color: appcolor,
          child: Text(
            'Solve',
            style: englishbuttontextstyle,
          ),
        ),

//        RaisedButton(
//          onPressed: () {
//            Navigator.pushNamed(context, '/explain');
//          },
//          color: appcolor,
//          child: Text(
//            'Explain',
//            style: englishbuttontextstyle,
//          ),
//        ),
      ],
    );
  }
}
