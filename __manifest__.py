# -*- coding: utf-8 -*-
{
    'name': "TSBRANDS",

    'summary': """
        Modificaciones al proyecto de TSBRANDS""",

    'description': """
        
    """,

    'author': "Softhink",
    'website': "http://www.sft.com.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'stock'],

    # always loaded
    'data': [

        'views/stock_picking_view.xml',

    ],
    'qweb': [],
    #"post_init_hook": "post_init_hook",
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
        #"autofactura/template.xml"
    ],
    #"images":['static/description/Integracion4.jpg']
}
