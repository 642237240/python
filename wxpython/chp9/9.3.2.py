import wx


if __name__ == '__main__':
    app = wx.App()
    app.MainLoop()
    ret = wx.GetPasswordFromUser("Get password from user:", "Get password function", "default")
    if ret == '':
        print('press cancel or input none')
    else:
        print('press ok, input string: %s' % ret)
