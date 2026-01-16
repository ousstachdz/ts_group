{
    "name": "Purchase Request",
    "author": "FINOUTSOUCE",
    "version": "1.0",
    "summary": "Use this module to have notification of requirements of "
    "materials and/or external services and keep track of such "
    "requirements.",
    "category": "Purchase Management",
    "depends": ["purchase_stock", "product"],
    "data": [
        "security/purchase_request.xml",
        "security/ir.model.access.csv",

        "data/purchase_request_sequence.xml",
        "data/purchase_request_data.xml",

        "reports/report_purchase_request.xml",
        "reports/ir_actions_report.xml",
        "wizard/purchase_request_line_make_purchase_order_view.xml",
        "views/purchase_request_view.xml",
        "views/purchase_request_line_view.xml",
        "views/product_template.xml",
        "views/purchase_order_view.xml",
        "views/stock_move_views.xml",
        "views/stock_picking_views.xml",
    ],

    "license": "LGPL-3",
    "installable": True,
    "application": True,
}
