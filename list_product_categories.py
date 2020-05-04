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

product_categories_ids = sock.execute(dbname, uid, pwd, 'product.category',
                                      'search', [])
for product_categories_id in product_categories_ids:
    product_categories_data = sock.execute(dbname, uid, pwd,
                                           'product.category', 'read',
                                           product_categories_id, ['name'])
    print product_categories_data[0]['name']
