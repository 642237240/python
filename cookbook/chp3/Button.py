import wx
import wx.lib.platebtn as pbtn
import wx.lib.agw.gradientbutton as gbtn

class MyFrame(wx.Frame):
    def __init__(self, parent, *args, **kwagrs):
        super(MyFrame, self).__init__(parent, *args, **kwagrs)
        self.panel = MyPanel(self)

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        # attibutes
        #make a toggleButton
        self.toggle = wx.ToggleButton(self, label="Toggle Button")

        #make a bitmapButton
        bmp = wx.Bitmap('../image/play_hover.png', wx.BITMAP_TYPE_PNG)
        self.bmpbtn = wx.BitmapButton(self, bitmap=bmp)
        
        # make a few plateButton variants
        self.pbtn1 = pbtn.PlateButton(self, label='PlateButton')
        self.pbtn2 = pbtn.PlateButton(self, label='PlateBmp', bmp=bmp)

        style = pbtn.PB_STYLE_SQUARE
        self.pbtn3 = pbtn.PlateButton(self, label='Square Plate', bmp=bmp, style=style)
        self.pbtn4 = pbtn.PlateButton(self, label='PlateMenu')

        menu = wx.Menu()
        menu.Append(wx.NewId(), item="Hello World")
        self.pbtn4.SetMenu(menu)

        # Gradient BUttons
        self.gbtn1 = gbtn.GradientButton(self, label='GradientBtn')
        self.gbtn2 = gbtn.GradientButton(self, label='GradientBmp', bitmap=bmp)

        # layout
        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.toggle, 0, wx.ALL, 5)
        vsizer.Add(self.bmpbtn, 0, wx.ALL, 5)
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.AddMany([(self.pbtn1, 0, wx.ALL, 5),
                        (self.pbtn2, 0, wx.ALL, 5),
                        (self.pbtn3, 0, wx.ALL, 5),
                        (self.pbtn4, 0, wx.ALL, 5)])
        vsizer.Add(hsizer1, 0, wx.ALL, 12)
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2.AddMany([(self.gbtn1, 0, wx.ALL, 5),
                        (self.gbtn2, 0, wx.ALL, 5)])
        vsizer.Add(hsizer2, 0, wx.ALL, 12)
        
        #make some buttons
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        for bid in (wx.ID_OK, wx.ID_CANCEL, wx.ID_APPLY, wx.ID_HELP):
            button = wx.Button(self, bid)
            sizer.Add(button, 0, wx.ALL, 5)
        vsizer.Add(sizer, 0, wx.ALL, 12)
        self.SetSizer(vsizer)

if __name__ == '__main__':
    app = wx.App()
    MyFrame(None).Show()
    app.MainLoop()

