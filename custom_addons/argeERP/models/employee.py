from datetime import date
from odoo import api, fields, models

class ArgeErpEmployee(models.Model):
    _name = "argeerp.employee"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "ArgeERP employee"

    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date(string='Date Of Birth', tracking=True)
    ref = fields.Char(string='Reference', default='Odoo Mates', tracking=True)
    age = fields.Integer(string='Age', compute='_compute_age', tracking=True)
    gender = fields.Selection([('male','Male'), ('female','Female')], string="Gender", tracking=True)
    active = fields.Boolean(string='Active', default=True)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1