import wx

#------------Notebook start-------------------
'''
wx.NoteBook的样式：
    wx.NB_BOTTOM：tab放在控制区的下面
    wx.NB_LEFT：tab放在控制区的左边
    wx.NB_RIGHT：tab放在控制区的右边
    wx.NB_TOP：tab放在控制区的上边，默认
    wx.NB_FIXEDWIDTH：所有tab相同大小
    wx.NB_MULTILINE：允许多行tab
    wx.NB_NOPAGETHEME：使用纯色的标签
事件：
    wx.EVT_NOTEBOOK_PAGE_CHANGING：page选择即将改变时触发
    wx.EVT_NOTEBOOK_PAGE_CHANGED：page选择正在改变时触发
'''
class NotebookFrame(wx.Frame):
    def __init__(self, parent, *args, **kwagrs):
        super(NotebookFrame, self).__init__(parent, *args, **kwagrs)
        #Attibutes
        self.ntbk = ntbk = wx.Notebook(self)

        ntbk.textctrl = wx.TextCtrl(ntbk, value='edit me', style=wx.TE_MULTILINE)
        ntbk.blue = wx.Panel(ntbk)
        ntbk.blue.SetBackgroundColour(wx.BLUE)
        ntbk.fbrowser = wx.GenericDirCtrl(ntbk)

        # Snetup
        ntbk.AddPage(ntbk.textctrl, 'Text Editor')
        ntbk.AddPage(ntbk.blue, 'Blue Panel')
        ntbk.AddPage(ntbk.fbrowser, 'File Browser')

    

        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChanging)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnPageChanged)
        self.CreateStatusBar()
    
    def OnPageChanging(self, event):
        event.Veto()
        self.PushStatusText('Changing event is fired')

    def OnPageChanged(self, event):
        event.Veto()
        self.PushStatusText('Changed event is fired')

#------------Notebook end----------------------


if __name__ == '__main__':
    app = wx.App()
    NotebookFrame(None).Show()
    app.MainLoop()
