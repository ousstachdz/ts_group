# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.tools import float_round

class grn_product(models.Model):
    _inherit = "product.template"

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