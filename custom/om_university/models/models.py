
from odoo import models, fields, api, _


class UniversityStudent(models.Model):
    _name = 'university.student'
    _description = 'Module for managing student'
    _rec_name = 'st_name'

    st_name = fields.Char(string="Name")
    st_email = fields.Char(string="Email ID")
    st_age = fields.Integer(string="Age")
    st_batch = fields.Integer(string="Batch")
    st_department = fields.Char(string="Department")
    st_image = fields.Binary(string="Image")
    st_address = fields.Char(string="Address")
    st_notes = fields.Text(string="Note")
    name_seq = fields.Char(string='Patient ID', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('university.student.sequence') or _('New')
        result = super(UniversityStudent, self).create(vals)
        return result
