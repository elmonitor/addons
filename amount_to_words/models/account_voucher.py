# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.osv import fields, osv
from num2words import num2words as n2w


class account_voucher(models.Model):
    _inherit = 'account.voucher'
    columns= {
        'amount_2_word':fields.text("Amount in Words"),
    }
    @api.onchange
    def amount2word(self, cr, uid, amount, currency_id, context=None):
        #currency = self.pool['res.currency'].browse(cr, uid, currency_id, context=context)
        self.write({'amount_2_word':n2w.num2words(amount,lang='es')})
        print("************************************")
        print(amount_2_word)