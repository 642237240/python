import wx


if __name__ == '__main__':
    app = wx.App()
    dialog = wx.DirDialog(None, "Choose a directory:", 
        style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
    ret = dialog.ShowModal()
    if ret == wx.ID_OK:
        print(dialog.GetPath())
    
    dialog.Destroy()

    ret = wx.DirSelector("Dir selector function", '', style=wx.DD_DEFAULT_STYLE|wx.DD_NEW_DIR_BUTTON)
    if ret != '':
        print(ret)
    else:
        print('not select or press cancel')