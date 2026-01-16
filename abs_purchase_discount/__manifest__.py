{
    'name': 'Purchase order lines with discounts',
    'version': '1.0',
    'category': 'Purchase Management',
    'author': 'FINOUTSOURCE',
    'license': 'LGPL-3',
    'depends': [
        'stock', 'purchase'
    ],
   
    'data': [
        'views/purchase_discount_view.xml',
        'views/product_supplierinfo_view.xml',
        'views/res_partner_view.xml',
        'views/report_purchaseorder.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
