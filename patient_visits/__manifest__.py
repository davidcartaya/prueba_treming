# -*- coding: utf-8 -*-
{
    'name': "Visitas de Pacientes",

    'summary': """
        - Control de visitas de pacientes
    """,

    'description': """
        - Control de visitas de pacientes
    """,


    'contribuitors': "David cartaya <david.cartaya2003@gmail.com>",
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/patient_visits.xml',
    ],
}
