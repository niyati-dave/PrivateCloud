#!/usr/bin/env python
from fabric.api import *

def grubupdate():
        sudo("sed -i 's/\#GRUB_HIDDEN_TIMEOUT\=0/GRUB_HIDDEN_TIMEOUT\=10/g' /etc/default/grub")
        sudo("sed -i 's/\#GRUB_TIMEOUT\=0/GRUB_TIMEOUT\=10/g' /etc/default/grub")
        sudo("update-grub")
        sudo("cat /etc/default/grub | grep -i GRUB_HIDDEN_TIMEOUT")
        sudo("cat /etc/default/grub | grep -i GRUB_TIMEOUT")

def passage():
    sudo("sudo chage -M -1 ubuntu")
    sudo("sudo chage -M -1 root")
    sudo("sed -i 's/PASS_MAX_DAYS\t99999/PASS_MAX_DAYS\t-1/g' /etc/login.defs")
#   sudo("sed -i 's/PASS_MAX_DAYS   99999/PASS_MAX_DAYS   -1/g' /etc/login.defs")    
#    sudo("sed -i 's/PASS_MAX_DAYS  45/PASS_MAX_DAYS   -1/g' /etc/login.defs")
    sudo("cat /etc/login.defs | grep -i PASS_MAX_DAYS")     
def telnetdremove():
    sudo("sudo dpkg --get-selections  | grep -v deinstall | grep telnetd | awk {'print $NF'} > out1")
    sudo ("if [[ -s /home/ubuntu/out1 ]]; then sudo apt-get remove telnetd -y; fi ")
 
