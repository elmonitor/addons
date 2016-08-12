# -*- coding: utf-8 -*-
# © 2016 3nodus SAS
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from openerp import api, models, fields


class ResPet(models.Model):
    _name = 'res_pet'
    
    name = fields.Char(string='Name',required=True)
    weight = fields.Float(string = 'Weight')
    genre = fields.Selection([('Male', 'Female')])
    size = fields.Selection([('Mini','Small','Medium','Big','Enormeus')])
    condition = fields.Selection([('Skinny','Thin','Normal','Fat','Very Fat')])
    activity = fields.Selection([('Muy sedentario','Sedentario','Normal','Activo','Muy activo')])
    category = fields.Selection([('Perro','Gato','Pájaro','Caballo','Conejo')])
    breed = fields.Char(string = 'Breed')
    age = fields.Integer(string = 'Age')
    parent = fields.Many2one('res.partner')
    photo = fields.Binary()
