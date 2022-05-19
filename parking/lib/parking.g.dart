// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'parking.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Parking _$ParkingFromJson(Map<String, dynamic> json) => Parking(
      json['name'] as String,
      json['location'] as String,
      json['status'] as bool,
      json['reservedStatus'] as bool,
    );

Map<String, dynamic> _$ParkingToJson(Parking instance) => <String, dynamic>{
      'name': instance.name,
      'location': instance.location,
      'status': instance.status,
      'reservedStatus': instance.reservedStatus,
    };
