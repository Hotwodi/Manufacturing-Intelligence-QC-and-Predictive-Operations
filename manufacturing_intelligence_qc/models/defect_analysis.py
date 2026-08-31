# -*- coding: utf-8 -*-
from odoo import fields, models


class DefectAnalysis(models.Model):
    _name = 'miqc.defect.analysis'
    _description = 'Defect Analysis with AI'
    _order = 'name'

    name = fields.Char(string='Reference', required=True, default='New')
    defect_type = fields.Char(string='Defect Type', required=True)
    root_cause = fields.Text(string='Root Cause')
    occurrence_count = fields.Integer(string='Occurrence Count', default=1)
    ai_root_cause_confidence = fields.Float(
        string='AI Root Cause Confidence (%)',
        help='AI confidence score for the identified root cause (0-100)',
    )
    corrective_action = fields.Text(string='Corrective Action')
    state = fields.Selection(
        [
            ('open', 'Open'),
            ('analyzing', 'Analyzing'),
            ('resolved', 'Resolved'),
        ],
        string='State',
        default='open',
        required=True,
    )
    date_opened = fields.Datetime(string='Date Opened', default=fields.Datetime.now)

    def action_analyze(self):
        for rec in self:
            rec.state = 'analyzing'

    def action_resolve(self):
        for rec in self:
            rec.state = 'resolved'

    def action_open(self):
        for rec in self:
            rec.state = 'open'
