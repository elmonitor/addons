# -*- coding: utf-8 -*-

from openerp import models, api, fields
from num2words import num2words

class AccountVoucher(models.Model):
    _inherit = 'account.voucher'
    a2w = fields.text('Cantidad en letras')
    
    
    @api.multi
    @api.onchange('amount')
    def a2w(self):
        _a2w = num2words(self.amount,lang='es')
        self.write({'a2w':_a2w})
