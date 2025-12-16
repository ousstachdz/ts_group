# -*- coding: utf-8 -*-
from odoo import models, fields, api


class stockpick(models.Model):
    _inherit = 'stock.move'
    
    etat = fields.Selection(
        [('S', 'S'),
         ('G', 'G'),
         ('L', 'L'),
        ], string='Etat', store='true')#, required=True,)
    typologie = fields.Selection(
        [('DMA', 'DMA'),
         ('DS', 'DS'),
         ('DSD', 'DSD'),
         ('I', 'I'),
         ], string='Typologie de déchets', store='true')#, required=True,)
    observation = fields.Char(string='Observation', store='true',)


    def _merge_moves_fields(self):
        """ This method will return a dict of stock move’s values that represent the values of all moves in `self` merged. """
        state = self._get_relevant_state_among_moves()
        origin = '/'.join(set(self.filtered(lambda m: m.origin).mapped('origin')))
        return {
            'product_uom_qty':self[0].product_qty,
            'date': min(self.mapped('date')) if all(p.move_type == 'direct' for p in self.picking_id) else max(self.mapped('date')),
            'move_dest_ids': [(4, m.id) for m in self.mapped('move_dest_ids')],
            'move_orig_ids': [(4, m.id) for m in self.mapped('move_orig_ids')],
            'state': state,
            'origin': origin,
        }