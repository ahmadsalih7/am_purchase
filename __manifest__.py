# -*- coding: utf-8 -*-
{
    'name': "am_purchase",
    'author': "Ahmed Salih",
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'mail',
                'my_account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menus_views.xml',
        'views/purchase_views.xml',
    ],

    'application': True
}
