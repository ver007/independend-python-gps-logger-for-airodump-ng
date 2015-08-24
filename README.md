## GPS logger tool for airodump-ng client data (CSV)
这Python脚本被记录的时间每一秒以及来自GPSD GPS位置。输出文件可以用来跟踪您的上网IP，或确定GPS位置
对“airodump中-NG”CSV文件无线客户端设备。
 坦率地说这是一个简单的通用产品安全指令为TXT文件记录器。
This Python script is logging each second of time along with GPS position from GPSD. Later to be used to determine the GPS position of Wifi Client devices against airodump-ng CSV file.

###Usage:
Simply run the ./log_position.py

![alt tag](https://raw.githubusercontent.com/ggtd/independend-python-gps-logger-for-airodump-ng/master/screen2.png)

The logfile is writen into ./gps_log_file
Log file is a TXT file. One line is representing one second in time and GPS.latitude + GPS.longitude.

NOTE: Time in log-file is local device time, (not GPS-time). To match other data time source on local system.


Have fun!


