# -*- coding: utf-8 -*-
{
    'name': "dw_proma",

    'summary': """
        Aqui va el summary""",

    'description': """
        Aqui la descripcion larga
    """,

    'author': "Gabriel Pabon",
    'website': "http://www.seindw.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/personal.xml',
        'views/aeronaves.xml',
        'views/motores.xml',
        'views/helices.xml',
        'views/alertas.xml',

    ],
    # only loaded in demonstration mode

}
