from odoo import models, fields


class ResConfigSettings(models.Model):
    _inherit = "res.config.settings"

    ncf_validation_target = fields.Selection(
        related="company_id.ncf_validation_target",
        readonly=False,
    )
