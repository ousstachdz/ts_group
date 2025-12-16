from odoo import models, fields, api


class manufactering_order_inherit(models.Model):
    _inherit = 'mrp.production'
    tache_id_of = fields.Many2one('project.task')
