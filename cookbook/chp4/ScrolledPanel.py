import wx
import wx.lib.scrolledpanel as scrolledpanel

#------------ScrolledPanel start-------------------
'''
ScrolledPanel控件用于显示一个bitmap列表，可以使用scroll查看bitmap列表
'''
class ScrolledPanelFrame(wx.Frame):
    def __init__(self, parent):
        super(ScrolledPanelFrame, self).__init__(parent)

        # Attributes
        self.panel = None

        # Setup
        bitmaps = list()
        bmp = wx.Bitmap("../image/bitmap/ab-1.png", wx.BITMAP_TYPE_PNG)
        bitmaps.append(bmp)
        bmp = wx.Bitmap("../image/bitmap/ab-2.png", wx.BITMAP_TYPE_PNG)
        bitmaps.append(bmp)
        bmp = wx.Bitmap("../image/bitmap/ab-3.png", wx.BITMAP_TYPE_PNG)
        bitmaps.append(bmp)
        self.panel = ImageListCtrl(self, bitmaps)

class ImageListCtrl(wx.lib.scrolledpanel.ScrolledPanel):
    '''Simple control to display a list of images'''
    def __init__(self, parent, bitmaps=list(), style=wx.TAB_TRAVERSAL|wx.BORDER_SUNKEN):
        super(ImageListCtrl, self).__init__(parent, style=style)

        #Attibutes
        self.images = list()
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Setup
        for bmp in bitmaps:
            self.AppendBitmap(bmp)
        self.SetSizer(self.sizer)

    def AppendBitmap(self, bmp):
        '''Add another bitmap to the control'''
        self.images.append(bmp)
        sbmp = wx.StaticBitmap(self, bitmap=bmp)
        self.sizer.Add(sbmp, 0, wx.EXPAND|wx.TOP, 5)
        self.SetupScrolling()

#------------ScrolledPanel end----------------------


if __name__ == '__main__':
    app = wx.App()
    ScrolledPanelFrame(None).Show()
    app.MainLoop()
