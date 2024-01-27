# -*- coding: utf-8 -*-
import re
from odoo.exceptions import UserError, RedirectWarning, ValidationError
from odoo import api, fields, models
from datetime import datetime
from itertools import groupby

class StockPicking(models.Model):
    _inherit = 'stock.picking'


    def _default_lote(self):
        valor =  fields.Date.today().strftime("%y%m%d")

        self.lote_recepcion = valor;
        return valor;

    lote_recepcion = fields.Char("Lote de recepción",compute =_default_lote, readonly = False, store = True, default= _default_lote )

    def aplica_lote_recepcion(self):
        None;
        obj_lot = self.env["stock.lot"]
        for picking in self:

            for move in picking.move_ids_without_package:
                arr_lote = obj_lot.search([("name", "=", self.lote_recepcion), ("product_id", "=", move.product_id.id)])
                if len(arr_lote) > 0:
                    lote = arr_lote[0]
                else:
                    lote = obj_lot.create({
                        "name": self.lote_recepcion,
                        "product_id" : move.product_id.id
                    })

                #Coloca el lote a las lineas
                if len(move.move_line_ids) > 0:
                    for line in move.move_line_ids:
                        line.lot_name = lote.name
                        line.lot_id = lote.id
                        #line.reserved_qty = move.product_uom_qty;
                        line.qty_done = move.product_uom_qty;
                else:
                    move.move_line_ids.create({
                        "lot_name" : lote.name,
                        "location_dest_id" : picking.location_dest_id.id,
                        "lot_id" : lote.id,
                        "qty_done" : move.product_uom_qty
                    })

                move.lot_ids = lote;

