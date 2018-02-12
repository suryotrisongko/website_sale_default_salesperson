# -*- coding: utf-8 -*-

from odoo import api, models
from odoo.http import request

class Website(models.Model):
    _inherit = 'website'

    @api.multi
    def _prepare_sale_order_values(self, partner, pricelist):
        self.ensure_one()
        affiliate_id = request.session.get('affiliate_id')
        salesperson_id = affiliate_id if self.env['res.users'].sudo().browse(affiliate_id).exists() else request.website.salesperson_id.id
        addr = partner.address_get(['delivery', 'invoice'])
        default_user_id = partner.parent_id.user_id.id or partner.user_id.id

        if self.env.context.get('uid'):
            defaultsales = self.env.context.get('uid')
        else:
            defaultsales = salesperson_id or self.salesperson_id.id or default_user_id

        values = {
            'partner_id': partner.id,
            'pricelist_id': pricelist.id,
            'payment_term_id': self.sale_get_payment_term(partner),
            'team_id': self.salesteam_id.id,
            'partner_invoice_id': addr['invoice'],
            'partner_shipping_id': addr['delivery'],
            'user_id': defaultsales,
        }

        company = self.company_id or pricelist.company_id
        if company:
            values['company_id'] = company.id

        return values
