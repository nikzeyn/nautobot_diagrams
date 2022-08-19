"""nautobot_diagrams Plugin Initilization."""
# __version__ = '0.1.4'


from nautobot.extras.plugins import PluginConfig


class NautobotDiagramsConfig(PluginConfig):
    """Plugin configuration for the nautobot_diagrams plugin."""

    name = "nautobot_diagrams"  # Raw plugin name; same as the plugin's source directory.
    verbose_name = "Nautobot Diagrams"  # Human-friendly name for the plugin.
    description = 'A plugin for Nautobot to generate network diagrams.'
    version = '0.1.4'
    author = 'Nik Zeynalov'
    author_email = 'Nik.Zeynalov@originenergy.com.au'
    base_url = "nautobot_diagrams"  # (Optional) Base path to use for plugin URLs. Defaulting to app_name.
    required_settings = []  # A list of any configuration parameters that must be defined by the user.
    min_version = "1.0.0"  # Minimum version of Nautobot with which the plugin is compatible.
    max_version = "1.999"  # Maximum version of Nautobot with which the plugin is compatible.
    default_settings = {}  # A dictionary of configuration parameters and their default values.
    caching_config = {}  # Plugin-specific cache configuration.


config = NautobotDiagramsConfig