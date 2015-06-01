from openerp import models, fields, api, exceptions, _


class Partner(models.Model):
    _inherit = 'res.partner'

    has_sale_order = fields.Boolean(compute='_compute_has_sale_order', store=True)

    @api.depends('sale_order_ids')
    @api.one
    def _compute_has_sale_order(self):
        self.has_sale_order = True if self.sale_order_ids else False

    @api.multi
    def write(self, values):
        for record in self:
            editing_phone = True if 'phone' in values.keys() else False
            if editing_phone:
                new_phone = values['phone']
                if record.has_sale_order and editing_phone and new_phone != self.phone:
                    raise exceptions.Warning('You can not edit phone when there is sale order exist. partner id %d'
                                             % record.id)
        super(Partner, self).write(values)
        return True