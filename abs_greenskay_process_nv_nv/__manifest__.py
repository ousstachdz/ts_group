# -*- coding: utf-8 -*-
{
    'name': "greenskay_process",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "FINOUTSOURCE",
    'website': "http://www.finoutsource.dz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'custom',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale', 'project','sale_project','account','purchase','stock',"mrp", 'fleet'],
    
    # always loaded
    'data': [
        'data/task_mail_template.xml',
        'security/ir.model.access.csv',
        'views/stock.view_picking_inherit_forme.xml',
        'views/task_inherit_form.xml',
        'views/vehicle_services_form_inherit.xml',
        'views/view_fabrication.xml',
        'views/crm_lead_views.xml',
        'views/account_move_views.xml',
        'views/planning_slot_views.xml',
        'views/report_invoice.xml',
        'views/report_purchase.xml',
        'views/report_sale.xml',
        'views/pv_traitement.xml',
        'views/res_company_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'pre_init_hook': 'nv_nv_pre_init',
}
