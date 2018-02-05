# -*- coding: utf-8 -*-

from odoo import models, fields, api

class location_calculate(models.TransientModel):
    _name = 'locationcalculate.wizard'

    location_ids = fields.Many2one('groups.location', string="Location", required=True)
    quality = fields.Boolean(default=False)

    @api.multi
    def check_report(self):
        data = {}
        data['form'] = self.read(['location_ids','quality'])
        return self._print_report(data)

    def _print_report(self, data):
        # data['form'].update(self.read(['location_ids']))
        # _logger.critical("Entre al _ptint")
        return self.env['report'].get_action(self,'location_calculate.report_location',data=data)
