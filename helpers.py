import os
import subprocess
import configparser


conf = configparser.ConfigParser()
conf.read("pdflist.conf")

cachedir = conf.get("General", "cachedir", default="cache")


def sp(command):
    print("execute '%s' in %s" % (command, os.getcwd()))
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()


