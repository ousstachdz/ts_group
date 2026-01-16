# -*- coding: utf-8 -*-
from odoo import models, fields, api


class stockpick(models.Model):
    _inherit = 'stock.picking'
    
    etat = fields.Selection( related="move_ids.etat", string="Etat")
    typologie = fields.Selection( related="move_ids.typologie", string="Typologie")
    observation = fields.Char( related="move_ids.observation", string="Observation")
