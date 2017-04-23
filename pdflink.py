
class PdfLink:
    def __init__(self, name, project, date, abs_filename):
        self.name = name
        self.project = project
        self.date = date
        self.abs_filename = abs_filename

    def sdate(self):
        return self.date.strftime("%Y-%m-%d %H:%M")

    def __str__(self):
        return "%s [%s]: mtime=%s, abs_filename=%s" % (self.name, self.project, self.date.strftime("%Y-%m-%d %H:%M:%S"), self.abs_filename)
