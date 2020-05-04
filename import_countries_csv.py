#!/usr/bin/python2.7

import sys
import xmlrpclib
import ssl
import csv

# Local
username_local = 'admin'
pwd_local = 'admin'
dbname_local = 'curso13'

gcontext = ssl._create_unverified_context()

# Local connection
sock_common_local = xmlrpclib.ServerProxy('http://localhost:1369/xmlrpc/common', context=gcontext)

uid_local = sock_common_local.login(dbname_local, username_local, pwd_local)

sock_local = xmlrpclib.ServerProxy('http://localhost:1369/xmlrpc/object', context=gcontext)

f = open('ejemplo_paises.csv','rt')
csv_reader = csv.DictReader(f, delimiter=',')

for i,line in enumerate(csv_reader):
    print i, line
    country_id = sock_local.execute(dbname_local, uid_local, pwd_local, 'res.country', 'search', [('name', '=', line['name'])])
    if country_id:
        print('Error ya existe el pais %s'%(line['name']))
        continue
    vals = {
        'name': line['name'],
        'code': line['code'],
        'l10n_ar_afip_code': line['l10n_ar_afip_code']
    }
    return_id = sock_local.execute(dbname_local, uid_local, pwd_local, 'res.country', 'create', vals)
    print return_id

f.close()
