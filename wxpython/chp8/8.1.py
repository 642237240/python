import wx


if __name__ = "__main__":
    app = wx.App()
    frame = wx.Frame(None, -1, "A Frame", size=(200, 100), 
        style=wx.DEFAULT_FRAME_STYLE)
    frame.Show()
    app.MainLoop()
