import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self) -> None:
        super().__init__(title="Trackpoint Settings")

        self.box1 = Gtk.Box(spacing=6)
        self.add(self.box1)

        self.box2 = Gtk.VBox(spacing=6)
        self.box1.pack_start(self.box2, True, True, 0)
        self.box3 = Gtk.VBox(spacing=6)
        self.box1.pack_start(self.box3, True, True, 0)
        
        self.SensitivityScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.box2.pack_start(self.SensitivityScale, True, True, 0)   
        
        self.SpeedScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.box2.pack_start(self.SpeedScale, True, True, 0)   
        
        self.InertiaScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.box2.pack_start(self.InertiaScale, True, True, 0)   
        
        self.ReachScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.box2.pack_start(self.ReachScale, True, True, 0)   
        
        self.DraghysScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.box2.pack_start(self.DraghysScale, True, True, 0)   
        
        self.MindragScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.box2.pack_start(self.MindragScale, True, True, 0)   
        
        self.ThreshScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.box2.pack_start(self.ThreshScale, True, True, 0)   
        
        self.UpthreshScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.box3.pack_start(self.UpthreshScale, True, True, 0)   
        
        self.ZtimeScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.box3.pack_start(self.ZtimeScale, True, True, 0)   
        
        self.JenksScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.box3.pack_start(self.JenksScale, True, True, 0)   
        
        self.Press_to_selectScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.box3.pack_start(self.Press_to_selectScale, True, True, 0)   
        
        self.SkipbackScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.box3.pack_start(self.SkipbackScale, True, True, 0)   
        
        self.Ext_devScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.box3.pack_start(self.Ext_devScale, True, True, 0)   
        
    def on_button_clicked(self,widget):
        print("Hello World")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()