{
    'name': "Inventory Configurator",
    'version': "17.0",
    'summary': "Inventory Configurator",
    'description': """
        "Inventory Configurator"
    """,
    'author': "Adil Akbar",
    'website': "https://github.com/aadilakbar",
    'category': "Inventory",
    'depends': ['product', 'stock', 'point_of_sale', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_product_view.xml',
        'wizard/product_import_wizard_view.xml',
    ],
    'demo': [
    ],
}
