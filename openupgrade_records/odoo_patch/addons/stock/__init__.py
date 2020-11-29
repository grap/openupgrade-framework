from odoo.addons import stock
from odoo.addons.openupgrade_records.odoo_patch.odoo_patch import OdooPatch


class PreInitHookPatch(OdooPatch):
    target = stock
    method_names = ['pre_init_hook']

    def pre_init_hook(cr):
        """ Don't unlink stock data on reinstall """
        pass
