{
    "name": "Purchase Request Tier Validation",
    "summary": "Extends the functionality of Purchase Requests to "
    "support a tier validation process.",
    "version": "1.0",
    "category": "Purchase Management",
    "author": "FINOUTSOURCE",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["purchase_request", "base_tier_validation"],
    "data": [
        "data/purchase_request_tier_definition.xml",
        "views/purchase_request_view.xml",
    ],
}
