{
    'name': 'Hospi PO',
    'version': '14.0.1.0.0',
    'author': 'Amirul',
    'summary': 'Custom PO',
    'website': '',
    'description': """
    """,
    'data': [
        'data/sequences.xml',
        'report/purchase_order.xml',
        'views/product_product_view.xml',
        'views/account_custom.xml',
        'views/inventory_custom.xml',
        'views/inherit_stock_picking.xml',
        
    ],
    'depends': ['purchase'],
    'auto_install': False,
    'installable': True,
    'application': False,
}