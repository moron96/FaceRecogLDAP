import string
import datetime
from ldap3 import Connection, Server, SIMPLE, SYNC, LEVEL, SUBTREE, ALL, MODIFY_REPLACE
import os,sys,inspect
import pathlib

now = datetime.datetime.now()
curdate = str(now.day) + '-' + str(now.month) + '-' + str(now.year)

LDAPaddr = '192.168.0.22'
LDAPdomain = 'dc=ibm-jti,dc=com'
LDAPou = 'ou=JTIUsers'
LDAPPWD = 'pw'
LDAPUID = 'id'

def createldapconnection():
    ldapserver = Server(LDAPaddr, get_info=ALL)
    ldapconn = Connection(ldapserver, user='cn='+LDAPUID+','+LDAPdomain,password=LDAPPWD, auto_bind=True) #testing, pw asli d3w419
    return ldapconn

def addattribute(dictionary,attrName,data):
    if data != '':
        dictionary[attrName] = data

#----------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    log_folder = currentdir + "/" + "logs"
    
    os.makedirs(log_folder, exist_ok=True) 
    print("start", file=open(log_folder+"/"+curdate+"fetchPhoto.txt", "w"))

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ldapconn = createldapconnection()
    for c in alphabet:
        ldapconn.search(search_base=LDAPou+","+LDAPdomain, search_filter="(cn="+c+"*)", search_scope=SUBTREE, attributes=['*'])
        for entry in ldapconn.response:
            entity = entry['attributes']

            if "jpegPhoto" in entity:
                currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
                image_folder = currentdir + "/" + "images"
                
                os.makedirs(image_folder, exist_ok=True) 
                with open(image_folder+"/"+entity['displayName'] + ".jpg", 'wb') as f:
                    f.write(entity['jpegPhoto'][0])
