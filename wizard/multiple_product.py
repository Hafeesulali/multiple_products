from odoo import models, fields


class MultipleProduct(models.TransientModel):
    _name = "multiple.product"
    _description = "Multiple Products"

    product_ids = fields.Many2many("product.product")

    def action_add_product(self):
        if self._context.get('active_model') == 'sale.order':
            self.env['sale.order'].browse(self._context.get('active_ids')).update({
                'order_line': [(fields.Command.create({
                    'product_id': record.id
                })) for record in self.product_ids]
            })
        else:
            self.env['purchase.order'].browse(self._context.get('active_ids')).update({
                'order_line': [(fields.Command.create({
                    'product_id': record.id
                })) for record in self.product_ids]
            })
