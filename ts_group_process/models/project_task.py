from odoo import models, fields, api


class project_task_inherit(models.Model):
    _inherit = 'project.task'

    purchase_order_count = fields.Integer(compute='_compute_purchase_count', string="Puchase Count")
    chargement_count = fields.Integer(compute='_compute_chargement', string="Chargement Count")
    of_count = fields.Integer(compute='_compute_of', string="Manufacturing  order Count")


    #### COMPUTE FUNCTIONS ####
    def _compute_purchase_count(self):
        for rec in self:
            rec.purchase_order_count = rec.env['purchase.order'].search_count([('origin', '=', rec.project_id.name)])
            print(rec.purchase_order_count)
            # rec.purchase_order_count = 0

    
    def _compute_chargement(self):
        for rec in self:
            rec.chargement_count = rec.env['stock.picking'].search_count([('origin', '=', rec.project_id.name)])
    
    def _compute_of(self):
        for rec in self:
            rec.of_count = rec.env['mrp.production'].search_count([('origin', '=', rec.project_id.name)])

    #### ACTION FUNCTIONS ####
    def action_chargement(self):

        return {
            'type': 'ir.actions.act_window',
            'name': 'Chargement',
            'res_model': 'stock.picking',
            'domain': [('origin', '=', self.project_id.name)],
            'view_mode': 'tree,form',
            'target': 'current',
        }
    def action_purchase(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Achats',
            'res_model': 'purchase.order',
            'domain': [('origin', '=', self.project_id.name)],
            'view_mode': 'tree,form',
            'target': 'current',
        }

    def action_CreateAchat(self):
        for record in self:
            record.env['purchase.order'].create({
                'partner_id': record.partner_id.id,
                'origin': record.project_id.name,
            })

    def action_CreateChargement(self):
        for record in self:
            lead_lines = record.sale_order_id.opportunity_id.lead_line_ids
            q = record.env['stock.picking'].search([('origin', '=', record.project_id.name)])
            record.env['stock.picking'].create({
                'partner_id': record.partner_id.id,
                'picking_type_id': 1,
                'location_id': 4,
                'location_dest_id': 8,
                'origin': record.project_id.name,
                'move_ids': [(0, 0, {
        'product_id': line.product_id.id,
        'product_uom':  line.product_id.uom_id.id,
        'product_uom_qty': line.product_qty,
        'location_id': 4,  
        'location_dest_id': 8,
        'name': f"Move for {line.product_id.name}",
    

                }) for line in lead_lines]
            })
        
    def action_of(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Traitement',
            'res_model': 'mrp.production',
            'domain': [('origin', '=', self.project_id.name)],
            'view_mode': 'tree,form',
            'target': 'current',
        }

    def action_Reapprovisionner(self):
        return {
            'name': 'Réapprovisionner le sous-traitant',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'stock.picking',
            'target': 'current',
            'context': {
                'default_picking_type_id': self.env['stock.picking.type'].search(
                    [('company_id','=',self.sale_order_id.company_id.id),('name','=','Réapprovisionner le sous-traitant')]).id
            }
            
        }
