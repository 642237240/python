import wx
import wx.lib.imagebrowser as imagebrowser


if __name__ == '__main__':
    app = wx.App()
    dialog = imagebrowser.ImageDialog(None)
    ret =  dialog.ShowModal()
    if ret == wx.ID_OK:
        print('You Selected File:' + dialog.GetFile())
    dialog.Destroy()