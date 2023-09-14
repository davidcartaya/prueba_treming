from odoo import api, fields, models, _

class PatientsVisits(models.Model):
    _name = 'patient.visits'

    date = fields.Datetime(string="Fecha y hora")
    name = fields.Char(string="Nombre del visitante")
    patient_id = fields.Many2one('res.partner', string="Paciente")
    reason = fields.Text(string="Motivo de visita")
    