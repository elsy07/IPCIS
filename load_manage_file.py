# -*- coding: utf-8 -*-
import pdb

pdb.set_trace()

def reload_master(filename):
    try:
        manageFile = open(filename,"r")
    except IOError:
        print "IP2manage_master dose not exits!"
    else:
        managelines = manageFile.readlines()
    finally:
        manageFile.close()
    return managelines

def list2dict(lines):
    keys = ['ip','country','region','city','ISP','UNIT','info']
    manageList = map(lambda l:dict(zip(keys,map(lambda var:var.strip(),l.split('|')))),lines[1:])
    return manageList
               
    
if "__name__" == "__main__":
    managelines = reload_master("IP2Manage_master_new")
    manageList = list2dict(managelines)
    print manageList[302]
