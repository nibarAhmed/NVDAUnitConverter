from . import Converter
from . import Unit
import wx
import string
import winsound
class UI(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.SetWindowStyle(wx.SYSTEM_MENU)
        self.mainPanel=wx.Panel(self)
        #this is the panel sizer where items will be added. 
        self.panelSizer=wx.BoxSizer(wx.VERTICAL)
        #the next sizer is for the combo box and the label.
        self.comboSizer=wx.BoxSizer(wx.HORIZONTAL)
        #this sizer is for the edit boxes and button to convert as well as a cansel button. 
        self.editSizer=wx.BoxSizer(wx.HORIZONTAL)        
        self.buttonsSizer=wx.BoxSizer(wx.HORIZONTAL)        
        #this sizer is for the window in order to allow the panel to fit in the window.
        self.windowSizer=wx.BoxSizer(wx.HORIZONTAL)
        self.comboLabelText="select what to convert"
        self.comboLabel=wx.StaticText(self.mainPanel, label=self.comboLabelText)
        self.comboBox=wx.ComboBox(self.mainPanel, style=wx.CB_READONLY, choices=Unit.Unit.getAllValues())
        self.comboBox.Bind(wx.EVT_COMBOBOX, self.onSelect)
        self.choice=None
        #remove this later
        self.comboLabel.SetBackgroundColour("white")
        self.comboBox.SetBackgroundColour("white")
        self.userInputLabelStr="convert from "
        self.userInputLabel=wx.StaticText(self.mainPanel, label=self.userInputLabelStr)
        self.userInput=wx.TextCtrl(self.mainPanel, style=wx.TE_PROCESS_ENTER)
        self.userInput.Bind(wx.EVT_CHAR, self.onKeyPressed)
        self.userInput.Bind(wx.EVT_TEXT_ENTER, self.onEnterPressed)
        self.userInput.SetBackgroundColour("white")
        self.userInputLabel.SetBackgroundColour("white")
        self.convertBtn=wx.Button(self.mainPanel, label="Convert")
        self.convertBtn.Bind(wx.EVT_BUTTON, self.onEnterPressed)
        self.closeBtn=wx.Button(self.mainPanel, label="Close")
        self.closeBtn.Bind(wx.EVT_BUTTON, self.onClosePressed)
        self.resultDialog=wx.MessageDialog(self, "result", "result", wx.OK)
        self.comboSizer.Add(self.comboLabel, proportion=0, flag=wx.RIGHT, border=10)
        self.comboSizer.Add(self.comboBox, proportion=2)
        self.panelSizer.Add(self.comboSizer, proportion=0, flag=wx.TOP|wx.EXPAND, border=40)
        self.editSizer.Add(self.userInputLabel, proportion=0, flag=wx.Right, border=10)
        self.editSizer.Add(self.userInput, proportion=2)
        self.buttonsSizer.Add(self.convertBtn, proportion=0)
        # just a spacer for the buttons so one is at the far left and one is at the far right. 150 is a constent that I set by just looking at the window. a smart choice will be to calculate the windows width minus both button widths
        self.buttonsSizer.Add((150,0), proportion=1)
        self.buttonsSizer.Add(self.closeBtn, proportion=0)
        self.panelSizer.Add(self.editSizer, proportion=0, flag=wx.TOP|wx.EXPAND, border=10)
        self.panelSizer.Add(self.buttonsSizer, proportion=0, flag=wx.TOP|wx.EXPAND, border=30)
        self.mainPanel.SetSizer(self.panelSizer)
        self.windowSizer.Add(self.mainPanel, proportion=1, flag=wx.EXPAND, border=30)
        self.SetSizerAndFit(self.windowSizer)
        self.SetBackgroundColour("black")
        self.Center()
    #this function checks weather the key that was just pressed is numeric or not. If it is numeric then the event is skipped and the user can continue typing.
    def onKeyPressed(self, event):
        keyCode=event.GetKeyCode()
        currentValue=self.userInput.GetValue()
        if chr(keyCode) in string.digits:
            event.Skip()
        #allow keys that are not printable but special such as arrows and so on.
        elif chr(keyCode) not in string.printable:
            event.Skip()
        #allow for negative numbers.
        elif chr(keyCode)=='-':
            if currentValue!="":
                if currentValue[0]=='-':
                    self.userInput.SetValue('-'+currentValue)
            else:
                event.Skip()
        #allow floats
        elif chr(keyCode)=='.' and '.' not in currentValue:
            event.Skip()
        elif chr(keyCode)=='\t':
            event.Skip()
        else:
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
    #this function performs the conversion when enter or the convert button is pressed and then shows a message dialog containing the result.
    def onEnterPressed(self, event):
        result=Converter.Converter.convert(self.choice, float(self.userInput.GetValue()))
        self.resultDialog.SetMessage(str(result))
        self.resultDialog.ShowModal()
    def onClosePressed(self, event):
        self.Close()
    def onSelect(self, event):
        self.choice=event.GetString()