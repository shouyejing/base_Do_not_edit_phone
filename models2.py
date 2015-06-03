from openerp import models, fields, api, exceptions, _


class Category(models.Model):
    _inherit = 'product.category'

    level = fields.Integer(compute='_compute_level', store=True)

    @api.one
    @api.depends('parent_id')
    def _compute_level(self):
        if not self.parent_id:
            self.level = 1
        else:
            self.level = self.parent_id.level + 1