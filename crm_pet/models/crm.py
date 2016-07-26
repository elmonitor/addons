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
        '_valoracion': fields.float(string='Valoración'),
        'contact_lastname': fields.char('Apellido'),
        'precio' : fields.float('Precio'),
        '_paquetes' : fields.char('Paquetes'),
        'frecuencia' : fields.char('Frecuencia'),
        'ref_bolsa': fields.char('Referencia'),
    }

    #This method will be called when either the field CostPrice or the field ShippingCost changes.
    @api.multi
    def calculo(self,cr,user,ids,_sexo,_tamano,_condicion,_actividad,peso_pet,context=None):
	    #Calculate the total
	valoracion = peso_pet * (_sexo + _tamano + _condicion + _actividad)*10
        res = {
            'value': {
		'_valoracion': valoracion
            }
        }
	#Return the values to update it in the view.
	return res



  
    @api.multi
    def datos(self):
        #valoracion=0

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

#class crm_lead(models.Model):
#    _inherit = "crm.lead"    
#    def create(self, cr, uid, vals, context=None):
#        crm_pet.datos(self)
#        crm_pet.calculo(self)
