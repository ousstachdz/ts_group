from odoo import models, fields, api


class ProductCategory(models.Model):
    _inherit = 'product.category'

    is_tools = fields.Boolean(string='Is Tools')

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    
    @api.model_create_multi
    def create(self,vals_list):
        res = super().create(vals_list)
        for vals in vals_list:
            if 'categ_id' in vals:
                categ_id =  self.env['product.category'].browse(vals['categ_id'])
                if categ_id.is_tools:
                    self.env['resource.resource'].create({
                        'name': vals['name'],
                        'resource_type':'material',
                        # 'flexible_hours':True
                        })
        return res
    