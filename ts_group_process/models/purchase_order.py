from odoo import models, fields, api


class purchase_order_inherit(models.Model):
    _inherit = 'purchase.order'

    tache_id_purchase = fields.Many2one('project.task')
