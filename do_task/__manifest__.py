# -*- coding: utf-8 -*-
{
    'name': "UCuenca Test Module",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'countries': ['ec'],

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'mail'],

    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "security/res_groups.xml",
        "views/views.xml",
        "views/templates.xml",
        "data/crm_stage.xml",
        "data/test_sequence.xml",
        # "views/res_config_settings.xml"
    ],
    
    "application": True,
    "installable": True,
}

