from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Tambahkan field-field yang diperlukan di sini

    def create_purchase_order(self):
        for order in self:
            if order.with_po:
                # Logic untuk membuat PO
                print("test")
            else:
                raise UserError(_("You cannot create a PO without 'With PO' set to True."))

