import wx

#------------ListCtrl start-------------------
'''

'''
class TaskBarIconFrame(wx.Frame):
    def __init__(self, parent, *args, **kwagrs):
        super(TaskBarIconFrame, self).__init__(parent, *args, **kwagrs)
        #Attibutes
        self.panel = TaskBarIconPanel(self)
        self.CreateStatusBar()

class TaskBarIconPanel(wx.Panel):
    def __init__(self, parent):
        super(TaskBarIconPanel, self).__init__(parent)

        # attibutes
        self.lstc = MyListCtrl(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.lstc, 1, wx.EXPAND)
        self.SetSizer(sizer)

        # event handlers

class CustomTaskBarIcon(wx.TaskBarIcon):
    ID_HELLO = wx.NewIdRef()
    ID_HELLO2 = wx.NewIdRef()
    def __init__(self, parent):
        super(CustomTaskBarIcon, self).__init__(parent)

        #setup
        icon = wx.Icon('../image/search.png', wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)

        # Event Handlers
        self.Bind(wx.EVT_MENU, self.OnMenu)

    def CreatePopupMenu(self):
        '''Base class virtual method for creating the pop menu for the icon.'''
        menu = wx.Menu()
        menu.Append(CustomTaskBarIcon.ID_HELLO, 'Hello')
        menu.Append(CustomTaskBarIcon.ID_HELLO2, 'Hi!')
        menu.AppendSeparator()
        menu.Append(wx.ID_CLOSE, 'Exit')
        return menu
    
    def OnMenu(self, event):
        evt_id = event.GetId()
        if evt_id == CustomTaskBarIcon.ID_HELLO:
            wx.MessageBox('Hello World!', 'hello')
        elif evt_id == CustomTaskBarIcon.ID_HELLO2:
            wx.MessageBox('Hi Again', 'Hi!')
        elif evt_id == wx.ID_CLOSE:
            self.Destroy()
        else:
            event.Skip()



#------------ListCtrl end------------------- --       

if __name__ == '__main__':
    app = wx.App()
    TaskBarIconFrame(None).Show()
    app.MainLoop()
