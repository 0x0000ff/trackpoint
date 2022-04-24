import configparser
import string
Config=configparser.ConfigParser()


tp_path="/sys/devices/platform/i8042/serio1/driver/serio2/"
scale = 1
checkbutton = 2
tp_labels = ["sensitivity", scale, 128],\
    ["speed", scale, 254], ["press_to_select", checkbutton, 1], \
    ["inertia", scale, 254], ["reach", scale, 254], ["draghys", scale, 254], \
    ["mindrag", scale, 254], ["thresh", scale, 254], ["upthresh", scale, 254], ["ztime", scale, 254],\
    ["jenks", scale, 254], ["skipback", checkbutton, 1], ["ext_dev", checkbutton, 1], 

def get_setting(tf):
    f = open(tf, "rt",newline='\n')
    r = f.readline()
    f.close()
    return r.replace('\n', '')

def set_setting(tpFilename, tpValue):
    f = open(tpFilename, "r+")
    f.write(str(tpValue))
    f.close()

def store_default_settings():
    Config.read('trackpoint.conf')
    for i in tp_labels:
        if (Config.has_option('DEFAULT', i[0]) == False \
                or Config ['DEFAULT'] [i[0]] == ''):
            Config['DEFAULT'] [i[0]] = get_setting(tp_path + i[0])
    with open('trackpoint.conf', 'w') as configfile:
        Config.write(configfile)

def store_changed_settings(option, preference):
    Config.read('trackpoint.conf')
    Config['DEFAULT'] [option] = preference
    with open('trackpoint.conf', 'w') as configfile:
        Config.write(configfile)

def retrieve_config_settings():
    Config.read('trackpoint.conf')
    tp_values = []
    for i in tp_labels:
        tp_values.append(Config ['DEFAULT'] [i[0]])     
    return (tp_values)
