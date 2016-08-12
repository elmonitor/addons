# -*- coding: utf-8 -*-
# © 2016 3NODUS SAS (<http://3nodus.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Amount to Words',
    'author': '3nodus',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Check printing commons',
    'description': """
    This module converts to text the field amount from account.voucher model  
    """,
    'website': 'https://www.github.com/3nodus/addons',
    'depends' : ['account_voucher',' res_currency_print_on_check'],
    'data': [
        'views/account_voucher_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
