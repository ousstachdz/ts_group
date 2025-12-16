from odoo import models, fields, api
from datetime import datetime

class inherit_resource_resource(models.Model):
    _inherit = 'resource.resource'

    vehicle_id = fields.Many2one('fleet.vehicle')
    


class inherit_planning_slot(models.Model):
    _inherit = 'planning.slot'

 
    resource_id = fields.Many2one(
        'resource.resource',
        'Resource',
        domain="[ '|', '&', ('vehicle_id', '=', False), ('vehicle_id.state_id.name', '=', 'En marche'), '|', ('company_id', '=', False), ('company_id', '=', company_id)]"
,
        group_expand='_read_group_resource_id'
    )

    driver_id = fields.Many2one('res.partner', 'Conducteur')
    vehicle_id = fields.Many2one('fleet.vehicle', related='resource_id.vehicle_id')
    stock_picking_id = fields.Many2one('stock.picking', 'Chargement')

    @api.model_create_multi
    def create(self,vals):
        res = super().create(vals)
        for rec in res: 
            # resource  = self.env['resource.resource'].browse(rec['resource_id'])
            resource  = rec.resource_id
            if resource.vehicle_id:
                history_vals =  {
                    'date_start' : rec.start_datetime,
                    'date_end' : rec.end_datetime,
                    'vehicle_id': resource.vehicle_id.id,
                    'driver_id' : rec.driver_id.id
                }
                self.env['fleet.vehicle.assignation.log'].create(history_vals)
        return res