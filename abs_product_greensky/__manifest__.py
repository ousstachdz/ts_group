# -*- coding: utf-8 -*-
{
    'name': "Product_grensky",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Manel Bougamra",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','hr_contract','mrp','stock','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_greensky.xml',
        # 'views/pricelist.xml',
    ],
}
