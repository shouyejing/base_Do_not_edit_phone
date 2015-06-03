from openerp import models, fields, api, exceptions, _


class Category(models.Model):
    _inherit = 'product.category'

    level = fields.Integer(compute='_compute_level', store=True)

    level2 = fields.Integer(compute='_compute_level2', store=True)

    level3 = fields.Integer(compute='_compute_level3', store=True)

    @api.one
    @api.depends('parent_id')
    def _compute_level(self):
        if not self.parent_id:
            self.level = 1
        else:
            self.level = self.parent_id.level + 1

    @api.one
    @api.depends('parent_id')
    def _compute_level2(self):
        def get_level(cat):
            if not cat.parent_id:
                return 1
            else:
                return get_level(cat.parent_id) + 1
        self.level2 = get_level(self)

    @api.one
    @api.depends('parent_id')
    def _compute_level3(self):
        level = 1
        cat = self
        while cat.parent_id:
            level += 1
            cat = cat.parent_id
        self.level3 = level