import wx


if __name__ == '__main__':
    app = wx.App()
    app.MainLoop()
    ret = wx.GetTextFromUser("Get text from user:", "Get Text function", "default")
    if ret == '':
        print('press cancel or input none')
    else:
        print('press ok')
