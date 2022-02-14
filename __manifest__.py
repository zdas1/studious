# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Repair Page',
    'version': '15.0.1',
    'summary': 'Repair page',
    'sequence': 4,
    'description': """
Repair Webpage
====================
This is a simple repair webpage module which saves the data's entered by the user.
    """,
    'category': 'Website/Website',
    'website': 'www.test.com',
    'depends': ['web', 'repair'],
    'data': ['views/template.xml',
             'views/repair_form.xml'
    ],
    'qweb': [],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
