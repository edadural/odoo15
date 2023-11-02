# -*- coding: utf-8 -*-

{
    'name': 'OttoERP',
    'version': '1.0.0',
    'category': 'OttoERP',
    'author': 'Eda',
    'sequence': -100,
    'summary': 'OttoERP management system',
    'description': """OttoERP management system""",
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/employee_view.xml',
        'views/female_employee_view.xml',
    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
