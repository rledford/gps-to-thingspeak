def extract_lat_lng(var):
    fields = var.split(',')
    count = len(fields)
    lat = None
    lng = None

    for i in range(len(fields)):
        if i-1 >= 0:
            try:
                f = fields[i]
                if f == "N" or f == "S":
                    degrees = float(fields[i-1][:2])
                    decMin = float(fields[i-1][2:])
                    lat = degrees + decMin/60.0
                    if f == "S":
                        lat = lat * -1
                if f == "E" or f == "W":
                    degrees = float(fields[i-1][:3])
                    decMin = float(fields[i-1][3:])
                    lng = degrees + decMin/60.0
                    if f == "W":
                        lng = lng * -1
            except ValueError:
                print("invalid lat/lng data")

    if not lat or not lng:
        print("ERROR: unable to parse GPS string")
        return (None, None)
    else:
        print("lat: %f\tlng: %f"%(lat, lng))
        return (lat, lng)
