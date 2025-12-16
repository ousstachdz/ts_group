# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResUsers(models.Model):
    _inherit = 'res.company'
    
    signature_img = fields.Binary('Signature Image')