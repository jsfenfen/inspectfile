class row(object):
    """ a class to represent a single row. Assumes the header has already been cleaned up according to the output style we're using"""
    def __init__(self, rowheader):
        self.header = rowheader
        self.nulls = 0
        self.ints = 0
        self.floats = 0
        self.strings = 0
        self.dates = 0
        self.maxlength = 0
        self.hasnulls = False
        self.totalcells = 0
        
        
    def set_header(self, newheader):
        self.header = newheader
    
    def print_sql(self):
        outstanding_rows = self.totalcells-self.nulls


        if (outstanding_rows - self.ints == 0):
            return("\t\"%s\" int" % (self.header))
        elif (outstanding_rows - self.floats == 0):
            return("\t\"%s\" float" % (self.header))    


        else:
            if self.maxlength < 8:
                return("\t\"%s\" char(%s)" % (self.header, self.maxlength))
            else:
                return("\t\"%s\" varchar(%s)" % (self.header, self.maxlength))
        
    

