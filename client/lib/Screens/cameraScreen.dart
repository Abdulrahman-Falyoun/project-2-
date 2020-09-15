import 'dart:convert';
import 'dart:async';
import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'package:animated_text_kit/animated_text_kit.dart';
import 'package:image_picker/image_picker.dart';
import 'package:grammarsolver/const.dart';
import 'package:flutter_plugin_android_lifecycle/flutter_plugin_android_lifecycle.dart';
import 'dart:io';
import 'package:http/http.dart' as http;
import 'package:path/path.dart';
import 'package:async/async.dart';

List<dynamic> solutionWay = [];
Map objectReceived = {};
File imagefile;
String newtext = '';
String solutiontext = '';
String selectedGrammar = 'Finder';
String grammar = '';
bool istext = false;
Future response;

class CameraScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        elevation: 10,
        title: Text(
          'English Solver',
          style: englishbuttontextstyle,
        ),
        backgroundColor: appcolor,
      ),
      body: SafeArea(
        child: WelcomePage(),
      ),
    );
  }
}

class WelcomePage extends StatefulWidget {
  @override
  _WelcomePageState createState() => _WelcomePageState();
}

class _WelcomePageState extends State<WelcomePage> {
  DropdownButton<String> androidDropdown() {
    List<DropdownMenuItem<String>> dropdownItems = [];
    for (String Grammar in ["Finder", "Conjunction", "Question"]) {
      var newItem = DropdownMenuItem(
        child: Text(Grammar),
        value: Grammar,
      );
      dropdownItems.add(newItem);
    }

    return DropdownButton<String>(
      value: selectedGrammar,
      items: dropdownItems,
      onChanged: (value) {
        setState(() {
          selectedGrammar = value;
          grammar = selectedGrammar;
          print(grammar);
        });
      },
    );
  }

  void openImagePicker(BuildContext context) {
    showModalBottomSheet(
        context: context,
        builder: (BuildContext context) {
          return Container(
            height: 180,
            padding: EdgeInsets.all(15),
            child: Column(
              children: <Widget>[
                Text(
                  'Pick an image',
                  style: englishnormaltextstyle,
                ),
                SizedBox(
                  height: 10,
                ),
                FlatButton(
                  color: appcolor,
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: <Widget>[
                      SizedBox(
                        width: 20,
                      ),
                      Text(
                        'Use camera',
                        style: englishbuttontextstyle,
                      ),
                    ],
                  ),
                  onPressed: () async {
                    await getImage(context, ImageSource.camera);
                    print(imagefile);
                    Navigator.pushNamed(context, '/problem');
                  },
                ),
                SizedBox(
                  height: 5,
                ),
                FlatButton(
                  color: appcolor,
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: <Widget>[
                      SizedBox(
                        width: 20,
                      ),
                      Text(
                        'Use gallery',
                        style: englishbuttontextstyle,
                      ),
                    ],
                  ),
                  onPressed: () async {
                    await getImage(context, ImageSource.gallery);
                    Navigator.pushNamed(context, '/problem');
                  },
                ),
              ],
            ),
          );
        });
  }

  Future getImage(BuildContext context, ImageSource sourse) async {
    final File image = await ImagePicker.pickImage(source: sourse);
    setState(() {
      imagefile = image;
    });
//    await http
//        .post(
//      "http://192.168.1.7:3000/",
//      headers: {
//        "Content-type": "application/json",
//        "Accept": "application/json"
//      },
//      body: json.encode({
//        "image": image != null
//            ? 'data:image/png;base64,' + base64Encode(image.readAsBytesSync())
//            : '',
//     "grammar":grammar
//      }),
//    )
//        .then((http.Response response) {
//      objectReceived = json.decode(response.body);
//      solutiontext = objectReceived['result'];
//      solutionWay = objectReceived['result way'];
//      print(solutionWay);
//      print(solutiontext);
//    });
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: <Widget>[
        SizedBox(
          child: TypewriterAnimatedTextKit(
              text: ['Grammer Solver'],
              textStyle: englishtitletextstyle,
              textAlign: TextAlign.center,
              alignment: AlignmentDirectional.topStart),
        ),
        SizedBox(
          height: 2,
          child: Container(
            width: 100,
            color: appcolor,
          ),
        ),
        Expanded(
          flex: 4,
          child: Padding(
            padding: EdgeInsets.all(10.0),
          ),
        ),
        Expanded(
          child: Center(
            child: Padding(
              padding: EdgeInsets.all(15.0),
              child: androidDropdown(),
            ),
          ),
        ),
        Expanded(
          child: Padding(
            padding: EdgeInsets.all(15.0),
            child: FlatButton(
              color: appcolor,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: <Widget>[
                  Icon(
                    Icons.camera_alt,
                    size: 30,
                    color: Colors.white,
                  ),
                  SizedBox(
                    width: 20,
                  ),
                  Text(
                    'Take a pic',
                    style: englishbuttontextstyle,
                  ),
                ],
              ),
              onPressed: () {
                openImagePicker(context);
              },
            ),
          ),
        ),
        Expanded(
          child: Padding(
            padding: EdgeInsets.all(15.0),
            child: FlatButton(
              color: appcolor,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: <Widget>[
                  Icon(
                    Icons.text_fields,
                    size: 30,
                    color: Colors.white,
                  ),
                  SizedBox(
                    width: 20,
                  ),
                  Text(
                    'Enter a text',
                    style: englishbuttontextstyle,
                  ),
                ],
              ),
              onPressed: () {
                showDialog(
                  context: context,
                  builder: (_) => SimpleDialog(
                    title: Center(
                      child: Text(
                        'Enter a text',
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
                          child: TextField(
                            maxLines: 99,
                            expands: false,
                            textAlign: TextAlign.center,
                            decoration: InputDecoration(
                              border: InputBorder.none,
                              hintText: 'Enter a text',
                              hintStyle: TextStyle(fontSize: 25),
                            ),
                            style: englishnormaltextstyle,
                            onChanged: (text) {
                              setState(() {
                                istext = true;
                                newtext = text;
                              });
                            },
                          ),
                        ),
                      ),
                      Padding(
                        padding:
                            EdgeInsets.symmetric(vertical: 1, horizontal: 10),
                        child: RaisedButton(
                          color: appcolor,
                          elevation: 3,
                          child: Text(
                            'Submit',
                            style: englishbuttontextstyle,
                          ),
                          onPressed: () async {
                            final Map<String, dynamic> imagedata = {
                              "text": newtext,
                              "grammar": grammar
                            };

                            await http
                                .post(
                              "http://192.168.1.4:3000/text",
                              headers: {
                                "Content-type": "application/json",
                                "Accept": "application/json"
                              },
                              body: json.encode(imagedata),
                            )
                                .then((http.Response response) {
                              objectReceived = json.decode(response.body);
                              solutiontext = objectReceived['result'] != ''
                                  ? objectReceived['result']
                                  : '';
                              solutionWay = objectReceived['result way'] != null
                                  ? objectReceived['result way']
                                  : [''];
                              print(solutionWay);
                              print(solutiontext);
                            });
                            Navigator.pushNamed(context, '/problem');
                          },
                        ),
                      ),
                    ],
                  ),
                );
              },
            ),
          ),
        ),
      ],
    );
  }
}
