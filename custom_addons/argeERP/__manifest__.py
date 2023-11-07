# -*- coding: utf-8 -*-

{
    'name': 'ArgeERP',
    'version': '1.0.0',
    'category': 'ArgeERP',
    'author': 'Eda',
    'sequence': -100,
    'summary': 'ArgeERP management system',
    'description': """ArgeERP management system""",
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/task_view.xml',
        'views/page_view.xml',
        'views/employee_view.xml',
        'views/female_employee_view.xml',
    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
