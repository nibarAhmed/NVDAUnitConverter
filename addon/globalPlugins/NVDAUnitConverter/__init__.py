# NVDA unit converter
# copyright 2023 Nibar Ahmed. Licensed under GPLv2.

import globalPluginHandler
import scriptHandler
import tones
from . import UI
import wx
import logging
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    log = logging.getLogger("nvda")
    @scriptHandler.script(
        gesture="kb:NVDA+shift+U",
        description="Launches the unit converter."
        )
    def script_launch(self, gesture):
        #only one instance of the addon is allowed to run.
        if wx.FindWindowByName("NVDAUnitConverter") is None:
            self.ui=UI.UI(None, title="NVDAUnitConverter", name="NVDAUnitConverter")
            #self.log.info("This is a message written to the NVDA log.")
            self.ui.Show(True)
    def terminate(self):
        self.ui.Close()
        super().terminate()