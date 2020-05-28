import wx

class MouseFrame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(MouseFrame, self).__init__(parent, *args, **kwargs)
        
        #Attributes
        self.panel = wx.Panel(self)
        self.btn = wx.Button(self.panel)

        #event handlers
        self.panel.Bind(wx.EVT_ENTER_WINDOW, self.OnEnter)
        self.panel.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeave)
        self.panel.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.panel.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)

    def OnEnter(self, event):
        '''Called when the mouse enters the panel'''
        self.btn.SetForegroundColour(wx.BLACK)
        self.btn.SetLabel("EVT_ENTER_WINDOW")
        self.btn.SetInitialSize()
    
    def OnLeave(self, event):
        '''Called when the mouse leaves the panel'''
        self.btn.SetLabel("EVT_LEAVE_WINDOW")
        self.btn.SetForegroundColour(wx.RED)
    
    def OnLeftDown(self, event):
        '''called for left down clicks on the panel'''
        self.btn.SetLabel("EVT_LEFT_DOWN")

    def OnLeftUp(self, event):
        '''called for left clicks on hte panel'''
        position = event.GetPosition()
        self.btn.SetLabel('EVT_LEFT_UP')

        #move the button
        self.btn.SetPosition(position - (25, 25))

if __name__ == "__main__":
    app = wx.App()
    MouseFrame(None).Show()
    app.MainLoop()
