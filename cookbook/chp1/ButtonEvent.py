import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, 
        pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, name='MyFrame'):
        wx.Frame.__init__(self, parent, id=id, title=title, pos=pos, size=size, style=style, name=name)

        # Atritutes
        self.panel = wx.Panel(self)

        self.btn1 = wx.Button(self.panel, label="Push Me")
        self.btn2 = wx.Button(self.panel, label='push me too')

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.btn1, 0, wx.ALL, 0)
        sizer.Add(self.btn2, 0, wx.ALL, 0)
        self.panel.SetSizer(sizer)

        self.Bind(wx.EVT_BUTTON, self.OnButton, self.btn1)
        self.Bind(wx.EVT_BUTTON, 
            lambda event:self.btn1.Enable(not self.btn1.Enabled), #lambda arg: expression（只能是一行）
            self.btn2)
        
    def OnButton(self, event):
        """Called when self.btn1 is clicked"""
        event_id = event.GetId()
        event_obj = event.GetEventObject()
        print('Button 1 Clicked:')
        print('ID=%d' % event_id)
        print('object=%s' % event_obj.GetLabel())

if __name__ == '__main__':
    app = wx.App()
    MyFrame(None).Show()
    app.MainLoop()

