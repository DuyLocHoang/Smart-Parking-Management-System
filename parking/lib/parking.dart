import 'package:json_annotation/json_annotation.dart';

part 'parking.g.dart';

@JsonSerializable()
class Parking {
  Parking(this.name,this.location,this.status,this.reservedStatus);
  String name;
  String location;
  bool status;
  bool reservedStatus;
  factory Parking.fromJson(Map<String, dynamic> json) => _$ParkingFromJson(json);
  Map<String,dynamic> toJson() => _$ParkingToJson(this);
}