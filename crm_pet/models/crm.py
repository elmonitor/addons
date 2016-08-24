# coding: utf-8

from openerp import api, fields, models
#from openerp.osv import fields, osv

class crm_pet(models.Model):
    _inherit = "crm.lead"

#Campos de la mascota

    nombre_pet = fields.Char('Nombre',required=True),
    contact_lastname = fields.Char('Apellido',required=True),
    peso_pet =  fields.Float('Peso en kg',required=True),
    sexo_pet = fields.Selection([('0.2', 'Macho'),('0.1', 'Hembra')],required=True)
    edad_pet = fields.Selection([('puppy','Puppy'),('junior','Junior'),('adult', 'Adult')]),
    tamano_pet = fields.Float('Tamaño',required=True,compute='TamanoPet'),
    #condicion_pet = fields.Float('Condición corporal',required=True,compute='CondicionPet'),
    #actividad_pet = fields.Float('Actividad Física',required=True,compute='ActividadPet'),
    raciones_pet = fields.Integer('Raciones por día',compute='RacionesPet'),

#Variables a calcular
    #valoracion = fields.Float('Valoración',compute='Valoracion'),
    #precio = fields.Float('Precio'),
    #paquetes = fields.Char('Paquetes'),
    #frecuencia = fields.Char('Frecuencia'),
    #ref_bolsa = fields.Char('Referencia'),
    
    RacionesPet()
    
#Cálculo número de raciones
    @api.depends('edad_pet')
    def RacionesPet(self):
        if self.edad_pet=='puppy':
            self.write({'raciones_pet':4})
        if self.edad_pet=='junior':
            self.write({'raciones_pet':3})
        if self.edad_pet=='adult':
            self.write({'raciones_pet':2})
    
