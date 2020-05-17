import wx

#from blockwindow import BlockWindow

labels = 'one two three four five six seven eight nine'.split()

class GridSizerFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Basic Grid Sizer')
        p = wx.Panel(self)
        sizer = wx.GridSizer(rows=3, cols=3, hgap=5, vgap=5)
        for label in labels:
            bw = wx.Button(p, label=label)
            sizer.Add(bw, 0, 0)
        
        self.SetSizer(sizer)
        self.Fit()
    
if __name__ == '__main__':
    app = wx.App()
    GridSizerFrame().Show()
    app.MainLoop()
