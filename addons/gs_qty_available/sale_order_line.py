from openerp.osv import fields, osv
from openerp import netsvc, tools, pooler
import openerp.addons.decimal_precision as dp

class sale_order_line(osv.osv):

    _inherit = "sale.order.line"

    _columns = {
        'qty_available': fields.float('Qty Disponible',digits_compute= dp.get_precision('Product UoS')),
    }    

sale_order_line()