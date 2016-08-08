# -*- coding: utf-8 -*-

from openerp.osv import models, api, fields, osv

from num2words import num2words

class AccountVoucher(models.Model):
    _inherit = 'account.voucher'
    a2w = fields.char('Cantidad en letras')
    
    
    @api.multi
    @api.onchange('amount')
    def a_2_w(self):
        _a2w = num2words(self.amount,lang='es')
        self.write({'a2w':_a2w})
