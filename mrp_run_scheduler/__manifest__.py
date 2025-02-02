# -*- coding: utf-8 -*-
{
    'name': "Mrp Run Scheduler Automation",

    'summary': """
        Üretim emri oluşturulması ve satış siparişinin onaylanması sonucunda run_scheduler çalıştırmak için geliştirilen uygulama""",

    'description': """
        Üretim emri oluşturulması ve satış siparişinin onaylanması sonucunda run_scheduler çalıştırmak için geliştirilen uygulama
    """,

    'author': "MechSoft",
    'website': "https://www.mechsoft.com.tr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Manufacturing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mrp', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True
}
