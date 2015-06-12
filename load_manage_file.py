# -*- coding: utf-8 -*-


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
    managelist = map(lambda l:dict(zip(keys,map(lambda var:var.strip(),l.split('|')))),lines)
    return managelist
               

