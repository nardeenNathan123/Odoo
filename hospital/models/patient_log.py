from odoo import models, fields


class PatientLogHistory(models.Model):
    _name = 'patient.log.history'
    _description = 'Patient Log History'

    patient_id = fields.Many2one('your.patient.model', string='Patient')
    created_by = fields.Many2one('res.users', string='Created By')
    date = fields.Date(string='Date')
    description = fields.Text(string='Description')
