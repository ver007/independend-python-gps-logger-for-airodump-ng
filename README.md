## GPS logger tool for airodump-ng client data (CSV)

This Python script is logging each second of time along with GPS position from GPSD. Later to be used to determine the GPS position of Wifi Client devices against airodump-ng CSV file.

###Usage:
Simply run the ./log_position.py

The logfile is writen into ./gps_log_file
Log file is a TXT file. One line is representing one second in time and GPS.latitude + GPS.longitude.

Have fun!


