import 'package:flutter/material.dart';
import 'Screens/cameraScreen.dart';
import 'Screens/problemScreen.dart';
import 'Screens/solutionScreen.dart';
import 'Screens/explainScreen.dart';
import 'const.dart';

void main() => runApp(grammarsolver());

class grammarsolver extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        buttonColor: appcolor,
        buttonTheme: ButtonThemeData(
          textTheme: ButtonTextTheme.primary,
        ),
      ),
      initialRoute: '/',
      routes: {
        '/': (BuildContext context) => CameraScreen(),
        '/problem': (BuildContext context) => ProblemScreen(),
        '/solution': (BuildContext context) => SolutionScreen(),
        '/explain': (BuildContext context) => ExplainScreen(),
      },
    );
  }
}
