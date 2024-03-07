from odoo import models, fields, api, exceptions
from datetime import datetime
class HmsPatient(models.Model):
    _name = "hms.patient"
    _description = 'Hospital Patient'

    name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    birth_date = fields.Date()
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    ])
    pcr = fields.Boolean()
    image = fields.Binary(attachment=True)
    address = fields.Text()
    age = fields.Integer(compute='_compute_age', store=True)
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),
    ], default='undetermined')
    department_id = fields.Many2one('hms.department', domain="[('isOpened', '=', True)]")
    doctor_id = fields.Many2one('hms.doctor', string='Doctor')
    department_capacity = fields.Integer(string='Department Capacity', related='department_id.Capacity')
    department_name = fields.Char(string='Department Name', related='department_id.Name', store=True)
    doctor_name = fields.Char(string='Doctor Name', related='doctor_id.First_name', store=True)
    state_log_ids = fields.One2many('patient.state.log', 'patient_id', string='State Logs')

    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                birth_date_str = record.birth_date.strftime('%Y-%m-%d')
                birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
                today = datetime.today().date()
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                record.age = age
            else:
                record.age = 0

    @api.constrains('department_id')
    def _check_department_opened(self):
        for patient in self:
            if patient.department_id and not patient.department_id.isOpened:
                raise exceptions.ValidationError("You cannot choose a closed department for the patient.")

    def write(self, vals):
        if 'state' in vals:
            vals['state_log_ids'] = [(0, 0, {'state': vals['state']})]
        return super(HmsPatient, self).write(vals)

class PatientStateLog(models.Model):
    _name = 'patient.state.log'
    _description = 'Patient State Log'

    patient_id = fields.Many2one('hms.patient', string='Patient')
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),
    ], string='State')
    date = fields.Date(default=fields.Date.today(), string='Date')
    created_by = fields.Many2one('res.users', string='Created By', default=lambda self: self.env.user.id)
