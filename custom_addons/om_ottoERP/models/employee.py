
from odoo import api, fields, models

class OttoErpEmployee(models.Model):
    _name = "ottoerp.employee"
    _description = "OttoERP employee"

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male','Male'), ('female','Female')], string="Gender")