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
        resuser=self.pool.get('res.users')
        userid=resuser.search(self._cr,self._uid,[('id','=',self._uid)],context=self._context)
        raise Warning(userid)
        _aws = num2words(self.amount,lang=reslang)
        self.a2w = _aws.upper()
#        self.write({'a2w':_a2w})
#        print("*********************")
