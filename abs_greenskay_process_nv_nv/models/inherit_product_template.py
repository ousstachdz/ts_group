from odoo import models, fields, api




class ProductTemplate(models.Model):
    _inherit = 'product.template'

    
    @api.model_create_multi
    def create(self,vals):
        res = super().create(vals)
        for rec in vals: 
            categ = self.env['product.category'].browse(rec.get('categ_id',False)).name
            if categ == 'Outillage':
                self.env['resource.resource'].create({
                    'name': rec['name'],
                    'resource_type':'material',
                    'flexible_hours':True})
        return res
    