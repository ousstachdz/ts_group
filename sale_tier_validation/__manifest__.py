{
    "name": "Sale Tier Validation",
    "summary": "Extends the functionality of Sale Orders to "
    "support a tier validation process.",
    "version": "1.0",
    "category": "Sale",
    "author": "FINOUTSOURCE",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["sale", "base_tier_validation"],
    "data": [
        "data/mail_data.xml", 
        "views/sale_order_view.xml"
    ],
}
