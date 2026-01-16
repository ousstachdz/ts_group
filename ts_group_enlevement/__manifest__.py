# -*- coding: utf-8 -*-
{
    'name': "TS Group ENLEVEMENT",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock',
                'product',
                'ts_group_process'
                ],

    # always loaded
    'data': [
        'reports/enlevement_report_template.xml',
        'reports/ir_actions_report.xml',
        'views/stock_picking.xml',
    ],

    'installable':True,
    'application':True,
    'auto_install':False,
    'sequence':-500,
    'license':'LGPL-3',
}
