# -*- coding: utf-8 -*-
# © 2016 3NODUS SAS (<http://3nodus.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models
from openerp.osv import fields, osv
from num2words import num2words

class AccountVoucher(models.Model):
    _inherit = 'account.voucher'
    _columns={
    'a2w':fields.text('Amount in text',compute='a_2_w'),
    }
    
    @api.depends('amount')
    def a_2_w(self):
        reslang=self.pool['res.users'].browse(self._cr,self._uid,self._uid,context=self._context).partner_id.lang
        rescurrency= self.pool['res.currency'].browse(self._cr,self._uid,self._uid,context=self._context).print_on_check 
        _aws = num2words(self.amount,lang=reslang)
        self.a2w = _aws.upper()
