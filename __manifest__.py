{
    'name': "SkillOdoo",
    'summary': "Trial Odoo",
    'description': "Trial Odoo",
    'author': "Rizky Damara Ardy",
    'category': 'Sales',
    'version': '14.0.1.0.0',
    'depends': ['sale', 'purchase'],
    'data': [
        'views/sale_order_view.xml'
      #  'views/purchase_order_view.xml',
        # Tambahkan file-file XML lain yang Anda butuhkan di sini
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
