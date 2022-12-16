# -*- coding: utf-8 -*-
{
    'name': "Quản lý sách",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "AnhDaiDo",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/book_management_security.xml',
        'security/ir.model.access.csv',
        
        'views/views.xml',
        'views/templates.xml',
        'views/customer_view.xml',
        'views/book_view.xml',
        'views/borrow_view.xml',
        'views/report_view.xml',
        'data/customer.csv',
        'data/book.csv',
        # 'data/borrow.csv'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'sequence': -1000,
    'application': True,
}
