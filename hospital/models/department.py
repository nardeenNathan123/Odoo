from odoo import models, fields

class Department(models.Model):
    _name = "hms.department"

    Name = fields.Char(required=True)
    Capacity = fields.Integer(required=True)
    isOpened = fields.Boolean(default=False)
    patient_ids = fields.One2many(comodel_name='hms.patient', inverse_name='department_id')
