# -*- coding: utf-8 -*-
# © 2016 3nodus SAS
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from openerp import api, models, fields


class ResPet(models.Model):
    _name = 'res_pet'
    
    name = fields.Char(string='Name',required=True)
    weight = fields.Float(string = 'Weight')
    genre = fields.Selection([(('m','Male'),('f','Female')])
    size = fields.Selection([('mi','Mini'),('sm','Small'),('me','Medium'),('bi','Big'),('en','Enormeus')])
    condition = fields.Selection([('sk','Skinny'),('th','Thin'),('n''Normal'),('f','Fat'),('vf','Very Fat')])
    activity = fields.Selection([('ms','Muy sedentario'),('s','Sedentario'),('n','Normal'),('a','Activo'),('ma','Muy activo')])
    category = fields.Selection([('pe','Perro'),('ga','Gato'),('pa','Pájaro'),('ca','Caballo'),('co','Conejo')])
    breed = fields.Char(string = 'Breed')
    age = fields.Integer(string = 'Age in monts')
    parent = fields.Many2one('res.partner')
    photo = fields.Binary()
    

