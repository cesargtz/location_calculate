# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
import pytz

class location_calculate(models.TransientModel):
    _name = 'locationcalculate.wizard'


    def _get_start_date():
        local = pytz.timezone("America/Chihuahua")
        utc = datetime.datetime.strptime(datetime.datetime.now().strftime("2018-10-15 11:00"), "%Y-%m-%d %H:%M")
        local_hr = local.localize(utc, is_dst=None)
        return local_hr

    location_ids = fields.Many2one('groups.location', string="Location", required=True)
    quality = fields.Boolean(default=False, help=""" Incluye los porcentajes de calidad por ubicación, tomando en cuenta
        las recepciones de camión y los traspasos""")
    calculate_tranfer = fields.Boolean(default=False, help="""Toma en cuenta las recepciones,
        las salidas, las traspasos y las salidas de excedentes solo si ya estan transferidos""")
    calculate_clean_kilos = fields.Boolean(default=False, help=""" Hace los calculos basandose en los kilos
        limpios de las recepciones de camión""")
    date_start = fields.Datetime(string="Fecha de Inicio", default=_get_start_date())
    date_end = fields.Datetime(string="Fecha Final")


    @api.multi
    def check_report(self):
        data = {}
        data['form'] = self.read(['location_ids','quality','calculate_tranfer','calculate_clean_kilos','date_start','date_end'])
        return self._print_report(data)

    def _print_report(self, data):
        # data['form'].update(self.read(['location_ids']))
        # _logger.critical("Entre al _ptint")
        return self.env['report'].get_action(self,'location_calculate.report_location',data=data)
