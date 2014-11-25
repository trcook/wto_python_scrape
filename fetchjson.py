#! usr/bin/env python 

# The file that produces the table with the listing of cases is referenced as a javascript file, but it's basically a json array: it's located at: http://wto.org/library/disputes/dispute_arrays_e.js


# First we get the files
os.system("scrapy fetch 'http://wto.org/library/disputes/dispute_arrays_e.js'>>disputes.js")

# now we process them through node into json. This will allow for easier reading later on.
os.system("node js_to_json.js disputes.js")

