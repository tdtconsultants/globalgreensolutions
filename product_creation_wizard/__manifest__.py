# -*- coding: utf-8 -*-
{
    'name': "product_creation_wizard",

    'summary': """
        This module adds the create product button to sale order 
    """,

    'description': """
        Add an easy way to create a product and its bom from sale order
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