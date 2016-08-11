# -*- coding: utf-8 -*-

from openerp import api, fields, models
from openerp.osv import fields, osv
from num2words import num2words

class AccountVoucher(models.Model):
    _inherit = 'account.voucher'
    _columns={
    'a2w':fields.text('Cantidad en letras',compute='a_2_w'),
    }
    
#    @api.multi
    @api.depends('amount')
#    @api.onchange('amount')    
    def a_2_w(self):
        print(num2words(float('amount'),lang='es'))
        self.a2w = str(float(num2words('amount'),lang='es'))
#        self.write({'a2w':_a2w})
#        print("*********************")
