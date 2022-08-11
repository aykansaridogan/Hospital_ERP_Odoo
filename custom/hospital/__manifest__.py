# -*- coding: utf-8 -*-
{
    'name': 'Hospital Management',
    'version': '1.2',
    'summary': 'Hospital Management Software',
    'sequence': 10,
    'category': 'Productivity',
    'website': 'aykansaridogan@gmail.com',
    'license': 'LPGL-3',
    'author': 'Aykan Sarıdoğan',
    'maintainer': 'Aykan SARIDOGAN',
    'depends': ['base', 'mail', 'sale'],
    'data': [
            'security/ir.model.access.csv',
             'security/security.xml',
             'wizards/create_appointment.xml',
             'data/sequence.xml',
             'views/appointment.xml',
             'views/doctor.xml',
             'views/patient.xml',
             'report/report.xml'
    ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False,
    
},
