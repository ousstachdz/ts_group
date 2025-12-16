
# -*- coding: utf-8 -*-



from odoo import api, fields, models, _, Command
class AccountMove(models.Model):
    _inherit = "account.move"
    posted_by = fields.Many2one('res.users', string='Confirmé Par')
    
    def action_post(self):
        self.posted_by = self.env.user.id
        return super(AccountMove, self).action_post()
    # def _get_name_invoice_report(self):
    #     """ This method need to be inherit by the localizations if they want to print a custom invoice report instead of
    #     the default one. For example please review the l10n_ar module """
    #     self.ensure_one()
    #     return 'abs_greenskay_process_nv_nv.new_report_invoice_document'