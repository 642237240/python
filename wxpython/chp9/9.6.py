import wx
import os


if __name__ == '__main__':
    app = wx.App()
    wildcard = 'Python source(*.py)|*.py|'\
        'Compile Python(*.pyc)|*.pyc|'\
        'All files(*.*)|*.*'
    dialog = wx.FileDialog(None, 'Choose a file', os.getcwd(),'', wildcard, wx.FD_MULTIPLE)
    dialog.SetFilterIndex(1)
    ret = dialog.ShowModal()
    if ret == wx.ID_OK:
        print(dialog.GetPath())
    
    dialog.Destroy()
