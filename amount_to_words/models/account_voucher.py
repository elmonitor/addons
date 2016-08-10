# -*- coding: utf-8 -*-

from openerp import api, fields, models
from openerp.osv import fields, osv
from num2words import num2words

class AccountVoucher(models.Model):
    _inherit = 'account.voucher'
    _columns={
    'a2w':fields.text('Cantidad en letras'),
    }
    
    @api.multi
    @api.depends('amount')
    def a_2_w(self):
        self._a2w = num2words('amount',lang='es')
        self.write({'a2w':_a2w})
        print("*********************")
