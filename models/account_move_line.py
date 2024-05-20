##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import api, models, fields, _
from datetime import date, timedelta
# from odoo.exceptions import ValidationError


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    debt_balance_ipc = fields.Float(
        'Deuda IPC',
        compute='_compute_debt_balance_ipc',
    )

    # This computes makes fields to be computed upon partner creation where no
    # id exists yet and raise an erro because of partner where being empty on
    # _credit_debit_get method, ase debit and credit don't have depends, this
    # field neither
    # @api.depends('debit', 'credit')
    def _compute_debt_balance_ipc(self):
        for rec in self:
            res = 0
            if rec.amount_residual > 0:
                base_amount = rec.amount_residual
                start_date = rec.date_maturity
                end_date = date.today()
                delta = timedelta(days=1)
                if start_date:
                    while (start_date <= end_date):
                        ipc = self.env['account.ipc'].search([('date','=',start_date)])
                        if ipc:
                            rate = 1 + ipc.amount / 100
                            base_amount = base_amount * rate
                        start_date += delta
                    if base_amount:
                        res = base_amount

            rec.debt_balance_ipc = res
