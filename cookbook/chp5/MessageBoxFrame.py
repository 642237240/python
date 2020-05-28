import wx
'''
wx.MessageBox()的style值：
icons：
    wx.ICON_ERROR：dialog窗口上显示error icon
    wx.ICON_INFORMATION：dialog窗口上显示information icon
    wx.ICON_QUESTION：dialog窗口上显示Question icon
    wx.ICON_WARNING：dislog窗口上显示warning icon
button：
    wx.CANCEL：添加CANCEL按钮到dialog
    wx.OK：添加OK按钮到dialog
    wx.YES：添加YES按钮到dialog
    wx.NO：添加NO按钮
    wx.YES_NO：相当于wx.YES|wx.NO
    wx.YES_DEFAULT：设置YES按钮为默认按钮
    wx.NO_DEFAULT：设置NO按钮为默认按钮
'''

class MessageBoxFrame(wx.Frame):
    def __init__(self, parent):
        super(MessageBoxFrame, self).__init__(parent)

        # Layout
        self.CreateStatusBar()
        self.PushStatusText("Close this window")

        # Event Handlers
        self.Bind(wx.EVT_CLOSE, self.OnClose)
    
    def OnClose(self, event):
        result = wx.MessageBox("Are you sure you want "
                                "to close this window?",
                                style=wx.CENTER|\
                                    wx.ICON_WARNING|\
                                    wx.YES_NO)
        if result == wx.NO:
            event.Veto()    # Veto()方法阻塞框架的close事件
        else:
            event.Skip()

if __name__ == '__main__':
    app = wx.App()
    MessageBoxFrame(None).Show()
    app.MainLoop()
