# -*- coding: utf-8 -*-

from odoo import models, fields, api

class location_calculate(models.TransientModel):
    _name = 'locationcalculate.wizard'

    location_ids = fields.Many2one('groups.location', string="Location", required=True)
    quality = fields.Boolean(default=False, help=""" Incluye los porcentajes de calidad por ubicación, tomando en cuenta
        las recepciones de camión y los traspasos""")
    calculate_tranfer = fields.Boolean(default=False, help="""Toma en cuenta las recepciones,
        las salidas, las traspasos y las salidas de excedentes solo si ya estan transferidos""")
    calculate_clean_kilos = fields.Boolean(default=False, help=""" Hace los calculos basandose en los kilos
        limpios de las recepciones de camión""")

    @api.multi
    def check_report(self):
        data = {}
        data['form'] = self.read(['location_ids','quality','calculate_tranfer','calculate_clean_kilos'])
        return self._print_report(data)

    def _print_report(self, data):
        # data['form'].update(self.read(['location_ids']))
        # _logger.critical("Entre al _ptint")
        return self.env['report'].get_action(self,'location_calculate.report_location',data=data)
