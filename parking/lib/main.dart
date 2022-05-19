// import 'package:flutter/material.dart';

// void main() {
//   runApp(const MyApp());
// }

// class MyApp extends StatelessWidget {
//   const MyApp({Key? key}) : super(key: key);

//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       title: "Parking",
//       theme: ThemeData(primarySwatch: Colors.blue),
//       home: const MyHomePage(title: "Home",),
//     );
//   }
// }

// class MyHomePage extends StatefulWidget {
//   const MyHomePage({Key? key, required this.title}) : super(key: key);

//   final String title;

//   @override
//   _MyHomePageState createState() => _MyHomePageState();
// }

// class _MyHomePageState extends State<MyHomePage> {
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//         appBar: AppBar(
//           backgroundColor: Colors.amber,
//           title: Text(
//             widget.title, //Home
//             style: const TextStyle(color: Colors.black),
//           ),
//         ),
//         body: const Center(
//           child: Text(
//             "Hello World",
//             style: TextStyle(
//                 color: Colors.orange,
//                 fontSize: 40,
//                 fontWeight: FontWeight.bold,
//                 backgroundColor: Colors.black),
//           ),
//         ));
//   }
// }
// // -------------------------------------------------------------------------------------------

// // void main() {
// //   runApp(const MyApp());
// // }

// // class MyApp extends StatelessWidget {
// //   const MyApp({Key? key}) : super(key: key);

// //   // This widget is the root of your application.
// //   @override
// //   Widget build(BuildContext context) {
// //     return MaterialApp(
// //       title: 'Flutter Demo',
// //       theme: ThemeData(
// //         // This is the theme of your application.
// //         //
// //         // Try running your application with "flutter run". You'll see the
// //         // application has a blue toolbar. Then, without quitting the app, try
// //         // changing the primarySwatch below to Colors.green and then invoke
// //         // "hot reload" (press "r" in the console where you ran "flutter run",
// //         // or simply save your changes to "hot reload" in a Flutter IDE).
// //         // Notice that the counter didn't reset back to zero; the application
// //         // is not restarted.
// //         primarySwatch: Colors.blue,
// //       ),
// //       home: const MyHomePage(title: 'Flutter Demo Home Page'),
// //     );
// //   }
// // }

// // class MyHomePage extends StatefulWidget {
// //   const MyHomePage({Key? key, required this.title}) : super(key: key);

// //   // This widget is the home page of your application. It is stateful, meaning
// //   // that it has a State object (defined below) that contains fields that affect
// //   // how it looks.

// //   // This class is the configuration for the state. It holds the values (in this
// //   // case the title) provided by the parent (in this case the App widget) and
// //   // used by the build method of the State. Fields in a Widget subclass are
// //   // always marked "final".

// //   final String title;

// //   @override
// //   State<MyHomePage> createState() => _MyHomePageState();
// // }

// // class _MyHomePageState extends State<MyHomePage> {
// //   int _counter = 0;

// //   void _incrementCounter() {
// //     setState(() {
// //       // This call to setState tells the Flutter framework that something has
// //       // changed in this State, which causes it to rerun the build method below
// //       // so that the display can reflect the updated values. If we changed
// //       // _counter without calling setState(), then the build method would not be
// //       // called again, and so nothing would appear to happen.
// //       _counter++;
// //     });
// //   }

// //   @override
// //   Widget build(BuildContext context) {
// //     // This method is rerun every time setState is called, for instance as done
// //     // by the _incrementCounter method above.
// //     //
// //     // The Flutter framework has been optimized to make rerunning build methods
// //     // fast, so that you can just rebuild anything that needs updating rather
// //     // than having to individually change instances of widgets.
// //     return Scaffold(
// //       appBar: AppBar(
// //         // Here we take the value from the MyHomePage object that was created by
// //         // the App.build method, and use it to set our appbar title.
// //         title: Text(widget.title),
// //       ),
// //       body: Center(
// //         // Center is a layout widget. It takes a single child and positions it
// //         // in the middle of the parent.
// //         child: Column(
// //           // Column is also a layout widget. It takes a list of children and
// //           // arranges them vertically. By default, it sizes itself to fit its
// //           // children horizontally, and tries to be as tall as its parent.
// //           //
// //           // Invoke "debug painting" (press "p" in the console, choose the
// //           // "Toggle Debug Paint" action from the Flutter Inspector in Android
// //           // Studio, or the "Toggle Debug Paint" command in Visual Studio Code)
// //           // to see the wireframe for each widget.
// //           //
// //           // Column has various properties to control how it sizes itself and
// //           // how it positions its children. Here we use mainAxisAlignment to
// //           // center the children vertically; the main axis here is the vertical
// //           // axis because Columns are vertical (the cross axis would be
// //           // horizontal).
// //           mainAxisAlignment: MainAxisAlignment.center,
// //           children: <Widget>[
// //             const Text(
// //               'You have pushed the button this many times:',
// //             ),
// //             Text(
// //               '$_counter',
// //               style: Theme.of(context).textTheme.headline4,
// //             ),
// //           ],
// //         ),
// //       ),
// //       floatingActionButton: FloatingActionButton(
// //         onPressed: _incrementCounter,
// //         tooltip: 'Increment',
// //         child: const Icon(Icons.add),
// //       ), // This trailing comma makes auto-formatting nicer for build methods.
// //     );
// //   }
// // }

// import "package:flutter/material.dart";

// void main() {
//   runApp(const MyApp());
// }

// class MyApp extends StatelessWidget {
//   const MyApp({Key? key}) : super(key: key);

//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       title: " App Counter",
//       home: const MyHomePage(),
//     );
//   }
// }

// class MyHomePage extends StatefulWidget {
//   const MyHomePage({Key? key}) : super(key: key);

//   @override
//   _MyHomePageState createState() => _MyHomePageState();
// }

// class _MyHomePageState extends State<MyHomePage> {
//   int _counter = 0;
//   void countUp() {
//     print("Pushed Counter Up");
//     setState(() {
//       _counter++;
//     });

//     print('$_counter');
//   }

//   void countDown() {
//     print("Pushed Counter Down");
//     setState(() {
//       _counter--;
//     });
//     print('$_counter');
//   }

//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: const Text("Home"),
//       ),
//       body: Center(
//         child: Column(
//           mainAxisAlignment: MainAxisAlignment.center,
//           children: [
//             const Text("Counter Values: "),
//             Text(
//               '$_counter',
//               style: TextStyle(color: Colors.red, fontSize: 40),
//             )
//           ],
//         ),
//       ),
//       floatingActionButton: Padding(
//         padding: EdgeInsets.all(8),
//         child: Row(
//           mainAxisAlignment: MainAxisAlignment.end,
//           children: <Widget>[
//             FloatingActionButton(
//               onPressed: countDown,
//               child: const Icon(Icons.remove),
//             ),
//             FloatingActionButton(
//               onPressed: countUp,
//               child: const Icon(Icons.add),
//             ),
//           ],
//         ),
//       ),
//       // floatingActionButton: FloatingActionButton(
//       //   onPressed: countUp,
//       //   child: const Icon(Icons.add),
//       // ),
//     );
//   }
// }

// import 'package:flutter/material.dart';

// void main() {
//   runApp(const MyApp());
// }

// class MyApp extends StatelessWidget {
//   const MyApp({Key? key}) : super(key: key);

//   @override
//   Widget build(BuildContext context) {
//     return const MaterialApp(
//       title: "Navigate new screen",
//       home: FirstRoute(),
//     );
//   }
// }

// class FirstRoute extends StatelessWidget {
//   const FirstRoute({Key? key}) : super(key: key);

//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: const Text("First Screen"),
//       ),
//       body: Center(
//         child: ElevatedButton(
//           child: const Text("Open Second Screen"),
//           onPressed: () {
//             Navigator.push(context,
//                 MaterialPageRoute(builder: (context) => SecondRoute()));
//           },
//         ),
//       ),
//     );
//   }
// }

// class SecondRoute extends StatelessWidget {
//   const SecondRoute({Key? key}) : super(key: key);

//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: const Text("Second Screen"),
//       ),
//       body: Center(
//         child: ElevatedButton(
//           child: const Text("Back First Screen"),
//           onPressed: () {
//             Navigator.pop(context);
//           },
//         ),
//       ),
//     );
//   }
// }

// import 'package:flutter/material.dart';

// void main() {
//   runApp(const MyApp());
// }

// class MyApp extends StatelessWidget {
//   const MyApp({Key? key}) : super(key: key);

//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       routes: {
//         DetailScreen.nameRoute: (context) => const DetailScreen(),
//       },
//       title: "My Home Page",
//       home: const MyHomePage(),
//     );
//   }
// }

// class MyHomePage extends StatelessWidget {
//   const MyHomePage({Key? key}) : super(key: key);

//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: const Text("Home"),
//       ),
//       body: Center(
//         child: Column(
//           mainAxisAlignment: MainAxisAlignment.center,
//           children: [
//             ElevatedButton(
//                 onPressed: () {
//                   Navigator.pushNamed(context, DetailScreen.nameRoute,
//                       arguments: ArgumentScreen("Title 1", "Content 1"));
//                 },
//                 child: const Text('Item 1')),
//             ElevatedButton(
//                 onPressed: () {
//                   Navigator.pushNamed(context, DetailScreen.nameRoute,
//                       arguments: ArgumentScreen("Title 2", "Content 2"));
//                 },
//                 child: const Text('Item 2'))
//           ],
//         ),
//       ),
//     );
//   }
// }

// class DetailScreen extends StatelessWidget {
//   const DetailScreen({Key? key}) : super(key: key);
//   static const nameRoute = '/Detail';
//   @override
//   Widget build(BuildContext context) {
//     final args = ModalRoute.of(context)!.settings.arguments as ArgumentScreen;
//     return Scaffold(
//       appBar: AppBar(
//         title: Text(args.title),
//       ),
//       body: Center(
//         child: Text(args.content),
//       ),
//     );
//   }
// }

// class ArgumentScreen {
//   String title ;
//   String content ;
//   ArgumentScreen(this.title, this.content);
// }

// import 'package:flutter/material.dart';

// void main() {
//   runApp(const MyApp());
// }

// class MyApp extends StatelessWidget {
//   const MyApp({Key? key}) : super(key: key);

//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       title: "Home",
//       home: MyHomePage(),
//     );
//   }
// }

// class MyHomePage extends StatelessWidget {
//   MyHomePage({Key? key}) : super(key: key);
//   List<Station> stations = [
//     Station(1, 'Tram 01', 'public', true),
//     Station(2, 'Tram 02', 'public', true),
//     Station(3, 'Tram 03', 'private', false),
//     Station(4, 'Tram 05', 'private', false),
//     Station(5, 'Tram 05', 'private', false),
//     Station(6, 'Tram 06', 'public', true),
//     Station(7, 'Tram 07', 'public', true),
//     Station(8, 'Tram 08', 'private', false),
//     Station(9, 'Tram 09', 'private', false),
//     Station(10, 'Tram 10', 'private', false)
//   ];
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(title: const Text("Home")),
//       body: ListView.builder(
//           itemCount: stations.length,
//           itemBuilder: (context, index) {
//             final item = stations[index];
//             return ListTile(
//               leading: Icon(Icons.online_prediction,
//                   color: item.status ? Colors.blue : Colors.black12),
//               title: Text(item.name,style: TextStyle(color: Colors.orange),),
//               trailing:
//                   Icon(item.type == 'publish' ? Icons.public : Icons.lock),
//             );
//           }),
//     );
//   }
// }

// class Station {
//   int id;
//   String name;
//   String type;
//   bool status;
//   Station(this.id, this.name, this.type, this.status);
// }

// import 'package:flutter/material.dart';

// void main() {
//   runApp(const MyApp());
// }

// class MyApp extends StatelessWidget {
//   const MyApp({Key? key}) : super(key: key);

//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       routes: {StationDetail.nameRoute: (context) => const StationDetail()},
//       title: "Home",
//       home: MyHomePage(),
//     );
//   }
// }

// class MyHomePage extends StatelessWidget {
//   MyHomePage({Key? key}) : super(key: key);
//   List<Station> stations = [
//     Station(1, 'Tram 01', 'public', true, 20.1),
//     Station(2, 'Tram 02', 'public', true, 20.2),
//     Station(3, 'Tram 03', 'private', false, 20.3),
//     Station(4, 'Tram 04', 'private', false, 20.4),
//     Station(5, 'Tram 05', 'private', false, 20.5),
//     Station(6, 'Tram 06', 'public', true, 20.6),
//     Station(7, 'Tram 07', 'public', true, 20.7),
//     Station(8, 'Tram 08', 'private', false, 20.8),
//     Station(9, 'Tram 09', 'private', false, 20.9),
//     Station(10, 'Tram 10', 'private', false, 30.0)
//   ];
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: Text("Home"),
//       ),
//       body: GridView.count(
//         crossAxisCount: 2,
//         childAspectRatio: 1.5,
//         children: stations.map((item) {
//           return StationItem(item: item);
//         }).toList(),
//       ),
//     );
//   }
// }

// class StationItem extends StatelessWidget {
//   const StationItem({Key? key, required this.item}) : super(key: key);
//   final Station item;
//   @override
//   Widget build(BuildContext context) {
//     return InkWell(
//       onTap: () {
//         print("CLick ${item.name}");
//         Navigator.pushNamed(context, StationDetail.nameRoute, arguments: item);
//       },
//       splashColor: Colors.orange,
//       child: Card(
//         child: Container(
//           alignment: Alignment.center,
//           child: Text(
//             item.name,
//             style: TextStyle(
//                 color: Colors.orange,
//                 fontSize: 25,
//                 fontWeight: FontWeight.bold),
//           ),
//           color: item.status ? Colors.green : Colors.black12,
//         ),
//       ),
//     );
//   }
// }

// class StationDetail extends StatelessWidget {
//   const StationDetail({Key? key}) : super(key: key);
//   static const nameRoute = '/Detail';
//   @override
//   Widget build(BuildContext context) {
//     final item = ModalRoute.of(context)!.settings.arguments as Station;
//     return Scaffold(
//       appBar: AppBar(
//         backgroundColor: item.status?Colors.green:Colors.black12,
//         title: Text(item.name),
//       ),
//       body: Center(
//         child: Row(
//             mainAxisAlignment: MainAxisAlignment.center,
//             crossAxisAlignment: CrossAxisAlignment.start,
//             children: [
//               Text(
//                 '${item.temp}',
//                 style: TextStyle(color: Colors.red, fontSize: 50),
//               ),
//               Text(
//                 'o',
//                 style: TextStyle(color: Colors.red, fontSize: 30),
//               ),
//               Text(
//                 'C',
//                 style: TextStyle(color: Colors.red, fontSize: 50),
//               ),
//             ]),
//       ),
//     );
//   }
// }

// class Station {
//   int id;
//   String name;
//   String type;
//   bool status;
//   double temp;
//   Station(this.id, this.name, this.type, this.status, this.temp);
// }



// import 'dart:html';

// import 'package:flutter/material.dart';
// import 'package:json_annotation/json_annotation.dart';
// // import 'package:socket_io_client/socket_io_client.dart' as IO;
// import 'package:web_socket_channel/web_socket_channel.dart';
// import 'dart:convert';
// import 'parking.dart';
// import 'user.dart';
// void main() {
  
//   runApp(const MyApp());
// }

// class MyApp extends StatelessWidget {
//   const MyApp({Key? key}) : super(key: key);

//   // This widget is the root of your application.
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       title: 'Flutter Demo',
//       theme: ThemeData(
//         primarySwatch: Colors.blue,
//       ),
//       home: const Home(),
//     );
//   }
// }

// class Home extends StatelessWidget {
//   const Home({Key? key}) : super(key: key);

//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: const Text('Home'),
//       ),
//       body: Center(
//         child: Column(
//           mainAxisAlignment: MainAxisAlignment.center,
//           children: [
//             ElevatedButton(
//                 onPressed: () {
//                   Navigator.pushNamed(context, DetailScreen.nameRoute,
//                       arguments: ArgumentScreen("Title 1", "Content 1"));
//                 },
//                 child: const Text('Item 1')),
//             ElevatedButton(
//                 onPressed: () {
//                   Navigator.pushNamed(context, DetailScreen.nameRoute,
//                       arguments: ArgumentScreen("Title 2", "Content 2"));
//                 },
//                 child: const Text('Item 2'))
//           ],
//         ),
//       ),
//     );
//   }
// }

// class MyHomePage extends StatefulWidget {
//   const MyHomePage({Key? key, required this.title}) : super(key: key);
//   final String title;
//   static const nameRoute = '/Detail';

//   @override
//   State<MyHomePage> createState() => _MyHomePageState();
// }

// class _MyHomePageState extends State<MyHomePage> {
//   // int _counter = 0;
//   List<Parking> stations = [];
//   // late IO.Socket socket;
//   List<ParkingSpace> _parkingSpaces =[];
//   List<ParkingSpace> get parkingSpaces => _parkingSpaces;
//   set  parkingSpaces(newVal) => _parkingSpaces = newVal;
  
//   @override
//   void initState() {
//     // TODO: implement initState
//     super.initState();
//     connectAndListen();
//   }

//   void connectAndListen() {
//     print('Call func connectAndListen');
//     final channel = WebSocketChannel.connect(Uri.parse('ws://localhost:8080/data'));
//     channel.stream.listen((message) {
//       statuses = [];
//       _parkingSpaces = [];
//     // print(message.runtimeType );
//     // var ab = json.decode(message);
//     // print(ab.runtimeType);
//     // print(ab);
//     for (var location in json.decode(message)){
//       // print(location.runtimeType);
//       _parkingSpaces.add(ParkingSpace.fromMap(location));
//       print(_parkingSpaces.runtimeType);
//       setState(() {
//         statuses = _parkingSpaces;
//       });
//     }
//     print(_parkingSpaces.length);

//     channel.sink.add('received!');
//     // channel.sink.close();
//   });
//   }

//   @override
//   Widget build(BuildContext context) {
//     // final args = ModalRoute.of(context)!.settings.arguments as ParkingSpace;
//     return Scaffold(
//       appBar: AppBar(
//         title: Text("Parking"),
//       ),
//       body: 
//     );
//   }
// }

// class MyHomePage extends StatelessWidget {
//   const MyHomePage({Key? key}) : super(key: key);
//   static const nameRoute = '/Detail';

//   @override
//   Widget build(BuildContext context) {
//     List<ParkingSpace> item = ModalRoute.of(context)!.settings.arguments ;
//     return Scaffold(
//       appBar: AppBar(
//         title: const Text('Home'),
//       ),
//       body: GridView.count(
//         childAspectRatio: 1.5,
//         crossAxisCount: 2,
//         children: item.map((item) {
//           return StationItem(item: item);
//         }).toList(),
//       ),
//     );
//   }
// }


// class StationItem extends StatelessWidget {
//   const StationItem({Key? key, required this.item}) : super(key: key);
//   final ParkingSpace item;
//   @override
//   Widget build(BuildContext context) {
//     return InkWell(
//       onTap: () {
//         print('Clicked ${item.name}');
//       },
//       splashColor: Colors.red,
//       child: Card(
//         child: Container(
//           color: item.status == false ? Colors.green : Colors.black12,
//           alignment: Alignment.center,
//           child: Text(
//             item.name,
//             style: TextStyle(
//                 color: Colors.orange,
//                 fontSize: 25,
//                 fontWeight: FontWeight.bold),
//           ),
//         ),
//       ),
//     );
//   }
// }

// @JsonSerializable(explicitToJson: true)
// class ParkingSpace {
//   String name;
//   String location;
//   bool status;
//   bool reservedStatus;

//   ParkingSpace({required this.name, required this.location, required this.status, required this.reservedStatus});


//   factory ParkingSpace.fromMap(Map<String, dynamic> data){
//     return ParkingSpace(
//       name: data['name'],
//       location: data['location'],
//       status: data['status'] == "true" ? true : false,
//       reservedStatus: data['reserve_status']== "0" ? true : false
//     );
//   }
// }



import 'dart:html';

import 'package:flutter/material.dart';
import 'package:json_annotation/json_annotation.dart';
// import 'package:socket_io_client/socket_io_client.dart' as IO;
import 'package:web_socket_channel/web_socket_channel.dart';
import 'dart:convert';
import 'parking.dart';
import 'user.dart';
void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Parking',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Parking Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);
  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  // int _counter = 0;
  List<Parking> stations = [];
  // late IO.Socket socket;
  List<ParkingSpace> _parkingSpaces =[];
  List<ParkingSpace> get parkingSpaces => _parkingSpaces;
  set  parkingSpaces(newVal) => _parkingSpaces = newVal;
  List<ParkingSpace> statuses = [];
  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    connectAndListen();
  }

  void connectAndListen() {
    print('Call func connectAndListen');
    final channel = WebSocketChannel.connect(Uri.parse('ws://localhost:8080/data'));
    channel.stream.listen((message) {
      statuses = [];
      _parkingSpaces = [];
    // print(message.runtimeType );
    // var ab = json.decode(message);
    // print(ab.runtimeType);
    // print(ab);
    for (var location in json.decode(message)){
      // print(location.runtimeType);
      _parkingSpaces.add(ParkingSpace.fromMap(location));
      print(_parkingSpaces.runtimeType);
      setState(() {
        statuses = _parkingSpaces;
      });
    }
    print(_parkingSpaces.length);

    channel.sink.add('received!');
    // channel.sink.close();
  });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Parking"),
      ),
      body: GridView.count(
        childAspectRatio: 1.5,
        crossAxisCount: 2,
        children: statuses.map((item) {
          return StationItem(item: item);
        }).toList(),
      ),
    );
  }
}

class StationItem extends StatelessWidget {
  const StationItem({Key? key, required this.item}) : super(key: key);
  final ParkingSpace item;
  @override
  Widget build(BuildContext context) {
    return InkWell(
      onTap: () {
        print('Clicked ${item.name}');
      },
      splashColor: Colors.red,
      child: Card(
        child: Container(
          color: item.status == false ? Colors.black12 : Colors.green,
          alignment: Alignment.center,
          child: Text(
            item.name,
            style: TextStyle(
                color: Colors.orange,
                fontSize: 25,
                fontWeight: FontWeight.bold),
          ),
        ),
      ),
    );
  }
}

@JsonSerializable(explicitToJson: true)
class ParkingSpace {
  String name;
  String location;
  bool status;
  bool reservedStatus;

  ParkingSpace({required this.name, required this.location, required this.status, required this.reservedStatus});


  factory ParkingSpace.fromMap(Map<String, dynamic> data){
    return ParkingSpace(
      name: data['name'],
      location: data['location'],
      status: data['status'] == "true" ? true : false,
      reservedStatus: data['reserve_status']== "0" ? true : false
    );
  }
}

