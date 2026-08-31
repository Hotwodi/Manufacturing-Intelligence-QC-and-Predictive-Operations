# -*- coding: utf-8 -*-
from odoo import fields, models


class PredictiveMaintenance(models.Model):
    _name = 'miqc.predictive.maintenance'
    _description = 'Predictive Maintenance Alert'
    _order = 'predicted_failure_date'

    name = fields.Char(string='Reference', required=True, default='New')
    machine_id = fields.Char(string='Machine ID', required=True)
    asset_name = fields.Char(string='Asset Name', required=True)
    risk_level = fields.Selection(
        [
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
            ('critical', 'Critical'),
        ],
        string='Risk Level',
        default='low',
        required=True,
    )
    predicted_failure_date = fields.Date(string='Predicted Failure Date')
    ai_confidence = fields.Float(
        string='AI Confidence (%)',
        help='AI confidence score for the prediction (0-100)',
    )
    maintenance_type = fields.Selection(
        [
            ('preventive', 'Preventive'),
            ('corrective', 'Corrective'),
            ('predictive', 'Predictive'),
        ],
        string='Maintenance Type',
        default='predictive',
        required=True,
    )
    state = fields.Selection(
        [
            ('scheduled', 'Scheduled'),
            ('in_progress', 'In Progress'),
            ('done', 'Done'),
        ],
        string='State',
        default='scheduled',
        required=True,
    )
    assigned_to = fields.Char(string='Assigned To')
    notes = fields.Text(string='Notes')

    def action_start(self):
        for rec in self:
            rec.state = 'in_progress'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_schedule(self):
        for rec in self:
            rec.state = 'scheduled'
