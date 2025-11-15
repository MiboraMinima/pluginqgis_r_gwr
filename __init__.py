def classFactory(iface):
    from .gwr_plugin_r import GWRPlugin
    return GWRPlugin(iface)