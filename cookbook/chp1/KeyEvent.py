import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, *args, **kwargs):
        super(MyFrame, self).__init__(parent, *args, **kwargs)

        #attributes
        self.panel = wx.Panel(self)
        self.txtctrl = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)

        #layout
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.txtctrl, 1, wx.EXPAND)
        self.panel.SetSizer(sizer)
        self.CreateStatusBar() # for output display

        # event handlers
        self.txtctrl.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        #self.txtctrl.Bind(wx.EVT_CHAR, self.OnChar)
        #self.txtctrl.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
    
    def OnKeyDown(self, event):
        '''KeyDown event is sent first'''
        print('OnKeyDown Called')
        
        # Get information about the event and log it to the statusbar for display
        key_code = event.GetKeyCode()
        raw_code = event.GetRawKeyCode()
        modifiers = event.GetModifiers()
        msg = 'Key: %d, raw: %d, modifers: %d' % (key_code, raw_code, modifiers)
        self.PushStatusText("KeyDonw: " + msg)
    
    def OnChar(self, event):
        '''The char event comes second and is 
        where the character associated with the
        key is put into the control
        '''
        print('OnChar Called')
        modifiers = event.GetModifiers()
        key_code = event.GetKeyCode()

        if modifiers & wx.MOD_SHIFT:
            wx.Bell()
        elif chr(key_code) in 'aeiou':
            #When a vowel is pressed append a question mark to the end.
            self.txtctrl.AppendText('?')
        else:
            event.Skip()
    
    def OnKeyUp(self, event):
        '''KeyUp comes last'''
        print('OnKeyUp Called')
        event.Skip()


if __name__ == "__main__":
    app = wx.App()
    frm = MyFrame(None)
    frm.Show()
    app.MainLoop()
