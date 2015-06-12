import sys
reload(sys)
sys.setdefaultencoding('utf8')


from load_manage_file import reload_master,list2dict
from IPFormat import countip

def count_ip(managelist):
    iplist = []
    for l in managelist:
        iplist.append(l['ip'])
    print iplist[0]
    print iplist[-1]
    return countip(iplist)


    
managelines = reload_master("IP2Manage_master")
managelist = list2dict(managelines)
count = count_ip(managelist)
countA = float(count)/2**24

print count
print countA