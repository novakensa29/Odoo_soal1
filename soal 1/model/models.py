from odoo import models, fields, api

class Material(models.Model):
    _name = 'material_dijual'
    _description = 'Material Information'

    material_code = fields.Char(string='Material Code', required=True)
    material_name = fields.Char(string='Material Name', required=True)
    material_type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton'),
    ], string='Material Type', required=True)
    material_buy_price = fields.Float(string='Material Buy Price', required=True)
    related_supplier = fields.Many2one('supplier_dijual', string='Related Supplier', required=True)

class Supplier(models.Model):
    _name = 'supplier_dijual'
    _description = 'Supplier Information'

    name = fields.Char(string='Supplier Name', required=True)
