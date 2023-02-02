# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital',
    'author': 'Eddy Daniel',
    'sequence': -100,
    'summary': 'Hospital management system',
    'description': """Hospital management system.""",
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
    ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3'
}
