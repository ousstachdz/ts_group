from odoo import api, models, fields, _

class PurchaseRequest(models.Model):
    _inherit = 'purchase.request'

    task_id = fields.Many2one('project.task')
