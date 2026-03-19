This is source code from [official feetech repository](https://github.com/ftservo/FTServo_Python).

## Structure

```
root dirrectory
     |---lynode 
     |---lyttlsd
```
The 'lynode ' 'lyttlsd' directories contain examples of using the library.

The source code of the library is located in the `scservo_sdk` directory.

The 'lydevs_sdk' directory contains the original archive with the source code of the library from the developer.

## Usage

Tested on Linux Raspbian GNU/Linux 9.13 (stretch).
Python version Python 3.5.3

### Method 1. Clone repositry

```
$ cd /usr/src/
$ sudo git clone https://github.com/ftservo/FTServo_Python.git
$ sudo chown -R pi lygion_devs
$ cd lygion_devs_py/lynode
$ python3 ping.py
Succeeded to open the port
Succeeded to change the baudrate
[ID:001] ping Succeeded. lydevs model number : 
```

