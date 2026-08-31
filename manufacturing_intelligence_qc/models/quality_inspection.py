# -*- coding: utf-8 -*-
from odoo import fields, models


class QualityInspection(models.Model):
    _name = 'miqc.quality.inspection'
    _description = 'Quality Inspection Record'
    _order = 'name desc'

    name = fields.Char(string='Reference', required=True, default='New')
    product = fields.Char(string='Product', required=True)
    inspection_type = fields.Selection(
        [
            ('incoming', 'Incoming'),
            ('in_process', 'In-Process'),
            ('final', 'Final'),
        ],
        string='Inspection Type',
        default='in_process',
        required=True,
    )
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('passed', 'Passed'),
            ('failed', 'Failed'),
            ('rework', 'Rework'),
        ],
        string='State',
        default='draft',
        required=True,
    )
    defect_count = fields.Integer(string='Defect Count', default=0)
    inspector = fields.Char(string='Inspector')
    ai_defect_prediction = fields.Float(
        string='AI Defect Prediction (%)',
        help='AI-predicted probability of defects (0-100)',
    )
    notes = fields.Text(string='Notes')
    date_inspected = fields.Datetime(string='Date Inspected', default=fields.Datetime.now)

    def action_pass(self):
        for rec in self:
            rec.state = 'passed'

    def action_fail(self):
        for rec in self:
            rec.state = 'failed'

    def action_rework(self):
        for rec in self:
            rec.state = 'rework'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'
