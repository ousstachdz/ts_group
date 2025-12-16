# -*- coding: utf-8 -*-
{
    'name': "GREENSKY ENLEVEMENT",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock',
                'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'reports/enlevement_report_button.xml',
        'reports/enlevement_report_template.xml',
        'views/stock_picking.xml',
    ],

    'installable':True,
    'application':True,
    'auto_install':False,
    'sequence':-500,
    'license':'LGPL-3',
}
