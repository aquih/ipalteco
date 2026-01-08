# -*- coding: utf-8 -*-

{
    'name': 'El Ipalteco',
    'version': '0.1',
    'category': 'Custom',
    'sequence': 6,
    'summary': 'El Ipalteco',
    'description': """ El Ipalteco """,
    'website': 'http://www.aquih.com',
    'author': 'aquíH',
    'depends': ['product', 'stock', 'account'],
    'data': [
        'security/ipalteco_security.xml',
        'views/product_template_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'assets': {
    },
}