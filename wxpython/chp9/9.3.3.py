import wx


if __name__ == '__main__':
    app = wx.App()
    app.MainLoop()
    ret = wx.GetNumberFromUser("Get number from user:", 'prompt',"Get number function", 10, min=-10, max=100)
    if ret == -1:
        print('press cancel.')
    else:
        print('press ok, input number %d' % ret)
