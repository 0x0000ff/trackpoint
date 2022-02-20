import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self) -> None:
        super().__init__(title="Trackpoint Settings")

        self.scale1 = Gtk.Scale.new_with_range(0, 0, 200, 1)
        self.button = Gtk.Button(label="apply")
        self.button.connect("clicked", self.on_button_clicked)
        #self.add(self.button)
        self.add(self.scale1)
    
    def on_button_clicked(self,widget):
        print("Hello World")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()