# -*- coding: utf-8 -*-

from odoo import api, models
from odoo.exceptions import UserError

import logging

_logger = logging.getLogger(__name__)

class ReportLocationCalculate(models.AbstractModel):
    _name = 'report.location_calculate.report_location'

    @api.model
    def render_html(self, docids, data=None):
        self.model = self.env.context.get('active_model')
        docs = self.env[self.model].browse(self.env.context.get('active_id'))
        location_group = docs.location_ids
        location_detail = []
        for location in location_group.location_in_ids:
            # _logger.critical(location.name)
            location_detail.append(location)

        docargs = {
            'doc_ids': self.ids,
            'doc_model': self.model,
            'docs': docs,
            'quality':docs.quality,
            'locations': location_group,
            'location_detail': location_detail,
        }
        return self.env['report'].render('location_calculate.report_location', docargs)
