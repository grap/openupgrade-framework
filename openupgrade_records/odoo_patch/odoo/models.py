from odoo import api, models
from odoo.addons.openupgrade_records.odoo_patch.odoo_patch import OdooPatch
from odoo.addons.openupgrade_records import openupgrade_log
from odoo.models import BaseModel


class BaseModelPatch(OdooPatch):
    target = models.BaseModel
    method_names = ['_convert_records']

    @api.model
    def _convert_records(self, records, log=lambda a: None):
        """ Log data ids that are imported with `load` """
        current_module = self.env.context['module']
        for res in BaseModelPatch._convert_records._original_method(
                self, records, log=log):
            _id, xid, _record, _info = res
            if xid:
                xid = xid if '.' in xid else "%s.%s" % (current_module, xid)
                openupgrade_log.log_xml_id(self.env.cr, current_module, xid)

            yield res
