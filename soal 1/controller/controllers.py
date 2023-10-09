from odoo import http
from odoo.http import request

class MaterialController(http.Controller):

    @http.route('/materials', auth='user', website=True)
    def materials_list(self, **kwargs):
        materials = request.env['material_dijual'].sudo().search([])
        return request.render('material_dijual_tree_view', {'materials': materials})

    @http.route('/material/<int:material_id>', auth='user', website=True)
    def material_detail(self, material_id, **kwargs):
        material = request.env['material_dijual'].sudo().browse(material_id)
        return request.render('material_dijual_form_view', {'material': material})

    @http.route('/material/<int:material_id>/update', auth='user', website=True, methods=['POST'])
    def material_update(self, material_id, **post):
        material = request.env['material_dijual'].sudo().browse(material_id)
        if material:
            material.write(post)
        return request.redirect('/materials')

    @http.route('/material/<int:material_id>/delete', auth='user', website=True)
    def material_delete(self, material_id, **kwargs):
        material = request.env['material_dijual'].sudo().browse(material_id)
        if material:
            material.unlink()
        return request.redirect('/materials')
