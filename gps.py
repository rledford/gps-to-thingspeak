"""provides functions for working with GPS strings"""
def extract_lat_lng(var):
    """extracts the latitude and longitude from NMEA GPS strings and converts to decimal degrees"""
    fields = var.split(',')
    lat = None
    lng = None
    for i in range(len(fields)):
        if i-1 >= 0:
            try:
                field = fields[i]
                if field == "N" or field == "S":
                    degrees = float(fields[i-1][:2])
                    dec_min = float(fields[i-1][2:])
                    lat = degrees + dec_min/60.0
                    if field == "S":
                        lat = lat * -1
                if field == "E" or field == "W":
                    degrees = float(fields[i-1][:3])
                    dec_min = float(fields[i-1][3:])
                    lng = degrees + dec_min/60.0
                    if field == "W":
                        lng = lng * -1
            except ValueError:
                print("\ninvalid lat/lng data")

    if not lat or not lng:
        print("\nERROR: unable to parse GPS string")
        return (None, None)
    else:
        return (lat, lng)
