from odoo import models, fields, api


class fleet_services_inherit(models.Model):
    _inherit = 'fleet.vehicle.log.services'

    stock_move_vehicle = fields.Many2one('stock.picking')
    origin = fields.Char('Document origine')


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    
    @api.model_create_multi
    def create(self,vals):
        res = super().create(vals)
        self.env['resource.resource'].create({
            'name': res.name.replace('/Pas de plaque',''),
            'vehicle_id':res.id,
            'resource_type':'material',
            'flexible_hours':True})
        return res
    