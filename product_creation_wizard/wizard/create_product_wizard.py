from odoo import models, fields, api

class ProductCreateWizard(models.TransientModel):
    _name = "product.create_wizard"

    base_material = fields.Many2one('product.template', "Base Material")
    name = fields.Char("Name")
    conversion = fields.Float("Conversion")

    def create_product(self):
        #New Product Creation
        routes = self.env['stock.location.route'].search([('name', 'in', ['Replenish on Order (MTO)', 'Manufacture'])])
        new_prod = {
            'name': self.name,
            'route_ids': routes.ids,
            'categ_id': self.base_material.categ_id.id
        }
        product = self.env['product.template'].create(new_prod)

        #Create BoM
        new_bom = {
            'product_tmpl_id': product.id,
        }
        bom = self.env['mrp.bom'].create(new_bom)
        bom_line = {
            'product_id': self.base_material.id,
            'product_qty': self.conversion,
            'bom_id': bom.id
        }
        line = self.env['mrp.bom.line'].create(bom_line)
