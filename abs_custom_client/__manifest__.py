# -*- coding: utf-8 -*-
{
    'name': "CUSTOM CLIENT",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'account',
                'product',
                'bus'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_partner.xml',
        #'views/res_company.xml',
    ],

    'installable':True,
    'application':True,
    'auto_install':False,
    'sequence':-500,
    'license':'LGPL-3',
}
