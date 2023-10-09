from odoo.tests import common

class TestMaterial(common.TransactionCase):

    def setUp(self):
        super(TestMaterial, self).setUp()

    def test_create_material(self):
        material = self.env['material_dijual'].create({
            'material_code': 'M001',
            'material_name': 'Test Material',
            'material_type': 'fabric',
            'material_buy_price': 150.0,
            'related_supplier': self.env['supplier_dijual'].create({'name': 'Test Supplier'}).id,
        })
        self.assertEqual(material.material_code, 'M001')
