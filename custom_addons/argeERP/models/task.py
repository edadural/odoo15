from odoo import api, fields, models

class ArgeErpTask(models.Model):
    _name = "argeerp.task"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "ArgeERP Task"
    _rec_name = "employee_id"

    employee_id = fields.Many2one('argeerp.employee', string='Employee', tracking=True)
    employee_task = fields.Char(string='Task', tracking=True)
    task_time = fields.Date(string='Time', tracking=True, default=fields.Datetime.now)
    task_deadline = fields.Date(string='Deadline', tracking=True)
    ref = fields.Char(string='Reference', tracking=True)
    html = fields.Html(string='Html')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], default='draft', string="Status", required=True)

    @api.onchange('employee_id')
    def onchange_employee_id(self):
        self.ref = self.employee_id.ref

    def action_test(self):
        print("button click")