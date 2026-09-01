# -*- coding: utf-8 -*-
{
    'name': 'Manufacturing Intelligence, QC & Predictive Operations',
    'version': '18.0.1.0.0',
    'category': 'Productivity/AI',
    'summary': 'AI-powered manufacturing intelligence, quality control and predictive maintenance',
    'description': """
Manufacturing Intelligence, QC & Predictive Operations
=======================================================

AI-powered manufacturing intelligence suite covering production line monitoring,
quality control inspections, predictive maintenance, KPI dashboards and defect
analysis with AI-driven root cause detection.

Features
--------
- Production line monitoring with OEE tracking and AI efficiency scoring
- Quality inspection records (incoming, in-process, final) with AI defect prediction
- Predictive maintenance alerts with risk levels and AI confidence scoring
- Manufacturing KPI dashboard with AI trend predictions
- Defect analysis with AI root cause detection and corrective actions
""",
    'author': 'SoftaiDev',
    'website': 'https://softaidev.pages.dev',
    'license': 'LGPL-3',
    'price': 1299.99,
    'currency': 'USD',
    'application': True,
    'installable': True,
    'depends': ['base', 'web', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/production_line_views.xml',
        'views/quality_inspection_views.xml',
        'views/predictive_maintenance_views.xml',
        'views/kpi_dashboard_views.xml',
        'views/defect_analysis_views.xml',
        'views/menu.xml',
    ],
    'assets': {},
    'images': ['static/description/cover.png'],
}
