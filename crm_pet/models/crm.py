# coding: utf-8

from openerp import api, fields, models
from openerp.osv import fields, osv

class crm_pet(models.Model):
    _inherit = "crm.lead"
    _columns = {
        'nombre_pet': fields.char('Nombre'),
        'peso_pet' :  fields.float('Peso en kg'),
        'sexo_pet' : fields.char('Sexo'),
        'edad_pet' : fields.char('Edad Meses'),
        'tamano_pet' : fields.char('Tamaño'),
        'condicion_pet' : fields.char('Condición corporal'),
        'actividad_pet' : fields.char('Actividad Física'),
        '_raciones' : fields.integer('Raciones por día'),
        '_sexo' : fields.float('Sexo'),
        '_tamano' : fields.float('Tamano'),
        '_condicion' : fields.float('Condicion'),
        '_actividad' : fields.float('Actividad'),
        '_valoracion': fields.float(string='Valoración',compute='calculo',store=False),
        'contact_lastname': fields.char('Apellido'),
        'precio' : fields.float('Precio'),
        '_paquetes' : fields.char('Paquetes'),
        'frecuencia' : fields.char('Frecuencia'),
        'ref_bolsa': fields.char('Referencia'),
    }

    @api.multi
    def datos(self):
        valoracion=0
        if self.actividad_pet=='muysedentario':
            self.write({'_actividad':-0.4})
        if self.actividad_pet=='sedentario':
            self.write({'_actividad':-0.2})
        if self.actividad_pet=='normal':
            self.write({'_actividad':0})
        if self.actividad_pet=='activo':
            self.write({'_actividad':0.2})
        if self.actividad_pet=='muyactivo':
            self.write({'_actividad':0.4})
        
        if self.sexo_pet=="macho":
            self.write({'_sexo': 0.2})
        elif self.sexo_pet=="hembra":
            self.write({'_sexo': 0.1})
        
        if self.edad_pet=='puppy':
            self.write({'_raciones':4})
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
            elif (self.peso_pet>13):
                self.write({'tamano_pet':"muygrande"})
                self.write({'_tamano':5})

        elif self.edad_pet=='junior':
            self.write({'_raciones':3})
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
            elif (self.peso_pet>27.8):
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
            self.write({'_raciones':2})
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
            elif (self.peso_pet>35):
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


#        elif self.city=='bogota':
#            if valoracion==100:
#                self.write({'_paquetes':'13'})
#                self.write({'precio':48000})
#                self.write({'frecuencia':'mensual'})
#                self.write({'ref_bolsa':'200'})
#            elif valoracion==150:
#                self.write({'_paquetes':'13'})
#                self.write({'precio':51000})
#                self.write({'frecuencia':'mensual'})
#                self.write({'ref_bolsa':'300'})
#            elif valoracion==200:
#                self.write({'_paquetes':'26'})
#                self.write({'precio':71500})
#                self.write({'frecuencia':'mensual'})
#                self.write({'ref_bolsa':'200'})
#            elif valoracion==250:
#                self.write({'_paquetes':'26'})
#                self.write({'precio':74750})
#                self.write({'frecuencia':'mensual'})
#                self.write({'ref_bolsa':'250'})
#            elif valoracion==300:
#                self.write({'_paquetes':'26'})
#                self.write({'ref_bolsa':'300'})
#                self.write({'frecuencia':'mensual'})
#                self.write({'precio':78000})
#            elif valoracion==400:
#                self.write({'_paquetes':'24'})
#                self.write({'ref_bolsa':'200'})
#                self.write({'frecuencia':'quincenal'})
#                self.write({'precio':66000})
#            elif valoracion==500:
#                self.write({'_paquetes':'24'})
#                self.write({'ref_bolsa':'250'})
#                self.write({'frecuencia':'quincenal'})
#                self.write({'precio':69000})
#            elif valoracion==600:
#                self.write({'_paquetes':'24'})
#                self.write({'ref_bolsa':'300'})
#                self.write({'frecuencia':'quincenal'})
#                self.write({'precio':72000})
#            elif valoracion==700:
#                self.write({'_paquetes':'12-12'})
#                self.write({'ref_bolsa':'300-400'})
#                self.write({'frecuencia':'quincenal'})
#                self.write({'precio':78000})
#            elif valoracion==800:
#                self.write({'_paquetes':'24'})
#                self.write({'ref_bolsa':'400'})
#                self.write({'frecuencia':'quincenal'})
#                self.write({'precio':84000})
#            elif valoracion==900:
#                self.write({'_paquetes':'12-12'})
#                self.write({'ref_bolsa':'400-500'})
#                self.write({'frecuencia':'quincenal'})
#                self.write({'precio':90000})
#            elif valoracion==1000:
#                self.write({'_paquetes':'24'})
#                self.write({'ref_bolsa':'500'})
#                self.write({'frecuencia':'quincenal'})
#                self.write({'precio':96000})
#            elif valoracion==1100:
#                self.write({'_paquetes':'12-12'})
#                self.write({'ref_bolsa':'500-600'})
#                self.write({'frecuencia':'quincenal'})
#                self.write({'precio':102000})
#            elif valoracion==1200:
#                self.write({'_paquetes':'24'})
#                self.write({'ref_bolsa':'600'})
#                self.write({'frecuencia':'quincenal'})
#                self.write({'precio':108000})
#            elif valoracion==1300:
#                self.write({'_paquetes':'12-12'})
#                self.write({'ref_bolsa':'600-700'})
#                self.write({'frecuencia':'quincenal'})
#                self.write({'precio':114000})
#            elif valoracion==1400:
#                self.write({'_paquetes':'24'})
#                self.write({'ref_bolsa':'700'})
#                self.write({'frecuencia':'quincenal'})
#                self.write({'precio':120000})


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


    
    
    
