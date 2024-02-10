# -*- coding: utf-8 -*-
{
    'name': "DO Task",

    'summary': "The DO Dev Task Odoo Module",

    'description': """
    DO Task is a module for the Odoo framework that allows you to create and manage tasks.
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'demo/demo.xml',
        'security/res_groups.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'license': 'OEEL-1',

    'installable': True,
    'application': True,
}

