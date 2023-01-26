import globalPluginHandler
import scriptHandler
import tones
from . import UI
import wx
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    @scriptHandler.script(gesture="kb:NVDA+I")
    def script_launch(self, gesture):
        ui=UI.UI(None, title="NVDAUnitConverter")
        ui.Show(True)