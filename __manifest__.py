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
        'security/purchase_security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'security/res_config_settings_views.xml',
        'views/purchase_views.xml',
        'views/menus_views.xml',
    ],

    'application': True
}
