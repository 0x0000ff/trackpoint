install:
	install -m 775 trackpoint.py /usr/lib/python3/dist-packages/trackpoint.py
	install -m 775 trackpoint-gtk.py /usr/bin/trackpoint-gtk
	install -m 644 trackpoint-autostart.desktop /etc/xdg/autostart/trackpoint-autostart.desktop
	install -m 644 trackpoint-gtk.desktop /usr/share/applications
	install -m 644 94-trackpoint.rules /etc/udev/rules.d/94-trackpoint.rules
	udevadm control --reload
	udevadm trigger
uninstall:
	rm /usr/lib/python3/dist-packages/trackpoint.py
	rm /usr/bin/trackpoint-gtk
	rm /etc/xdg/autostart/trackpoint-autostart.desktop
	rm /etc/udev/rules.d/94-trackpoint.rules
	rm trackpoint-gtk.desktop /usr/share/applications
