#!/usr/bin/python2.7

import sys
import xmlrpclib
import ssl

username = ''
pwd = ''
dbname = ''

# Local
username_local = 'admin'
pwd_local = 'admin'
dbname_local = 'curso13'

gcontext = ssl._create_unverified_context()

# Remote connection
sock_common = xmlrpclib.ServerProxy('URL/xmlrpc/common',
                                    context=gcontext)

uid = sock_common.login(dbname, username, pwd)

sock = xmlrpclib.ServerProxy('URL/xmlrpc/object',
                             context=gcontext)

# Local connection
sock_common_local = xmlrpclib.ServerProxy('http://localhost:1369/xmlrpc/common',
                                    context=gcontext)

uid_local = sock_common_local.login(dbname_local, username_local, pwd_local)

sock_local = xmlrpclib.ServerProxy('http://localhost:1369/xmlrpc/object',
                             context=gcontext)

# Create Local Country
"""
vals = {
    'name': 'Mercedeslandia',
    'code': 'M2',
    'l10n_ar_afip_code': 999
}

return_id = sock_local.execute(dbname_local, uid_local, pwd_local, 'res.country',
                         'create', vals)
print return_id
"""

# Search Local Country
country_id = sock_local.execute(dbname_local, uid_local, pwd_local, 'res.country', 'search', [('name', '=', 'Mercedeslandia')])
country_data = sock_local.execute(dbname_local, uid_local, pwd_local, 'res.country', 'read', country_id, ['name','code','l10n_ar_afip_code'])

vals = {
    'name': country_data[0]['name'],
    'code': country_data[0]['code'],
    'l10n_ar_afip_code': country_data[0]['l10n_ar_afip_code']
}

# Remote Insert
return_id = sock.execute(dbname, uid, pwd, 'res.country', 'create', vals)
print return_id
