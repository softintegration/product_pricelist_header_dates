# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Pricelist(models.Model):
    _inherit = "product.pricelist"

    date_start = fields.Datetime('Start Date', help="Starting datetime will be applied on all items")
    date_end = fields.Datetime('End Date', help="Ending datetime will be applied on all items")


    @api.onchange('date_start')
    def on_change_date_start(self):
        if self.date_start:
            item_ids = self.item_ids
            for item in item_ids:
                item.date_start = self.date_start
            self.item_ids = item_ids

    @api.onchange('date_end')
    def on_change_date_end(self):
        if self.date_end:
            item_ids = self.item_ids
            for item in item_ids:
                item.date_end = self.date_end
            self.item_ids = item_ids
