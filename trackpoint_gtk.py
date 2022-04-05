from cProfile import label
import gi
import trackpoint

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
tp_values=trackpoint.retrieve_config_settings()

class MyWindow(Gtk.Window):
    def __init__(self) -> None:
        super().__init__(title="Trackpoint Settings")
        self.Box1 = Gtk.VBox(spacing=6)
        self.add(self.Box1)
        self.Grid1 = Gtk.Grid()
        self.Grid1.set_column_homogeneous(True)
        self.Grid1.set_row_baseline_position(1, 1)
        self.Box1.pack_start(self.Grid1, True, True, 0)
        self.ButtonBox = Gtk.Box(spacing=6)
        self.Box1.pack_start(self.ButtonBox, False, False, 0)

        self.tp_values = trackpoint.retrieve_config_settings()
        
        self.Widgets = []
        for count, item in enumerate(trackpoint.tp_labels):
            WidgetHolder = Gtk.Label.new(item[0])
            self.Widgets.append(WidgetHolder)
            if (item[1] == trackpoint.scale):
                WidgetHolder = Gtk.Scale.new_with_range(0,0,item[2],1)
                WidgetHolder.set_round_digits(1)
                WidgetHolder.set_value(float(tp_values[count]))
                WidgetHolder.set_valign(4)
            if (item[1] == trackpoint.checkbutton):
                WidgetHolder = Gtk.CheckButton.new()
            self.Widgets.append(WidgetHolder)

            y_more = 0
            x_more = 0
        for count, item in enumerate(self.Widgets):
            if (count > 12):
               y_more = 2 
               x_more = 12
            if (count % 2 == 0):
                self.Grid1.attach(item, 1+y_more, count-x_more, 1, 1) 
            if (count % 2 != 0):
                self.Grid1.attach(item, 2+y_more, count-x_more, 1, 1) 

        self.DefaultButton = Gtk.Button(label="Default")
        self.ButtonBox.pack_start(self.DefaultButton, False, False, 0)

        self.AdvancedButton = Gtk.Button(label="Advanced >>")
        self.AdvancedButton.connect("clicked", self.on_advanced_clicked)
        self.ButtonBox.pack_start(self.AdvancedButton, False, False, 0)

        self.ResetButton = Gtk.Button(label="Reset")
        self.ButtonBox.pack_end(self.ResetButton, False, False, 0)

        self.ApplyButton = Gtk.Button(label="Apply")
        self.ApplyButton.connect("clicked", self.on_apply_clicked)
        self.ButtonBox.pack_end(self.ApplyButton, False, False, 0)
        
    def on_advanced_clicked(self,widget):
        if (widget.get_label() != "Advanced <<"):
            widget.set_label("Advanced <<")
            for i in range(6, 25):
                win.show_all()
            self.resize(700,250)
        else:
            widget.set_label("Advanced >>")
            for i in range(6, 25):
                self.Widgets[i].hide()
            self.resize(400,100)

    def on_apply_clicked(self,widget):
        print ("fuck")
        for count, item in enumerate(trackpoint.tp_labels):
            print (self.Widgets[count*2+1].get_name())
            if (self.Widgets[count*2+1].get_name() == "GtkScale"):
                print (self.Widgets[count*2+1].get_value())
                trackpoint.store_changed_settings(trackpoint.tp_labels[count] [0], str(int(self.Widgets[count*2+1].get_value())))
            if (self.Widgets[count*2+1].get_name() == "GtkCheckButton"):
                trackpoint.store_changed_settings(trackpoint.tp_labels[count] [0], ((str(int(self.Widgets[count*2+1].get_active())))))
    
    def on_scale_draw(self,widget,something):
            widget.set_value(200)

    def initial_show(self):
        win.show_all()
        for count, item in enumerate (self.Widgets):
            if (count > 5):
                self.Widgets[count].hide()
        self.resize(200,50)

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.initial_show()
Gtk.main()