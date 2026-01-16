from odoo import models, fields, api, _


class stock_picking_inherit(models.Model):
    _inherit = 'stock.picking'

    tache_id_chargement = fields.Many2one('project.task')

    vehicle_count = fields.Integer(
        compute='_compute_vehicle', string="Vehicle Count")

    vehicle_ids = fields.One2many(
        'fleet.vehicle.assignation.log', compute='_compute_vehicle_ids', string="Vehicle")

    def _compute_vehicle_ids(self):
        for rec in self:
            resource_ids = self.env['planning.slot'].search(
                [('stock_picking_id', '=', rec.id)]).mapped('resource_id.vehicle_id').ids

            rec.vehicle_ids = self.env['fleet.vehicle.assignation.log'].search(
                [('vehicle_id', 'in', resource_ids)])

    def _compute_vehicle(self):
        for rec in self:
            # rec.chargement_count = rec.env['stock.picking'].search_count(['tache_id_chargement', '=', rec.id])
            # rec.vehicle_count = rec.env['fleet.vehicle.log.services'].search_count([('origin', '=', rec.origin)])
            resource_ids = self.env['planning.slot'].search(
                [('stock_picking_id', '=', self.id)]).mapped('resource_id.vehicle_id').ids

            rec.vehicle_count = self.env['fleet.vehicle.assignation.log'].search_count(
                [('vehicle_id', 'in', resource_ids)])

    def action_vehicle(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Transport',
            'res_model': 'fleet.vehicle.assignation.log',
            'domain': [('vehicle_id', 'in', self.env['planning.slot'].search([('stock_picking_id', '=', self.id)]).mapped('resource_id.vehicle_id').ids)],
            'view_mode': 'tree,form',
            'target': 'current',
        }

    def action_CreateVehicle(self):

        action = {
            'type': 'ir.actions.act_window',
            'view_mode': 'gantt',
            'res_model': 'planning.slot',
            'view_id': False,
            'target': 'current',
            "name": _("Créer Service Transport"),
            'context': {'search_default_group_by_resource': True, 'default_stock_picking_id': self.id},
        }

        return action
