from odoo import api, fields, models

class ArgeErpPage(models.Model):
    _name = "argeerp.page"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "ArgeERP page"

    employee_id = fields.Many2one('argeerp.employee', string='Employee', tracking=True)
