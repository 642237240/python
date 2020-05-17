import wx


if __name__ == '__main__':
    app = wx.App()
    app.MainLoop()
    wx.FileSelector('File selector function', '', '123.py', 'py', 
        wildcard='all file(*.*)|*.*|python file(*.py)|*.py|c file(*.c)|*.c',flags=wx.FD_SAVE)
