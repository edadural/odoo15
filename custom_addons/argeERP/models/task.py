from odoo import api, fields, models

class ArgeErpTask(models.Model):
    _name = "argeerp.task"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "ArgeERP Task"

    employee_id = fields.Many2one('argeerp.employee', string='Employee')
    employee_task = fields.Char(string='Task')
