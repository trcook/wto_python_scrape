#! usr/bin/env python 

# The file that produces the table with the listing of cases is referenced as a javascript file, but it's basically a json array: it's located at: http://wto.org/library/disputes/dispute_arrays_e.js
import os
import json
import csv
from collections import OrderedDict

def fetch_disputes():
    os.system("scrapy fetch 'http://wto.org/library/disputes/dispute_arrays_e.js'>>disputes.js")
    #: First we get the files
    # now we process them through node into json. This will allow for easier reading later on:
    os.system("node js_to_json.js disputes.js")
    os.system("rm disputes.js")
    input=json.load(file("disputes.json"))
    # First record is empty, so we remove it:
    input.pop(0)
    f=open("disputes.json","w")
    f.write(json.JSONEncoder().encode(input))
    return input



def get_third_parties(obj):
    out=[]
    for i in obj[0:len(obj)]:
        print "dispute number %(num)s, third parties: %(party)s" % {"num":i.get('code'),"party":i.get('third_party')}
        out.append(OrderedDict(
                [("dispute",i.get('code')),("third_parties",i.get('third_party'))]
                ))
    return out



def write_third_parties(obj,filename):
    csvfile=open(filename,'w')
    writer=csv.DictWriter(csvfile,fieldnames=obj[1].keys())    
    writer.writeheader()
    writer.writerows(obj)
    csvfile.close()

write_third_parties(get_third_parties(fetch_disputes()),"output.csv")


