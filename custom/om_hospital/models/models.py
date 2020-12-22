# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class custom/om_hospital(models.Model):
#     _name = 'custom/om_hospital.custom/om_hospital'
#     _description = 'custom/om_hospital.custom/om_hospital'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


from odoo import models, fields


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Module for managing hospital'

    patient_name = fields.Char(string='Name', required=False)
    patient_age = fields.Integer('Age')
    notes = fields.Text(string='Note')
    image = fields.Binary(string='Image')


