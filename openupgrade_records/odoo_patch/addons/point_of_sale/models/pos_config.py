from odoo import api
from odoo.addons.point_of_sale.models.pos_config import PosConfig
from odoo.addons.openupgrade_records.odoo_patch.odoo_patch import OdooPatch


class PostInstallPosLocalisationPatch(OdooPatch):
    target = PosConfig
    method_names = ['post_install_pos_localisation']

    @api.model
    def post_install_pos_localisation(self, companies=False):
        """ Don't create duplicate journals etc. on reinstall """
        pass
