# -*- coding: utf-8 -*-

from openerp import models, api
from num2words import num2words

class AccountVoucher(models.Model):
    _inherit = 'account.voucher'
    
    
    @api.multi
    @api.onchange(amount)
    def a2w(self):
        _a2w = num2words(self.amount,lang='es')
        self.write({'amount_in_word':_a2w})
