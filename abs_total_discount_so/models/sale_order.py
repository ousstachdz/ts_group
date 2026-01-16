from odoo import api,fields,models,_

#inherit SaleOrder class.
class SaleOrder(models.Model):
    _inherit = "sale.order"

    discount_total = fields.Monetary("Remise globale",compute='total_discount')

    #Count for total discount
    @api.depends('order_line.product_uom_qty','order_line.price_unit','order_line.discount')
    def total_discount(self):
        self.discount_total=0.0
        for sale_order_line_id in self.order_line:
            sale_order_line_qty_price = sale_order_line_id.product_uom_qty * sale_order_line_id.price_unit
            sale_order_line_discount = sale_order_line_qty_price*(sale_order_line_id.discount /100)
            self.discount_total = sale_order_line_discount + self.discount_total


