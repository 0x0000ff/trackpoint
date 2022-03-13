import configparser
Config=configparser.ConfigParser()

tp_path="/sys/devices/platform/i8042/serio1/driver/serio2/"
tp_labels = ["sensitivity", "speed", "inertia", "reach", "draghys", \
    "mindrag", "thresh", "upthresh", "ztime", "jenks", "press_to_select", \
        "skipback", "ext_dev"]

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

def store_default_settings():
    Config.read('trackpoint.conf')
    for i in tp_labels:
        if (Config.has_option('DEFAULT', i) == False \
                or Config ['DEFAULT'] [i] == ''):
            Config['DEFAULT'] [i] = get_setting(tp_path + i)
    with open('trackpoint.conf', 'w') as configfile:
        Config.write(configfile)

def retrieve_config_settings():
    Config.read('trackpoint.conf')
    tp_values = []
    for i in tp_labels:
        tp_values.append(Config ['DEFAULT'] [i])     
    return (tp_values)

store_default_settings() 
#print (retrieve_config_settings())