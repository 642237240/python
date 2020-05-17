import wx


if __name__ == "__main__":
    app = wx.App()
    dlg = wx.MessageDialog(None, 'Is this explanation OK?', 'A Message Box',
        wx.YES_NO| wx.ICON_QUESTION)
    retCode = dlg.ShowModal()
    if retCode == wx.ID_YES:
        print('yes')
    elif retCode == wx.ID_NO:
        print('no')
    elif retCode == wx.ID_OK:
        print('ok')
    else:
        print('cancel')
    
    dlg.Destroy()

    retCode = wx.MessageBox('Is this way easier?', 'Via Function', wx.YES_NO | wx.ICON_QUESTION)
    if retCode == wx.YES:
        print('yes')
    elif retCode == wx.NO:
        print('no')
    elif retCode == wx.OK:
        print('ok')
    else:
        print('cancel')