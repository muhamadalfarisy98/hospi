from odoo import api, fields, models


class VatResPartner(models.Model):
    _inherit = 'account.move'
    # _description = 'New Description'

    vat_child = fields.Char(string='VAT', help ='VAT child')