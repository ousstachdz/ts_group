from odoo import api, models, fields, _ 

class inherit_planning_slot(models.Model):
    _inherit = 'planning.slot'

 
    resource_id = fields.Many2one(
        'resource.resource',
        'Resource',
        domain="[ '|', '&', ('vehicle_id', '=', False), ('vehicle_id.state_id.name', '=', 'En marche'), '|', ('company_id', '=', False), ('company_id', '=', company_id)]"
,
        group_expand='_group_expand_resource_id'
    )

    driver_id = fields.Many2one('res.partner', 'Conducteur')
    vehicle_id = fields.Many2one('fleet.vehicle', related='resource_id.vehicle_id')
    stock_picking_id = fields.Many2one('stock.picking', 'Chargement')

    @api.model_create_multi
    def create(self,vals):
        res = super().create(vals)
        for rec in res: 
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


    @api.model
    def _read_group_stage_ids(self, stages, domain):
        # retrieve job_id from the context and write the domain: ids + contextual columns (job or default)
        job_id = self.env.context.get('default_job_id')
        search_domain = [('job_ids', '=', False)]
        if job_id:
            search_domain = ['|', ('job_ids', '=', job_id)] + search_domain
        if stages:
            search_domain = ['|', ('id', 'in', stages.ids)] + search_domain

        stage_ids = stages.sudo()._search(search_domain, order=stages._order)
        return stages.browse(stage_ids)