from odoo import models, fields, api
from datetime import datetime

class inherit_resource_resource(models.Model):
    _inherit = 'resource.resource'

    vehicle_id = fields.Many2one('fleet.vehicle')