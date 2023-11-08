from odoo import api, fields, models

class ArgeErpPage(models.Model):
    _name = "argeerp.page"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "ArgeERP page"
    _rec_name = "task_id"

    employee_id = fields.Many2one('argeerp.employee', string='Employee', tracking=True)
    manager_id = fields.Many2one('res.users', string='Manager', tracking=True)
    groups_id = fields.Many2one('res.groups', string='Manager', tracking=True)
    task_id = fields.Many2one('argeerp.task', string='Task', tracking=True)
    state = fields.Selection([
        ('draft', 'Oluşturuldu'),
        ('in_consultation', 'Bekleniyor'),
        ('done', 'Onaylandı'),
        ('cancel', 'Reddedildi')], default='draft', string="Status", required=True)


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