# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductionLine(models.Model):
    _name = 'miqc.production.line'
    _description = 'Production Line Monitoring'
    _order = 'name'

    name = fields.Char(string='Production Line', required=True, translate=True)
    code = fields.Char(string='Code', required=True)
    active = fields.Boolean(string='Active', default=True)
    capacity = fields.Float(string='Capacity (units/hr)')
    oee_target = fields.Float(string='OEE Target (%)', default=85.0)
    current_oee = fields.Float(string='Current OEE (%)')
    state = fields.Selection(
        [
            ('running', 'Running'),
            ('idle', 'Idle'),
            ('stopped', 'Stopped'),
            ('maintenance', 'Maintenance'),
        ],
        string='State',
        default='idle',
    )
    throughput = fields.Float(string='Throughput (units/hr)')
    downtime_hours = fields.Float(string='Downtime (hours)')
    ai_efficiency_score = fields.Float(
        string='AI Efficiency Score',
        help='AI-generated efficiency score (0-100)',
    )

    def name_get(self):
        result = []
        for record in self:
            name = record.name
            if record.code:
                name = '[%s] %s' % (record.code, record.name)
            result.append((record.id, name))
        return result
