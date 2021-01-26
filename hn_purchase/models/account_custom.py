from odoo import api, fields, models


class VatResPartner(models.Model):
    _inherit = 'account.move'
    # _description = 'New Description'

    vat_child = fields.Char(string='VAT', help ='VAT child')

    @api.model
    def create(self,vals):
        print('self', self)
        print('vals',vals)
        ret=super(VatResPartner,self).create(vals)
        print('ret,',ret)
        print('ret.vat_child',ret.vat_child)
        if not ret.vat_child:
            print('kosong')
            print('return partner id',ret.partner_id)
            print('rreturn vatnya partnert id',ret.partner_id.vat)
            ret.vat_child=ret.partner_id.vat
            print('passing nilai',ret.vat_child)
        return ret

