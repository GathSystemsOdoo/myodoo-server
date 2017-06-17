# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) Rooms For (Hong Kong) Limited T/A OSCG (<http://www.openerp-asia.net>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'GathSystems - Show qty_available in Sales Order line',
    'version': '1.0',
    'author': 'GathSystems GbR',
    'website': 'http://www.gathsystems.com',
    'category': 'Sales Management',
    'description': "Show qty_available in Sales Order line - Aktivate Developer Mode -> Open Sales Orders -> Edit FormView -> Add Field qty_available where needed (e.g. after price_unit",
    'data': [
            'sale_order_line.xml',
    ],
    'depends': ['sale', 'stock', 'stock_account'],
    'installable': True,
    'auto_install': False
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
