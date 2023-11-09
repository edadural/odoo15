from odoo import api, fields, models
from datetime import date
class ArgeErpTask(models.Model):
    _name = "argeerp.task"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "ArgeERP Task"
    _rec_name = "customer_id"

    customer_id = fields.Many2one('argeerp.employee', string='Müşteri', tracking=True)
    project_name = fields.Char(string='Proje Adı', tracking=True)
    project_code = fields.Char(string='Proje Kodu', tracking=True)
    cost = fields.Integer(string='Toplam Maliyet', tracking=True)
    task_time = fields.Date(string='Time', tracking=True, default=fields.Datetime.now)
    task_deadline = fields.Date(string='Deadline', tracking=True)
    ref = fields.Char(string='Reference', tracking=True, help="Reference from patient record")
    html = fields.Html(string='Html')
    img = fields.Image("Image")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority")
    state = fields.Selection([
        ('draft', 'Oluşturuldu'),
        ('in_consultation', 'Bekleniyor'),
        ('done', 'Onaylandı'),
        ('cancel', 'Reddedildi')], default='draft', string="Durum", required=True)
    manager_id = fields.Many2one('res.users', string='Oluşturan', tracking=True)
    groups_id = fields.Many2one('res.groups', string='Departman', tracking=True)

    @api.onchange('customer_id')
    def onchange_employee_id(self):
        self.ref = self.customer_id.ref

    def action_test(self):
        print("button click")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Click Successfull',
                'type': 'rainbow_man'
            }
        }

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

