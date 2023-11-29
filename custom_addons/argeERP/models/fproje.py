from odoo import api, fields, models

class ArgeErpFproje(models.Model):
    _name = "argeerp.fproje"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "ArgeERP fproje"

    project_name = fields.Many2one('argeerp.task', string='Proje Adı', tracking=True)
    customer_id = fields.Many2one('argeerp.employee', string='Müşteri', tracking=True)
    process = fields.Selection([
        ('L00', 'L00 - Teklif'),
        ('L01', 'L01 - Kick-Off'),
        ('L02', 'L02 - Ön Tasarım'),
        ('L03', 'L03 - Detay Tasarım'),
        ('L04', 'L04 - Tasarım Dondurma'),
        ('L05', 'L05 - Üretim Planı'),
        ('L06', 'L06 - Tedarik'),
        ('L07', 'L07 - Fonksiyonel Üretim'),
        ('L08', 'L08 - Devreye Alma & Final Montaj'),
        ('L09', 'L09 - COP'),
        ('L10', 'L10 - Ön Kabul'),
        ('L11', 'L11 - Sevkiyat'),
        ('L12', 'L12 - Kabul'),
        ('L13', 'Kapanan Projeler'),], default='L00', string="Aşama", required=True)


# @api.onchange('customer_id')
# def onchange_employee_id(self):
#         self.project_name = self.customer_id.project_name
