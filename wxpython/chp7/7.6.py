import wx
import wx.lib.buttons as buttons


class GenericButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Generic Button Example', size=(500, 300))
        panel = wx.Panel(self, -1)

        sizer = wx.FlexGridSizer(3, 20, 20)
        b = wx.Button(panel, -1, "A wx.Button")
        b.SetDefault()
        sizer.Add(b)

        b = wx.Button(panel, -1, "non-default wx.Button")
        sizer.Add(b)
        sizer.Add(10, 10)

        b = buttons.GenButton(panel, -1, 'Generic Button')
        sizer.Add(b)

        b = buttons.GenButton(panel, -1, "disabled Generic")
        b.Enable(False)
        sizer.Add(b)


if __name__ == "__main__":
    app = wx.App()
    frame = GenericButtonFrame()
    frame.Show()
    app.MainLoop()
