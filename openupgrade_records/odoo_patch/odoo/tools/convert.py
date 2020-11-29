from odoo.addons.openupgrade_records.odoo_patch.odoo_patch import OdooPatch
from odoo.addons.openupgrade_records import openupgrade_log
from odoo.tools.convert import xml_import


class XMLImportPatch(OdooPatch):
    target = xml_import
    method_names = ['_test_xml_id']

    def _test_xml_id(self, xml_id):
        res = XMLImportPatch._test_xml_id._original_method(self, xml_id)
        openupgrade_log.log_xml_id(self.env.cr, self.module, xml_id)
        return res
