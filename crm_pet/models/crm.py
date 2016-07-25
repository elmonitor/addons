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
        '_valoracion': fields.float(string='Valoración',compute='calculo'),
        'contact_lastname': fields.char('Apellido'),
        'precio' : fields.float('Precio'),
        '_paquetes' : fields.char('Paquetes'),
        'frecuencia' : fields.char('Frecuencia'),
        'ref_bolsa': fields.char('Referencia'),
    }

    @api.multi
    def calculo(self):
        valoracion=self.peso_pet * (self._sexo + self._tamano + self._condicion + self._actividad)*10
        crm_pet._valoracion=valoracion
