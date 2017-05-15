"""provide functions to load, save, and configure runtime parameters"""
import keys
import os

DEFAULT_CONFIG = {
    "port": "COM1",
    "baud": "19200",
    "channel": "null",
    "write_key": "null",
    "update_rate": "3"
}

HOME = os.path.expanduser("~")
CFG_FILE = os.path.join(HOME, "s2ts.cfg")

API_KEY = keys.THINGSPEAK_API_KEY

def save_config(cfg):
    """save cfg to file"""
    print()
    print("saving config")
    outfile = open(CFG_FILE, 'w')
    for k in cfg:
        outfile.write("%s=%s\n"%(k, cfg[k]))
    outfile.close()

def load_config():
    """loads and returns the config from file or generates and returns a copy of default config"""
    if os.path.exists(CFG_FILE):
        print("loading config")
        infile = open(CFG_FILE, 'r')
        lines = infile.readlines()
        infile.close()
        cfg = {}
        for line in lines:
            items = line.split("=")
            cfg[items[0]] = items[1].strip("\n")
        return cfg
    else:
        print("no config file found - using default config")
        save_config(DEFAULT_CONFIG)
        cfg_copy = {}
        for k in DEFAULT_CONFIG:
            cfg_copy[k] = DEFAULT_CONFIG[k]
        return cfg_copy

def set_port(cfg):
    """prompts user to select/type a serial port name/path and returns the chosen port name"""
    current = cfg["port"]
    print("***** PORT *****")
    print("for Windows - type COM# where # is a number (1 to 256) - no spaces between COM and #")
    print("for Linux/MacOS - type the path to the device")
    print("leave blank to use current: %s"%current)
    port = None
    while not port:
        port = input("PORT: ")
        if (port == ""):
            print("using current: %s"%current)
            return
    cfg["port"] = port

def set_baud(cfg):
    """prompts user to input a baud rate and returns the baud chosen"""
    current = cfg["baud"]
    print("***** BAUD *****")
    print("leave blank to use current: %s"%current)
    baud = None
    while not baud:
        baud = input("BAUD: ")
        if baud == "":
            print("using current: %s"%current)
            return
        try:
            int(baud)
            cfg["baud"] = baud
        except ValueError:
            baud = None
            print("BAUD must be an integer")

def set_channel(cfg):
    """prompts user for a ThingSpeak channel id"""
    current = cfg["channel"]
    print("***** THINGSPEAK CHANNEL *****")
    print("leave blank to use current: %s"%current)
    channel = None
    while not channel:
        channel = input("CHANNEL: ")
        if channel == "":
            print("using current: %s"%current)
            return
    cfg["channel"] = channel

def set_write_key(cfg):
    """prompts user for a ThingSpeak write key"""
    current = cfg["write_key"]
    print("***** THINGSPEAK WRITE KEY *****")
    print("leave blank to use current: %s"%current)
    write_key = None
    while not write_key:
        write_key = input("KEY: ")
        if write_key == "":
            print("using current: %s"%current)
            return
    cfg["write_key"] = write_key

def set_update_rate(cfg):
    """prompts user to provide an integer value for update rate in minutes"""
    current = cfg["update_rate"]
    print("***** RATE *****")
    print("update rate in minutes - must be an integer (3 to 10)")
    print("leave blank to use current: %s"%current)
    rate = None
    while not rate:
        rate = input("RATE: ")
        if rate == "":
            print("using current: %s"%current)
            return
        try:
            tmp = int(rate)
            if tmp >= 3 and tmp <= 10:
                cfg["update_rate"] = rate
            else:
                raise ValueError
        except ValueError:
            rate = None
            print("RATE must be an integer (3 to 10)")
