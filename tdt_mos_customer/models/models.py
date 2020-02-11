# -*- coding: utf-8 -*-
from odoo import models, fields, api
from collections import namedtuple, OrderedDict, defaultdict
from odoo.exceptions import UserError

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    customer_id = fields.Many2one('res.partner', "Customer")

class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

    customer_id = fields.Many2one('res.partner', "Customer",store=True,related='production_id.customer_id')

class StockRule(models.Model):
    _inherit = 'stock.rule'

    def _add_customer(self, vals):
        order_name = vals[0]['origin']
        order = self.env['sale.order'].search([('name', '=', order_name)])
        if order:
            vals[0]['customer_id'] = order.partner_id.id


    #Copied from mrp>models>stock_rule
    def _run_manufacture(self, procurements):
        productions_values_by_company = defaultdict(list)
        for procurement, rule in procurements:
            bom = self._get_matching_bom(procurement.product_id, procurement.company_id, procurement.values)
            if not bom:
                msg = _('There is no Bill of Material of type manufacture or kit found for the product %s. Please define a Bill of Material for this product.') % (procurement.product_id.display_name,)
                raise UserError(msg)

            productions_values_by_company[procurement.company_id.id].append(rule._prepare_mo_vals(*procurement, bom))

        for company_id, productions_values in productions_values_by_company.items():
            # create the MO as SUPERUSER because the current user may not have the rights to do it (mto product launched by a sale for example)
            self._add_customer(productions_values) #This is the only custom line
            productions = self.env['mrp.production'].sudo().with_context(force_company=company_id).create(productions_values)
            self.env['stock.move'].sudo().create(productions._get_moves_raw_values())
            productions.action_confirm()

            for production in productions:
                origin_production = production.move_dest_ids and production.move_dest_ids[0].raw_material_production_id or False
                orderpoint = production.orderpoint_id
                if orderpoint:
                    production.message_post_with_view('mail.message_origin_link',
                                                    values={'self': production, 'origin': orderpoint},
                                                    subtype_id=self.env.ref('mail.mt_note').id)
                if origin_production:
                    production.message_post_with_view('mail.message_origin_link',
                                                    values={'self': production, 'origin': origin_production},
                                                    subtype_id=self.env.ref('mail.mt_note').id)
        return True
