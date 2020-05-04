#!/usr/bin/python2.7

import sys
import xmlrpclib
import ssl

username = ''
pwd = ''
dbname = ''

gcontext = ssl._create_unverified_context()

sock_common = xmlrpclib.ServerProxy('URL/xmlrpc/common',
                                    context=gcontext)

uid = sock_common.login(dbname, username, pwd)

sock = xmlrpclib.ServerProxy('URL/xmlrpc/object',
                             context=gcontext)

bank_ids = sock.execute(dbname, uid, pwd, 'res.bank', 'search', [])
for bank_id in bank_ids:
    bank_data = sock.execute(dbname, uid, pwd, 'res.bank', 'read', bank_id, ['name'])
    print bank_data[0]['name']
