# -*- coding: utf-8 -*-

# Resource object code
#
# Created by: The Resource Compiler for PyQt5 (Qt v5.15.2)
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore

qt_resource_data = b"\
\x00\x00\x01\x29\
\x00\
\x00\x0e\xdd\x78\x9c\xeb\x0c\xf0\x73\xe7\xe5\x92\xe2\x62\x60\x60\
\xe0\xf5\xf4\x70\x09\x62\x60\x60\x69\x60\x60\x60\xea\xe0\x60\x02\
\x8a\xb4\x7b\x8a\x45\x01\x29\xc6\xe2\x20\x77\x27\x86\x75\xe7\x64\
\x5e\x02\x39\x2c\xe9\x8e\xbe\x8e\x0c\x0c\x1b\xfb\xb9\xff\x24\xb2\
\x02\xf9\x9c\x05\x1e\x91\xc5\x0c\x0c\x42\x25\x20\xcc\x78\x2f\x4d\
\xbe\x82\x81\x81\xaf\xc8\xd3\xc5\x31\xa4\x22\xee\xed\xf5\x8d\xbd\
\x87\x19\x78\x0e\x1c\x78\x63\xef\xb6\xec\xb4\xd8\x3f\xb7\xa9\x59\
\x8d\x06\x1f\xca\x1f\x08\xfd\xb1\x01\xea\x54\xe1\x91\x60\x60\x70\
\x38\xd2\xc0\xc8\xc0\xe0\x32\xca\x1c\x65\x0e\x76\xe6\x13\x51\xe6\
\x6f\x3f\xff\xa9\x78\x4e\x52\x79\x69\x7b\x76\x75\x8c\x71\xc2\x24\
\x20\x7b\xcb\xec\xf0\x9d\x69\x07\x40\x82\x99\xe6\xeb\x8b\xce\x36\
\x00\x19\x9e\x97\xf2\xe2\x9e\xce\x62\x9c\x0c\x14\x5c\x72\x77\xcf\
\x29\x53\x66\x35\x90\xe0\xee\xca\xa9\xd9\x6c\x3e\x20\x2d\x65\x9f\
\xb5\xae\xf3\xcc\x00\x69\x79\xfb\x2c\x74\x9d\xa4\x01\x48\xf6\x16\
\xfd\x0d\xbc\xa5\xcd\xc6\xc3\xc0\xf0\xc0\xde\x20\x01\x98\x17\x05\
\x99\xd9\x18\x18\x04\x0c\x47\x99\xa3\xcc\x51\xe6\x28\x73\x94\x39\
\xca\x1c\x65\x8e\x32\x47\x99\xa3\xcc\x21\xc0\xec\x7c\xfe\x93\xd9\
\x63\xeb\xc2\x98\xfd\x62\x6d\x71\x40\x2e\x83\xa7\xab\x9f\xcb\x3a\
\xa7\x84\x26\x00\xc4\x16\xba\x7d\
"

qt_resource_name = b"\
\x00\x0a\
\x07\x85\x49\x33\
\x00\x6e\
\x00\x65\x00\x77\x00\x50\x00\x72\x00\x65\x00\x66\x00\x69\x00\x78\x00\x33\
\x00\x08\
\x07\x98\x59\x07\
\x00\x6c\
\x00\x61\x00\x63\x00\x65\x00\x2e\x00\x70\x00\x6e\x00\x67\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x1a\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x1a\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x86\x30\x2b\xcd\x36\
"

qt_version = [int(v) for v in QtCore.qVersion().split('.')]
if qt_version < [5, 8, 0]:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
