# -*- coding: utf-8 -*-
from odoo import fields, models


class KpiDashboard(models.Model):
    _name = 'miqc.kpi.dashboard'
    _description = 'Manufacturing KPI Dashboard'
    _order = 'period desc'

    name = fields.Char(string='KPI Name', required=True)
    period = fields.Char(string='Period', required=True, help='e.g. 2026-08')
    oee = fields.Float(string='OEE (%)')
    availability = fields.Float(string='Availability (%)')
    performance = fields.Float(string='Performance (%)')
    quality_rate = fields.Float(string='Quality Rate (%)')
    scrap_rate = fields.Float(string='Scrap Rate (%)')
    on_time_delivery = fields.Float(string='On-Time Delivery (%)')
    ai_trend_prediction = fields.Text(
        string='AI Trend Prediction',
        help='AI-generated trend prediction narrative',
    )
