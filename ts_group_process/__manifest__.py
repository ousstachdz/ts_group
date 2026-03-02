# -*- coding: utf-8 -*-
{
    'name': "TS Group Process",
    'author': "FINOUTSOURCE",
    'website': "http://www.finoutsource.dz",
    'category': 'custom',
    'version': '1.0',

    'depends': ['base','account', 'fleet', 'crm', 'product', 'sale', 'planning', 'project', 'purchase', 'mrp', 'purchase_request'],
    'data': [
        'data/mail_template.xml',

        'security/ir.model.access.csv',
        'security/security.xml',

        'reports/sale_order_report.xml',
        'reports/ir_actions_report.xml',
        'reports/invoice_report.xml',
        'reports/purchase_report.xml',
        'reports/pv_report.xml',

        'views/stock_picking_views.xml',
        'views/fleet_vehicle_views.xml',
        'views/mrp_production_views.xml',
        'views/crm_lead_views.xml',
        'views/account_move_views.xml',
        'views/product_views.xml',
        'views/planning_slot_views.xml',
        # 'views/report_invoice.xml',
        # 'views/report_purchase.xml',
        # 'views/report_sale.xml',
        # 'views/pv_traitement.xml',
        'views/res_company_views.xml',
        'views/res_users_views.xml',
        'views/project_task_views.xml',
        'views/sale_order_views.xml'
    ],
}
