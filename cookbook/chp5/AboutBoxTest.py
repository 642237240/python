import wx
import sys

'''

'''

class AboutBoxDialogFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(parent)

        # Attributes
        self.panel = wx.Panel(self)

        # Setup Menu
        menubar = wx.MenuBar()
        helpmenu = wx.Menu()
        helpmenu.Append(wx.ID_ABOUT, 'About')
        menubar.Append(helpmenu, 'Help')
        self.SetMenuBar(menubar)

        # Setup StatusBar
        self.CreateStatusBar()
        self.PushStatusText('See About int the Menu')

        # Event Handlers
        self.Bind(wx.EVT_MENU, self.OnAbout, id=wx.ID_ABOUT)

    def OnAbout(self, event):
        '''Show the about dialog'''
        info = wx.AboutDialogInfo()

if __name__ == '__main__':
    app = wx.App()
    MessageBoxFrame(None).Show()
    app.MainLoop()
