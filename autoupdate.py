#!/usr/bin/env python3
import os

# simpel program to autoupdate system, scheduled in a cron job
def run_update():
    os.system("sudo apt-get update")
    os.system("sudo apt-get dist-upgrade -y")    
    os.system("sudo apt-get autoremove -y")    
    os.system("sudo apt-get autoclean -y")    

run_update()
