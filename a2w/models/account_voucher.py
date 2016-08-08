from openerp import models, api
from num2words import num2words

class AccountVoucher(models.Model):
    _inherit = 'account.voucher'
    
    
    @api.multi
    @api.onchange(amount)
    def a2w(self):
        self.amount_in_word = num2words(self.amount,lang='es')
