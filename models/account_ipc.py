##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import api, models, fields, _
# from odoo.exceptions import ValidationError


class AccountIpc(models.Model):
    _name = 'account.ipc'
    _description = 'account.ipc'

    amount = fields.Float('IPC')
    date = fields.Date('Fecha')
