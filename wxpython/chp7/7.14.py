import wx


class ChoiceFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Choice Example", size=(250, 200))
        panel = wx.Panel(self, -1)
        sampleList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
            'seven', 'eight']
        wx.StaticText(panel, -1, "Select one:", (15, 20))
        ch = wx.Choice(panel, -1, (85, 18), choices=sampleList)
        ch.SetSelection(1)


if __name__ == "__main__":
    app = wx.App()
    ChoiceFrame().Show()
    app.MainLoop()
