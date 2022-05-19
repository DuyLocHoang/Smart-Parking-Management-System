class User {
  String name;
  String location;
  bool status;
  bool reservedStatus;
  User(this.name, this.location,this.status,this.reservedStatus);
  User.fromJson(Map<String, dynamic> json)
      : name = json['name'],
        location = json['location'],
        status = json['status'],
        reservedStatus = json['reservedStatus'];
  Map<String, dynamic> toJson() => {
        'name': name,
        'location': location,
        'status' : status,
        'reservedStatus' : reservedStatus
      };
}