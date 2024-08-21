# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hospital management',
    'version': '1.0.0',
    'category': 'Hospital',
    'author': 'Kevin Kipruto',
    'sequence': -100,
    'summary': 'Hospital management system',
    'description': """hospital management system""",
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/male_patient_view.xml'
    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
