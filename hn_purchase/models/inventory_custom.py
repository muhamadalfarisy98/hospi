from odoo import api, fields, models


class KoliCustom(models.Model):
    _inherit = 'stock.picking'

    total_koli = fields.Float(string='Total Koli')
    # total_koli = fields.Float(string='Total Koli',compute='_get_total_koli')
    koli = fields.Float(string='Koli')
    

    # @api.depends('move_line_ids_without','move_line_ids_without.qty_done')
    # def _get_total_koli(self):
    #     total=0
    #     for r in self:
    #         for line in r.move_line_ids_without:
    #             total+=line.qty_done
    #         r['total_koli']=total
    
