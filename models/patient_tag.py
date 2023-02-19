# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "patient.tag"
    _description = "Patient Tag "

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active')
    color = fields.Integer(string='Color')

