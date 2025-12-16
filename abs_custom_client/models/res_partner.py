# -*- coding: utf-8 -*-
from odoo import models, fields, api


class respartner(models.Model):
    _inherit = 'res.partner'
    
    street = fields.Char()
    city = fields.Char()
    nis = fields.Char(string='NIS')
    rc = fields.Char(string='RC')
    ai = fields.Char(string='AI')
    nif = fields.Char(string='NIF')
    rib = fields.Char(string='RIB')
    compte = fields.Char(string='Compte')
    contacts = fields.One2many(related='child_ids',)
    type_client = fields.Selection(
        [('public', 'Secteur public'),
         ('prive', 'Secteur privé')], string='Type client', store='true')
