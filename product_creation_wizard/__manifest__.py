# -*- coding: utf-8 -*-
{
    'name': "product_creation_wizard",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com
    """,

    'description': """
        Long description of module's purpose
    """,

    'author': "TDT Consultants",
    'website': "http://www.tdtconsultants.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'tdt',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['web_enterprise', 'product', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'wizard/create_product_wizard.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'data/demo.xml',
    ],
    'license': 'OPL-1',
}