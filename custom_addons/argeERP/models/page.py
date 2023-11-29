from odoo import api, fields, models

class ArgeErpPage(models.Model):
    _name = "argeerp.page"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "ArgeERP page"
    _rec_name = "task_id"

    employee_id = fields.Many2one('argeerp.employee', string='Müşteri', tracking=True)
    manager_id = fields.Many2one('res.users', tracking=True)
    groups_id = fields.Many2one('res.groups', tracking=True)
    task_id = fields.Many2one('argeerp.task', string='Task', tracking=True)
    state = fields.Selection([
        ('draft', 'Oluşturuldu'),
        ('in_consultation', 'Bekleniyor'),
        ('done', 'Onaylandı'),
        ('cancel', 'Reddedildi')], default='draft', string="Status", required=True)
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
        ('L13', 'Kapanan Projeler'), ], default='L00', string="Aşama", required=True)


    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'