from nautobot.extras.plugins import PluginTemplateExtension
from django.conf import settings
from packaging import version

# NETBOX_CURRENT_VERSION = version.parse(settings.VERSION)
NAUTOBOT_CURRENT_VERSION = version.parse(settings.VERSION)


class SiteTopologyButtons(PluginTemplateExtension):
    """
    Extend the DCIM site template to include content from this plugin.
    """
    model = 'dcim.site'

    def buttons(self):
        # if NETBOX_CURRENT_VERSION >= version.parse("3.0"):
        if NAUTOBOT_CURRENT_VERSION >= version.parse("1.2"):
            # return self.render('nautobot_diagrams/site_topo_button_3.x.html') # original from nextbox_ui_plugin
            return self.render('nautobot_diagrams/site_topo_button.html')
        # else:
            # NZE: kept them from the original source just in case
            # any compatibility issues or behavior changes are encountered due to different versions.
            # return self.render('nautobot_diagrams/site_topo_button_3.x.html')
            # return self.render('nautobot_diagrams/site_topo_button.html')  # original from nextbox_ui_plugin

# PluginTemplateExtension subclasses must be packaged into an iterable named
# template_extensions to be imported by NetBox.
template_extensions = [SiteTopologyButtons]