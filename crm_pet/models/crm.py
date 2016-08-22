# coding: utf-8

from openerp import api, fields, models
#from openerp.osv import fields, osv

class crm_pet(models.Model):
    _inherit = "crm.lead"

#Campos de la mascota

    nombre_pet = fields.Char('Nombre',required=True),
    contact_lastname = fields.Char('Apellido',required=True),
    peso_pet =  fields.Float('Peso en kg',required=True),
    sexo_pet = fields.Float([('0.2', 'Macho'),('0.1', 'Hembra')],required=True)
    edad_pet = fields.Selection([('puppy','Puppy),('junior','Junior'),('adult', 'Adult')], required=True),
    tamano_pet = fields.Float('Tamaño',required=True,compute='TamanoPet'),
    condicion_pet = fields.Float('Condición corporal',required=True,compute='CondicionPet'),
    actividad_pet = fields.Float('Actividad Física',required=True,compute='ActividadPet'),
    raciones_pet = fields.Integer('Raciones por día',compute='RacionesPet',required=True),

#Variables a calcular
    valoracion = fields.Float('Valoración'),
    precio = fields.Float('Precio'),
    paquetes = fields.Char('Paquetes'),
    frecuencia = fields.Char('Frecuencia'),
    ref_bolsa = fields.Char('Referencia'),
    
#Cálculo número de raciones
    @api.depends('edad_pet')
    def RacionesPet(self):
        if self.edad_pet=='puppy':
            self.write({'raciones_pet':4})
        if self.edad_pet=='junior':
            self.write({'raciones_pet':3})
        if self.edad_pet=='adult':
            self.write({'raciones_pet':2})
    
#Calcular condición y tamaño
    @api.depends('edad_pet')
    def CondicionPet('self'):
        
        if self.edad_pet=='puppy':
            if self.condicion_pet=="muydelgado":
                self.write({'_condicion':0.4})
            elif self.condicion_pet=="delgado":
                self.write({'_condicion':0.2})
            elif self.condicion_pet=="optimo":
                self.write({'_condicion':0.0})
            elif self.condicion_pet=="sobrepeso":
                self.write({'_condicion':-0.2})
            elif self.condicion_pet=="obeso":
                self.write({'_condicion':-0.4})
                
            if (self.peso_pet>=0.35 and self.peso_pet<=2.1):
                self.write({'tamano_pet':"miniatura"})
                self.write({'_tamano':9})
            elif (self.peso_pet>2.1 and self.peso_pet<=5.2):
                self.write({'tamano_pet':"pequeno"})
                self.write({'_tamano':8})
            elif (self.peso_pet>5.2 and self.peso_pet<=8.5):
                self.write({'tamano_pet':"mediano"})
                self.write({'_tamano':7})
            elif (self.peso_pet>8.5 and self.peso_pet<=13):
                self.write({'tamano_pet':"grande"})
                self.write({'_tamano':6})
            elif (self.peso_pet>13 and self.peso_pet<100):
                self.write({'tamano_pet':"muygrande"})
                self.write({'_tamano':5})

        elif self.edad_pet=='junior':
        #    self.write({'_raciones':3})
            if (self.peso_pet>=0.7 and self.peso_pet<=4.4):
                self.write({'tamano_pet':"miniatura"})
                self.write({'_tamano':6.5})
            elif (self.peso_pet>4.4 and self.peso_pet<=13.5):
                self.write({'tamano_pet':"pequeno"})
                self.write({'_tamano':5.2})
            elif (self.peso_pet>13.5 and self.peso_pet<=21.3):
                self.write({'tamano_pet':"mediano"})
                self.write({'_tamano':4.5})
            elif (self.peso_pet>21.3 and self.peso_pet<=27.8):
                self.write({'tamano_pet':"grande"})
                self.write({'_tamano':3.7})
            elif (self.peso_pet>27.8 and self.peso_pet<100):
                self.write({'tamano_pet':"muygrande"})
                self.write({'_tamano':3})

            if self.condicion_pet=="muydelgado":
                self.write({'_condicion':0.4})
            elif self.condicion_pet=="delgado":
                self.write({'_condicion':0.2})
            elif self.condicion_pet=="optimo":
                self.write({'_condicion':0.0})
            elif self.condicion_pet=="sobrepeso":
                self.write({'_condicion':-0.2})
            elif self.condicion_pet=="obeso":
                self.write({'_condicion':-0.4})

        elif self.edad_pet=='adult':
    #        self.write({'_raciones':2})
            if (self.peso_pet>=1.5 and self.peso_pet<=5):
                self.write({'tamano_pet':"miniatura"})
                self.write({'_tamano':4})
            elif (self.peso_pet>5 and self.peso_pet<=15):
                self.write({'tamano_pet':"pequeno"})
                self.write({'_tamano':3})
            elif (self.peso_pet>15 and self.peso_pet<=25):
                self.write({'tamano_pet':"mediano"})
                self.write({'_tamano':2.5})
            elif (self.peso_pet>25 and self.peso_pet<=35):
                self.write({'tamano_pet':"grande"})
                self.write({'_tamano':2})
            elif (self.peso_pet>35 and self.peso_pet<100):
                self.write({'tamano_pet':"muygrande"})
                self.write({'_tamano':1.7})

            if self.condicion_pet=="muydelgado":
                self.write({'_condicion':0.25})
            elif self.condicion_pet=="delgado":
                self.write({'_condicion':0.1})
            elif self.condicion_pet=="optimo":
                self.write({'_condicion':0.0})
            elif self.condicion_pet=="sobrepeso":
                self.write({'_condicion':-0.1})
            elif self.condicion_pet=="obeso":
                self.write({'_condicion':-0.25})

        valoracion=self.peso_pet * (self._sexo + self._tamano + self._condicion + self._actividad)*10
        
        if valoracion <300:
            valoracion=50 * ((valoracion + 25) // 50)
        else:
            valoracion=100 * ((valoracion + 50) // 100)

        self.write({'_valoracion':valoracion})

        if self.city=='medellin':
            if valoracion==100:
                self.write({'_paquetes':'13'})
                self.write({'precio':32500})
                self.write({'frecuencia':'mensual'})
                self.write({'ref_bolsa':'200'})
            elif valoracion==150:
                self.write({'_paquetes':'13'})
                self.write({'precio':35750})
                self.write({'frecuencia':'mensual'})
                self.write({'ref_bolsa':'300'})
            elif valoracion==200:
                self.write({'_paquetes':'12'})
                self.write({'precio':30000})
                self.write({'frecuencia':'quincenal'})
                self.write({'ref_bolsa':'200'})
            elif valoracion==250:
                self.write({'_paquetes':'12'})
                self.write({'precio':31500})
                self.write({'frecuencia':'quincenal'})
                self.write({'ref_bolsa':'250'})
            elif valoracion==300:
                self.write({'_paquetes':'12'})
                self.write({'ref_bolsa':'300'})
                self.write({'frecuencia':'quincenal'})
                self.write({'precio':33000})
            elif valoracion==400:
                self.write({'_paquetes':'12'})
                self.write({'ref_bolsa':'200'})
                self.write({'frecuencia':'semanal'})
                self.write({'precio':30000})
            elif valoracion==500:
                self.write({'_paquetes':'12'})
                self.write({'ref_bolsa':'250'})
                self.write({'frecuencia':'semanal'})
                self.write({'precio':31500})
            elif valoracion==600:
                self.write({'_paquetes':'12'})
                self.write({'ref_bolsa':'300'})
                self.write({'frecuencia':'semanal'})
                self.write({'precio':33000})
            elif valoracion==700:
                self.write({'_paquetes':'6-6'})
                self.write({'ref_bolsa':'300-400'})
                self.write({'frecuencia':'semanal'})
                self.write({'precio':36000})
            elif valoracion==800:
                self.write({'_paquetes':'12'})
                self.write({'ref_bolsa':'400'})
                self.write({'frecuencia':'semanal'})
                self.write({'precio':39000})
            elif valoracion==900:
                self.write({'_paquetes':'6-6'})
                self.write({'ref_bolsa':'400-500'})
                self.write({'frecuencia':'semanal'})
                self.write({'precio':42000})
            elif valoracion==1000:
                self.write({'_paquetes':'12'})
                self.write({'ref_bolsa':'500'})
                self.write({'frecuencia':'semanal'})
                self.write({'precio':45000})
            elif valoracion==1100:
                self.write({'_paquetes':'6-6'})
                self.write({'ref_bolsa':'500-600'})
                self.write({'frecuencia':'semanal'})
                self.write({'precio':48000})
            elif valoracion==1200:
                self.write({'_paquetes':'12'})
                self.write({'ref_bolsa':'600'})
                self.write({'frecuencia':'semanal'})
                self.write({'precio':51000})
            elif valoracion==1300:
                self.write({'_paquetes':'6-6'})
                self.write({'ref_bolsa':'600-700'})
                self.write({'frecuencia':'semanal'})
                self.write({'precio':54000})
            elif valoracion==1400:
                self.write({'_paquetes':'12'})
                self.write({'ref_bolsa':'700'})
                self.write({'frecuencia':'semanal'})
                self.write({'precio':57000})

        elif (self.city=='otra' or self.city=='bogota'):
            if valoracion==100:
                self.write({'_paquetes':'13'})
                self.write({'precio':62500})
                self.write({'frecuencia':'mensual'})
                self.write({'ref_bolsa':'200'})
            elif valoracion==150:
                self.write({'_paquetes':'13'})
                self.write({'precio':65750})
                self.write({'frecuencia':'mensual'})
                self.write({'ref_bolsa':'300'})
            elif valoracion==200:
                self.write({'_paquetes':'26'})
                self.write({'precio':91000})
                self.write({'frecuencia':'mensual'})
                self.write({'ref_bolsa':'200'})
            elif valoracion==250:
                self.write({'_paquetes':'26'})
                self.write({'precio':94250})
                self.write({'frecuencia':'mensual'})
                self.write({'ref_bolsa':'250'})
            elif valoracion==300:
                self.write({'_paquetes':'26'})
                self.write({'ref_bolsa':'300'})
                self.write({'frecuencia':'mensual'})
                self.write({'precio':97500})
            elif valoracion==400:
                self.write({'_paquetes':'24'})
                self.write({'ref_bolsa':'200'})
                self.write({'frecuencia':'quincenal'})
                self.write({'precio':84000})
            elif valoracion==500:
                self.write({'_paquetes':'24'})
                self.write({'ref_bolsa':'250'})
                self.write({'frecuencia':'quincenal'})
                self.write({'precio':87000})
            elif valoracion==600:
                self.write({'_paquetes':'24'})
                self.write({'ref_bolsa':'300'})
                self.write({'frecuencia':'quincenal'})
                self.write({'precio':90000})
            elif valoracion==700:
                self.write({'_paquetes':'12-12'})
                self.write({'ref_bolsa':'300-400'})
                self.write({'frecuencia':'quincenal'})
                self.write({'precio':96000})
            elif valoracion==800:
                self.write({'_paquetes':'24'})
                self.write({'ref_bolsa':'400'})
                self.write({'frecuencia':'quincenal'})
                self.write({'precio':102000})
            elif valoracion==900:
                self.write({'_paquetes':'12-12'})
                self.write({'ref_bolsa':'400-500'})
                self.write({'frecuencia':'quincenal'})
                self.write({'precio':108000})
            elif valoracion==1000:
                self.write({'_paquetes':'24'})
                self.write({'ref_bolsa':'500'})
                self.write({'frecuencia':'quincenal'})
                self.write({'precio':114000})
            elif valoracion==1100:
                self.write({'_paquetes':'12-12'})
                self.write({'ref_bolsa':'500-600'})
                self.write({'frecuencia':'quincenal'})
                self.write({'precio':120000})
            elif valoracion==1200:
                self.write({'_paquetes':'24'})
                self.write({'ref_bolsa':'600'})
                self.write({'frecuencia':'quincenal'})
                self.write({'precio':126000})
            elif valoracion==1300:
                self.write({'_paquetes':'12-12'})
                self.write({'ref_bolsa':'600-700'})
                self.write({'frecuencia':'quincenal'})
                self.write({'precio':132000})
            elif valoracion==1400:
                self.write({'_paquetes':'24'})
                self.write({'ref_bolsa':'700'})
                self.write({'frecuencia':'quincenal'})
                self.write({'precio':138000})
