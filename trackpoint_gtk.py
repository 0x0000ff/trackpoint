import gi
import trackpoint

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self) -> None:
        super().__init__(title="Trackpoint Settings")
        self.Box1 = Gtk.VBox(spacing=6)
        self.add(self.Box1)
        self.Box2 = Gtk.Box(spacing=6)
        self.Box1.pack_start(self.Box2, True, True, 0)

        self.Box3 = Gtk.VBox(spacing=6)
        self.Box2.pack_start(self.Box3, True, True, 0)
        self.Box4 = Gtk.VBox(spacing=6)
        self.Box2.pack_start(self.Box4, True, True, 0)
        self.ButtonBox = Gtk.Box(spacing=6)
        self.Box1.pack_start(self.ButtonBox, True, True, 0)

        self.tp_values = trackpoint.retrieve_config_settings()
        
        self.SensitivityScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.SensitivityScale.set_value(int(self.tp_values[0]))
        self.Box3.pack_start(self.SensitivityScale, True, True, 0)   
        
        self.SpeedScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.SpeedScale.set_value(int(self.tp_values[1]))
        self.Box3.pack_start(self.SpeedScale, True, True, 0)   
        
        self.InertiaScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.InertiaScale.set_value(int(self.tp_values[2]))
        self.Box3.pack_start(self.InertiaScale, True, True, 0)   
        
        self.ReachScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.ReachScale.set_value(int(self.tp_values[3]))
        self.Box3.pack_start(self.ReachScale, True, True, 0)   
        
        self.DraghysScale = Gtk.Scale.new_with_range(0, 0, 255, 1)
        self.DraghysScale.set_value(int(self.tp_values[4]))
        self.Box3.pack_start(self.DraghysScale, True, True, 0)   
        
        self.MindragScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.MindragScale.set_value(int(self.tp_values[5]))
        self.Box3.pack_start(self.MindragScale, True, True, 0)   
        
        self.ThreshScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.ThreshScale.set_value(int(self.tp_values[6]))
        self.Box3.pack_start(self.ThreshScale, True, True, 0)   
        
        self.UpthreshScale = Gtk.Scale.new_with_range(0, 0, 255, 1)
        self.UpthreshScale.set_value(int(self.tp_values[7]))
        self.Box4.pack_start(self.UpthreshScale, True, True, 0)   
        
        self.ZtimeScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.ZtimeScale.set_value(int(self.tp_values[8]))
        self.Box4.pack_start(self.ZtimeScale, True, True, 0)   
        
        self.JenksScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.JenksScale.set_value(int(self.tp_values[9]))
        self.Box4.pack_start(self.JenksScale, True, True, 0)   
        
        self.Press_to_selectScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.Press_to_selectScale.set_value(int(self.tp_values[10]))
        self.Box4.pack_start(self.Press_to_selectScale, True, True, 0)   
        
        self.SkipbackScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.SkipbackScale.set_value(int(self.tp_values[11]))
        self.Box4.pack_start(self.SkipbackScale, True, True, 0)   
        
        self.Ext_devScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.Ext_devScale.set_value(int(self.tp_values[12]))
        self.Box4.pack_start(self.Ext_devScale, True, True, 0)   
        
        self.ListofScales = (self.Box3.get_children())
        self.ListofScales = self.ListofScales + self.Box4.get_children()

        self.DefaultButton = Gtk.Button(label="Default")
        self.DefaultButton.connect("clicked", self.on_button_clicked)
        self.ButtonBox.pack_start(self.DefaultButton, True, True, 0)

        self.ResetButton = Gtk.Button(label="Reset")
        self.ResetButton.connect("clicked", self.on_button_clicked)
        self.ButtonBox.pack_start(self.ResetButton, True, True, 0)

        self.ApplyButton = Gtk.Button(label="Apply")
        self.ApplyButton.connect("clicked", self.on_button_clicked)
        self.ButtonBox.pack_start(self.ApplyButton, True, True, 0)


    def on_button_clicked(self,widget):
        print("Hello World")
        for i in self.ListofScales:
            print (i.get_value())
        print (self.tp_values)
    
    def on_scale_draw(self,widget,something):
            widget.set_value(200)


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()