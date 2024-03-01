
from odoo import models, fields

class TodoList(models.Model):
    _name = 'todo.ticket'
    _description = 'Todo app'

    name = fields.Char(required=True)
    description = fields.Text()
    number = fields.Integer()
    tags = fields.Char()
    state = fields.Selection([('new', 'New'), ('doing', 'Doing'), ('done', 'Done')])
    file = fields.Binary()
