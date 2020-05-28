import wx

#------------ListCtrl start-------------------
'''

'''
class VListCtrlFrame(wx.Frame):
    def __init__(self, parent, *args, **kwagrs):
        super(VListCtrlFrame, self).__init__(parent, *args, **kwagrs)
        #Attibutes
        self.panel = VListBoxPanel(self)
        self.CreateStatusBar()

class VListBoxPanel(wx.Panel):
    def __init__(self, parent):
        super(VListBoxPanel, self).__init__(parent)

        # attibutes
        self.vlstb = MyListBox(self, ['a', 'b', 'c'])

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.vlstb, 1, wx.EXPAND)
        self.SetSizer(sizer)

class MyListBox(wx.VListBox):
    '''Simple List Box control to show a list of users'''
    def __init__(self, parent, users):
        super(MyListBox, self).__init__(parent)

        #Attributes
        #system-users.png is a sample image provided with
        #this chapters sample code.
        self.bmp = wx.Bitmap('../image/search.png', wx.BITMAP_TYPE_PNG)
        self.bh = self.bmp.GetHeight()
        self.users = users

        # Setup
        self.SetItemCount(len(self.users))

    def OnMeasureItem(self, index):
        '''Called to get an items height'''
        # All our items are the same so index is ignored
        return self.bh + 4

    def OnDrawSeparator(self, dc, rect, n):
        '''Called to draw the item separator'''
        oldpen = dc.GetPen()
        dc.SetPen(wx.Pen(wx.BLACK))
        dc.DrawLine(rect.x, rect.y, rect.x + rect.width, rect.y)
        rect.Deflate(0, 2)
        dc.SetPen(oldpen)
    
    def OnDrawItem(self, dc, rect, n):
        '''Called to draw the item'''
        # Draw the bitmap
        dc.DrawBitmap(self.bmp, rect.x + 2, (rect.height - self.bh)//2 + rect.y)
        # Draw the label to the right of the bitmap
        textx = rect.x + 2 + self.bh + 2
        lblrect = wx.Rect(textx, rect.y, rect.width - textx, rect.height)
        dc.DrawLabel(self.users[n], lblrect, wx.ALIGN_LEFT|wx.ALIGN_CENTER_VERTICAL)

#------------ListCtrl end------------------- --       

if __name__ == '__main__':
    app = wx.App()
    VListCtrlFrame(None).Show()
    app.MainLoop()
