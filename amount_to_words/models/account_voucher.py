# -*- coding: utf-8 -*-

import num2words as n2w
from openerp import models, fields, api

class account_voucher(models.Model):
    _inherit = 'account.voucher'
    amount_2_word = fields.char("Amount in Words")
    
    @api.onchange('amount')
    def amount2word(self, cr, uid, amount, currency_id, context=None):
        currency = self.pool['res.currency'].browse(cr, uid, currency_id, context=context)
        amount_2_word = n2w.num2words(amount,lang='es')
