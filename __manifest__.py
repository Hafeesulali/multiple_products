{
    'name': 'Multiple Product Sale and Purchase',
    'description': 'option to add multiple products in sale and purchase order lines.',
    'installable': True,
    'version': '16.0.1.0.0',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/multiple_product_wizard.xml',
        'views/multiproduct_inherit.xml',

    ],

}
