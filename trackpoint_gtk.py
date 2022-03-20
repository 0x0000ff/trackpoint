import gi
import trackpoint

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self) -> None:
        super().__init__(title="Trackpoint Settings")
        self.Box1 = Gtk.VBox(spacing=6)
        self.Box1.set_margin_left(6)
        self.Box1.set_margin_right(6)
        self.Box1.set_margin_top(6)
        self.Box1.set_margin_bottom(6)
        self.add(self.Box1)
        self.Grid1 = Gtk.Grid()
        self.Box1.pack_start(self.Grid1, False, False, 0)
        self.Box2 = Gtk.Box(spacing=6)
        self.Box1.pack_start(self.Box2, True, True, 0)
        self.Box3a = Gtk.VBox(spacing=6)
        self.Box2.pack_start(self.Box3a, True, True, 0)
        self.Box3 = Gtk.VBox(spacing=6)
        self.Box2.pack_start(self.Box3, True, True, 0)
        self.Box4a = Gtk.VBox(spacing=6)
        self.Box2.pack_start(self.Box4a, True, True, 0)
        self.Box4 = Gtk.VBox(spacing=6)
        self.Box2.pack_start(self.Box4, True, True, 0)
        self.ButtonBox = Gtk.Box(spacing=6)
        self.Box1.pack_start(self.ButtonBox, False, False, 0)

        self.tp_values = trackpoint.retrieve_config_settings()
        
        self.SensitivityLabel = Gtk.Label.new("Sensitivity")
        self.Grid1.attach(self.SensitivityLabel, 1, 1, 1, 1)
#        self.Box3a.pack_start(self.SensitivityLabel, False, False, 0)
        self.SpeedLabel = Gtk.Label.new("Speed")
        self.Grid1.attach(self.SpeedLabel, 1, 2, 1, 1)
#        self.Box3a.pack_start(self.SpeedLabel, False, False, 0)
        self.InertiaLabel = Gtk.Label.new("Inertia")
        self.Box3ab = Gtk.VBox(spacing=6)
        self.Box3a.pack_start(self.Box3ab, False, False, 0)
        self.Box3ab.pack_start(self.InertiaLabel, False, False, 0)
        self.ReachLabel = Gtk.Label.new("Reach")
        self.Box3ab.pack_start(self.ReachLabel, False, False, 0)
        self.DraghyLabel = Gtk.Label.new("Draghy")
        self.Box3ab.pack_start(self.DraghyLabel, False, False, 0)
        self.MindragLabel = Gtk.Label.new("Mindrag")
        self.Box4a.pack_start(self.MindragLabel, False, False, 0)
        self.ThreshLabel = Gtk.Label.new("Thresh")
        self.Box4a.pack_start(self.ThreshLabel, False, False, 0)
        self.UpthreshLabel = Gtk.Label.new("Upthresh")
        self.Box4a.pack_start(self.UpthreshLabel, False, False, 0)
        self.ZtimeLabel = Gtk.Label.new("Ztime")
        self.Box4a.pack_start(self.ZtimeLabel, False, False, 0)
        self.JenksLabel = Gtk.Label.new("Jenks")
        self.Box4a.pack_start(self.JenksLabel, False, False, 0)

       
        self.SensitivityScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.SensitivityScale.set_value(int(self.tp_values[0]))
#        self.Box3.pack_start(self.SensitivityScale, False, False, 0)   
        self.Grid1.attach(self.SensitivityScale, 2, 1, 1, 1)
        
        
        self.SpeedScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.SpeedScale.set_value(int(self.tp_values[1]))
        self.Grid1.attach(self.SpeedScale, 2, 2, 1, 1)
        #self.Box3.pack_start(self.SpeedScale, False, False, 0)   

        self.Box3b = Gtk.VBox(spacing=0)
        self.Box3.pack_start (self.Box3b, False, False, 0)
    
        self.InertiaScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.InertiaScale.set_value(int(self.tp_values[2]))
        self.Box3b.pack_start(self.InertiaScale, False, False, 0)   
        
        self.ReachScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.ReachScale.set_value(int(self.tp_values[3]))
        self.Box3b.pack_start(self.ReachScale, False, False, 0)   
        
        self.DraghysScale = Gtk.Scale.new_with_range(0, 0, 255, 1)
        self.DraghysScale.set_value(int(self.tp_values[4]))
        self.Box3b.pack_start(self.DraghysScale, False, False, 0)   
        
        self.MindragScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.MindragScale.set_value(int(self.tp_values[5]))
        self.Box4.pack_start(self.MindragScale, False, False, 0)   
        
        self.ThreshScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.ThreshScale.set_value(int(self.tp_values[6]))
        self.Box4.pack_start(self.ThreshScale, False, False, 0)   
        
        self.UpthreshScale = Gtk.Scale.new_with_range(0, 0, 255, 1)
        self.UpthreshScale.set_value(int(self.tp_values[7]))
        self.Box4.pack_start(self.UpthreshScale, False, False, 0)   
        
        self.ZtimeScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.ZtimeScale.set_value(int(self.tp_values[8]))
        self.Box4.pack_start(self.ZtimeScale, False, False, 0)   
        
        self.JenksScale = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.JenksScale.set_value(int(self.tp_values[9]))
        self.Box4.pack_start(self.JenksScale, False, False, 0)   
        
        self.SkipbackCheck = Gtk.CheckButton.new_with_label("Skipback")
        self.Box4.pack_start(self.SkipbackCheck, False, False, 0)
       
        self.Ext_devCheck = Gtk.CheckButton.new_with_label("Ext_dev")
        self.Box4.pack_start(self.Ext_devCheck, False, False, 0)
       
        self.ListofScales = (self.Box3.get_children())
        self.ListofScales = self.ListofScales + self.Box4.get_children()

        self.DefaultButton = Gtk.Button(label="Default")
        self.DefaultButton.connect("clicked", self.on_button_clicked)
        self.ButtonBox.pack_start(self.DefaultButton, False, False, 0)

        self.AdvancedButton = Gtk.Button(label="Advanced >>")
        self.AdvancedButton.connect("clicked", self.on_advanced_clicked)
        self.ButtonBox.pack_start(self.AdvancedButton, False, False, 0)

        self.ResetButton = Gtk.Button(label="Reset")
        self.ResetButton.connect("clicked", self.on_button_clicked)
        self.ButtonBox.pack_end(self.ResetButton, False, False, 0)

        self.ApplyButton = Gtk.Button(label="Apply")
        self.ApplyButton.connect("clicked", self.on_button_clicked)
        self.ButtonBox.pack_end(self.ApplyButton, False, False, 0)

        self.Press_to_selectCheck = Gtk.CheckButton.new_with_label("Press to Select")
        self.ButtonBox.pack_end(self.Press_to_selectCheck, False, False, 0)

        print(self.get_size())

    def on_advanced_clicked(self,widget):
        if (widget.get_label() != "Advanced <<"):
            widget.set_label("Advanced <<")
            self.Box4.show()
            self.Box3b.show()
            self.resize(800,400)
        else:
            widget.set_label("Advanced >>")
            self.Box4.hide()
            self.Box3b.hide()
            self.resize(400,200)

    def on_button_clicked(self,widget):
        print("Hello World")
        for i in self.ListofScales:
            print (i.get_value())
        print (self.tp_values)
    
    def on_scale_draw(self,widget,something):
            widget.set_value(200)

    def initial_show(self):
        win.show_all()
        self.resize(400,200)


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.initial_show()
Gtk.main()