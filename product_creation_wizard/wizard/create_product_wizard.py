from odoo import models, fields, api

class ProductCreateWizard(models.TransientModel):
    _name = "product.create_wizard"

    categ_id = fields.Many2one('product.category', "Category")
    name = fields.Char("Name")
    uom = fields.Many2one('uom.uom', "Unit of Measure")
    price = fields.Float("Price")

    def create_product(self):
        #New Product Creation
        routes = self.env['stock.location.route'].search([('name', 'in', ['Replenish on Order (MTO)', 'Manufacture'])])
        new_prod = {
            'name': self.name,
            'route_ids': routes.ids,
            'categ_id': self.categ_id.id,
            'list_price': self.price,
            'uom_id': self.uom.id,
            'uom_po_id': self.uom.id,
        }
        product = self.env['product.template'].sudo().create(new_prod)

        #Create BoM
        new_bom = {
            'product_tmpl_id': product.id,
        }
        bom = self.env['mrp.bom'].sudo().create(new_bom)

        #Add new product to current sale order
        order_line = {
            'order_id': self._context['active_id'],
            'product_id': product.product_variant_id.id,
        }
        order = self.env['sale.order.line'].sudo().create(order_line)
        self.env['sale.order'].browse(self._context['active_id']).order_line += order
