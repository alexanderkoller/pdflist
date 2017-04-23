import os
import subprocess
import configparser
import time


conf = configparser.ConfigParser()
conf.read("pdflist.conf")

cachedir = conf.get("General", "cachedir", default="cache")


def sp(command):
    #print("execute '%s' in %s" % (command, os.getcwd()))
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()


def spns(command):
    parts = command.split()
    process = subprocess.Popen(parts, stdout=subprocess.PIPE,
    stdin=subprocess.PIPE)

    second_command = conf.get("General", "second_command")

    if second_command:
        time.sleep(1)
        p2 = subprocess.Popen(second_command, shell=True)
    
    process.wait()
