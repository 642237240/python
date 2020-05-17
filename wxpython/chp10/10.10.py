import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Fancier Menu Example')
        p = wx.Panel(self)
        menu = wx.Menu()

        bmp = wx.Bitmap('open.png', wx.BITMAP_TYPE_PNG)
        item = wx.MenuItem(menu, -1, 'Has Open Bitmap')
        item.SetBitmap(bmp)
        menu.AppendItem(item)

        for True or 