import os
from datetime import datetime

from pdflink import PdfLink

from helpers import *

def p(filename):
    return "%s/%s" % (cachedir, filename)


def synchronize():
    ret = []
    rootdir = os.path.abspath(os.path.join(os.getcwd(), cachedir))

    if not os.path.exists(rootdir):
        os.mkdir(rootdir)

    for section in conf.sections():
        try:
            if section != "General":
                dir = conf.get(section, "dir")
                fulldir = os.path.join(rootdir, dir)

                if os.path.exists(fulldir):
                    os.chdir(fulldir)
                    sp("git pull")
                else:
                    os.chdir(rootdir)
                    sp("git clone %s" % conf.get(section, "url"))

                pdfdir = os.path.join(fulldir, conf.get(section, "pdfs"))
                for file in os.listdir(pdfdir):
                    if file.endswith("pdf") or file.endswith("PDF"):
                        abs_filename = os.path.join(pdfdir, file)
                        timestamp = datetime.fromtimestamp(os.path.getmtime(abs_filename))
                        pdf = PdfLink(file, section, timestamp, abs_filename)
                        ret.append(pdf)
                        print("found %s" % pdf)

        except Exception as e:
            print("Error while reading section %s: %s" % (section, str(e)))

    return ret

