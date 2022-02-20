trackpointpath="/sys/devices/platform/i8042/serio1/driver/serio2/"
tf=trackpointpath + "speed"

def get_setting(tf):
    f = open(tf, "r")
    r = f.read()
    f.close()
    return r

def set_setting(tf, ts):
    f = open(tf, "r+")
    f.write(ts)
    f.close()

set_setting(trackpointpath + "speed", "30")
print("speed = ", get_setting(trackpointpath + "speed"))