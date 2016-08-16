# -*- coding: utf-8 -*-
# © 2016 3nodus SAS
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from openerp import api, models, fields


class ResPet(models.Model):
    _name = 'res_pet'
    
    name = fields.Char(string='Name',required=True)
    weight = fields.Float(string = 'Weight')
    genre = fields.Selection([('Male', 'Female')], required=True)
    size = fields.Selection([('Mini','Small','Medium','Big','Enormeus')],required=True)
    condition = fields.Selection([('Skinny','Thin','Normal','Fat','Very Fat')],required=True)
    activity = fields.Selection([('Muy sedentario','Sedentario','Normal','Activo','Muy activo')],required=True)
    category = fields.Selection([('Perro','Gato','Pájaro','Caballo','Conejo')])
    breed = fields.Char(string = 'Breed')
    age = fields.Integer(string = 'Age in monts')
    parent = fields.Many2one('res.partner')
    photo = fields.Binary()
    

