from odoo import http
from odoo.http import request


class RepairPage(http.Controller):
    @http.route('/repair/forms', type='http', auth='public', website=True)
    def repair(self, product_qty=None, description=None, invoice_method=None):
        product_id = request.env['product.product'].sudo().search([])
        partner_id = request.env['res.partner'].sudo().search([])
        address_id = request.env['res.partner'].sudo().search([])
        location_id = request.env['stock.location'].sudo().search([])
        sale_order_id = request.env['sale.order'].sudo().search([])
        product_uom = request.env['uom.uom'].sudo().search([])
        return request.render('new_task.create_repair_form',
                              {'description': description,
                               'product_id': product_id,
                               'partner_id': partner_id,
                               'address_id': address_id,
                               'product_qty': product_qty,
                               'sale_order_id': sale_order_id,
                               'location_id': location_id,
                               'invoice_method': invoice_method,
                               'product_uom': product_uom})

    @http.route("/create/repair", type='http', auth='public', website=True)
    def create_repair_backend(self,  **kw):
        request.env["repair.order"].sudo().create(kw)
        return request.render('new_task.repair_thanks', {})


class FirstPage(http.Controller):
    @http.route('/repair/first', type='http', auth='public', website=True)
    def menu_in_form(self):
        return request.render('new_task.repair_page', {})
