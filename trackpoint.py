import configparser
import string
import os
Config=configparser.ConfigParser()

tp_path="/sys/devices/platform/i8042/serio1/driver/serio2/"
tp_config_path=os.environ.get('HOME')+"/.config/trackpoint.conf"
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
    Config.read(tp_config_path)
    for i in tp_labels:
        if (Config.has_option('DEFAULT', i[0]) == False \
                or Config ['DEFAULT'] [i[0]] == ''):
            Config['DEFAULT'] [i[0]] = get_setting(tp_path + i[0])
    with open(tp_config_path, 'w') as configfile:
        Config.write(configfile)

def store_current_settings():
    Config.read(tp_config_path)
    if (Config.has_section('CURRENT')) == False :
        Config.add_section('CURRENT')
    for i in tp_labels:
        Config['CURRENT'] [i[0]] = get_setting(tp_path + i[0])
        with open(tp_config_path, 'w') as configfile:
            Config.write(configfile)


def store_changed_settings(option, preference):
    Config.read(tp_config_path)
    Config['DEFAULT'] [option] = preference
    with open(tp_config_path, 'w') as configfile:
        Config.write(configfile)

def retrieve_config_settings(section):
    Config.read(tp_config_path)
    tp_values = []
    if Config.has_section('DEFAULT') == False:
        store_default_settings()
    if Config.has_section('CURRENT') == False:
        for i in tp_labels:
            tp_values.append(Config ['DEFAULT'] [i[0]])     
    else:
        for i in tp_labels:
            tp_values.append(Config[section] [i[0]])
    return (tp_values)


def apply_stored_settings(section):
    tp_values=retrieve_config_settings(section)
    for count, item in enumerate(tp_labels):
        set_setting(tp_path+item[0], str(tp_values[count])) 