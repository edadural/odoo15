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
    age = fields.Integer(string='Age', tracking=True)

    @api.onchange('employee_id')
    def onchange_employee_id(self):
        self.ref = self.employee_id.ref
        self.age = self.employee_id.age