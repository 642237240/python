import wx


if __name__ == '__main__':
    app = wx.App()
    app.MainLoop()
    dialog = wx.TextEntryDialog(None, 'What kind of text would you like to enter?', 
        'Text Entry', 'Default Value', style=wx.CANCEL |wx.OK|wx.CENTER|wx.TE_CENTER)
    dialog.SetValue("please input:")
    ret = dialog.ShowModal()
    if ret == wx.ID_OK:
        print("You entered: %s" % dialog.GetValue())
    elif ret == wx.ID_CANCEL:
        print("you canel enter %s" % dialog.GetValue())


    dialog.Destroy()