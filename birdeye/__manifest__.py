# -*- coding: utf-8 -*-
{
    'name': "birdeye",

    'summary': """
        custom Website CMS building block 
        """,

    'description': """
        website building block for Odoo V13 apper in Odoo CMS editor 
        contain stars review box that pulls data from Birdeye.com using API credentials. And shows current business reviews.
    """,

    'author': "Orion Technology",
    'website': "https://www.oriontech.info/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # Load the snippets (building block code) when installing
        'views/snippets.xml',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
