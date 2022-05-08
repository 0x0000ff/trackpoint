#!/usr/bin/python3
import gi
import trackpoint

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
tp_values=trackpoint.retrieve_config_settings('CURRENT')
class MyWindow(Gtk.Window):
    def __init__(self) -> None:
        self.rowSkip = 0
        super().__init__(title="Trackpoint Settings")
        self.Box1 = Gtk.VBox(spacing=6)
        self.add(self.Box1)
        self.Grid1 = Gtk.Grid()
        self.Grid1.set_column_homogeneous(True)
        self.Grid1.set_row_baseline_position(1, 1)
        self.Box1.pack_start(self.Grid1, True, True, 0)
        self.ButtonBox = Gtk.Box(spacing=6)
        self.Box1.pack_start(self.ButtonBox, False, False, 0)

        self.tp_values = trackpoint.retrieve_config_settings('CURRENT')
        
        self.Widgets = []
        for count, item in enumerate(trackpoint.tp_labels):
            if (item[1] == trackpoint.scale):
                WidgetHolder = Gtk.Label.new(item[0])
                self.Widgets.append(WidgetHolder)
                WidgetHolder = Gtk.Scale.new_with_range(0,0,item[2],1)
                WidgetHolder.set_round_digits(1)
                WidgetHolder.set_value(float(tp_values[count]))
            if (item[1] == trackpoint.checkbutton):
                WidgetHolder = Gtk.CheckButton.new_with_label(item[0])
                WidgetHolder.set_halign(Gtk.Align.CENTER)
            self.Widgets.append(WidgetHolder)

        nextColumn= 0
        nextRow = 0
        for count, item in enumerate(self.Widgets):
            if (count + self.rowSkip >= 12):
               nextColumn = 2 
               nextRow = 11
            if ((count + self.rowSkip) % 2 == 0):
                if (item.get_name() == "GtkCheckButton"):
                    self.Grid1.attach(item, nextColumn, count-nextRow, 1, 1) 
                    self.rowSkip += 1
                else:
                    self.Grid1.attach(item, nextColumn, count-nextRow, 1, 1) 
            if ((self.rowSkip + count) % 2 != 0):
                self.Grid1.attach(item, nextColumn+1, count-nextRow-1, 1, 1) 
            


        self.DefaultButton = Gtk.Button(label="Default")
        self.DefaultButton.connect("clicked", self.on_default_clicked)
        self.ButtonBox.pack_start(self.DefaultButton, False, False, 0)

        self.AdvancedButton = Gtk.Button(label="Advanced >>")
        self.AdvancedButton.connect("clicked", self.on_advanced_clicked)
        self.ButtonBox.pack_start(self.AdvancedButton, False, False, 0)

        self.ApplyButton = Gtk.Button(label="Apply")
        self.ApplyButton.connect("clicked", self.on_apply_clicked)
        self.ButtonBox.pack_end(self.ApplyButton, False, False, 0)
        
    def on_advanced_clicked(self,widget):
        if (widget.get_label() != "Advanced <<"):
            widget.set_label("Advanced <<")
            win.show_all()
            for count, item in enumerate (self.Widgets):
            self.resize(700,250)
        else:
            widget.set_label("Advanced >>")
            for count, item in enumerate (self.Widgets):
                if (count > 4):
                    item.hide()
            self.resize(400,100)

    def on_default_clicked(self,widget):
        trackpoint.apply_stored_settings('DEFAULT')
        values=trackpoint.retrieve_config_settings('DEFAULT')
            
    def on_apply_clicked(self,widget):
        valueCount = 0
        for item in self.Widgets:
            if (item.get_name() == "GtkCheckButton"):
                trackpoint.set_setting(trackpoint.tp_path + trackpoint.tp_labels[valueCount] [0], \
                    int(item.get_active()))
                valueCount += 1
            if (item.get_name() == "GtkScale"):
                trackpoint.set_setting(trackpoint.tp_path + trackpoint.tp_labels[valueCount] [0], \
                    int(item.get_value()))
                valueCount +=1
        trackpoint.store_current_settings()
    
    def on_scale_draw(self,widget,something):
            widget.set_value(200)

    def initial_show(self):
        win.show_all()
        for count, item in enumerate (self.Widgets):
            if (count > 4):
                item.hide()
        self.resize(200,50)

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.initial_show()
Gtk.main()