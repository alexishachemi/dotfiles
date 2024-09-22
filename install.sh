#!/bin/bash

# dependency for the installer
echo checking python...
sudo apt install python3 -qq > /dev/null 2> /dev/null

echo running installer
python3 src/installer.py install && echo done
