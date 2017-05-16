"""starts the main program loop"""
import sys
import time
import config
import gps
import requests
import serial

API_URL = "https://api.thingspeak.com/update.json?api_key={write_key}&field1={lat}&field2={lon}&field3={time}"
READ_TIMEOUT = 2#seconds

def update_thingspeak(cfg, lat, lon):
    """updates thingspeak channel with lat lon"""
    url = API_URL.replace("{write_key}", cfg["write_key"]).replace("{lat}", str(lat)).replace("{lon}", str(lon))
    success = False
    try:
        req = requests.get(url)
        if req.status_code == 200:
            print("updated ThingSpeak")
            success = True
        elif req.status_code == 404:
            print("unable to update ThingSpeak - please verify channel and/or write key")
        else:
            print(req.content)
    except requests.exceptions.ConnectionError:
        print("ERROR: check internet connection")
    return success

def configure():
    """loads, configures, and saves runtime configuration"""
    cfg = config.load_config()
    config.set_port(cfg)
    config.set_baud(cfg)
    config.set_update_rate(cfg)
    #config.set_channel(cfg)
    config.set_write_key(cfg)
    config.save_config(cfg)

def run():
    """opens the serial port, reads and parses data, updates ThingSpeak"""
    print("***** RUN *****")
    cfg = config.load_config()
    last_update = time.time()
    update_rate_seconds = 5#int(cfg["update_rate"])*60
    ser = serial.Serial()
    ser.port = cfg["port"]
    ser.baudrate = cfg["baud"]
    ser.timeout = READ_TIMEOUT
    try:
        print("opening serial port: %s"%cfg["port"])
        ser.open()
    except:
        print("ERROR: unable to open serial port")
        raise KeyboardInterrupt#raise to go to menu instead of exiting

    while True:
        try:
            data = ser.readline()
            time_delta = time.time() - last_update
            if data:
                gps_string = data.decode("utf-8")
                print(gps_string.strip("\n"))
                if time_delta > update_rate_seconds:
                    print("updating ThingSpeak")
                    lat, lng = gps.extract_lat_lng(gps_string)
                    if lat and lng:
                        updated = update_thingspeak(cfg, lat, lng)
                        if updated:
                            last_update = time.time()
                        else:
                            print("failed to update ThingSpeak - trying again in 10 seconds")
                            #set last_update so that an update will be attempted in 10 seconds
                            last_update = time.time() - update_rate_seconds + 10
            else:
                print("input timeout")
        except KeyboardInterrupt:
            if ser.is_open:
                print("\nclosing serial port: %s"%cfg["port"])
                ser.close()
            #bubble the exception out of the run() function to for menu to be shown
            raise KeyboardInterrupt

def menu():
    """provides a menu for the user to choose to run, confiure, or quit the application"""
    choice = None
    while not choice:
        print("\n***** MENU *****")
        print("r) RUN")
        print("c) CONFIGURE")
        print("q) QUIT")
        choice = input(">> ").lower()
        if choice == "r":
            return
        elif choice == "c":
            configure()
        elif choice == "q":
            sys.exit()
        else:
            print("invalid option")
            choice = None

def main():
    """application entry point"""
    while True:
        try:
            run()
        except KeyboardInterrupt:
            menu()

main()
