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

# Country Search
"""
countries_ids = sock.execute(dbname, uid, pwd, 'res.country',
                             'search', [])
for countries_id in countries_ids:
    country_data = sock.execute(dbname, uid, pwd,
                                  'res.country', 'read',
                                  countries_id, ['name'])
    print country_data[0]['name']
"""
"""
# Create Country
vals = {
    'name': 'Mercedeslandia'
}

return_id = sock.execute(dbname, uid, pwd, 'res.country', 'create', vals)
print return_id
"""

# Update Country
"""
vals = {
    'l10n_ar_afip_code': 999
}

return_id = sock.execute(dbname, uid, pwd, 'res.country', 'write', 253, vals)
print return_id

"""

# read new country
country_data = sock.execute(dbname, uid, pwd, 'res.country', 'read', 253,
                            ['name'])
print country_data[0]['name']

# delete new country
return_id = sock.execute(dbname, uid, pwd, 'res.country', 'unlink', 253)
print return_id
