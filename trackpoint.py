tp_labels = ["sensitivity", "speed", "inertia", "reach", "draghys", \
    "mindrag", "thresh", "upthresh", "ztime", "jenks", "press_to_select", \
        "skipback", "ext_dev"]
tp_path="/sys/devices/platform/i8042/serio1/driver/serio2/"

def get_setting(tf):
    f = open(tf, "rt",newline='\n')
    r = f.readline()
    f.close()
    return r.replace('\n', '')
    #return r

def set_setting(tf, ts):
    f = open(tf, "r+")
    f.write(ts)
    f.close()

#set_setting(tp_path + "speed", "30")
print (tp_path + tp_labels[1])
print(get_setting(tp_path + tp_labels[1]))