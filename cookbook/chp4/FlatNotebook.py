#------------FlatNotebook start----------------
import wx
import wx.lib
import wx.lib.flatnotebook as FNB

class FlatNotebookFrame(wx.Frame):
    def __init__(self, parent):
        super(FlatNotebookFrame, self).__init__(self)

        self.fnb = MyFlatNoteBook(self)

class MyFlatNoteBook(FNB.FlateNotebook):
    def __init__(self, parent):
        mystyle =   FNB.FNB_DROPDOWN_TABS_LIST|\
                    FNB.FNB_FF2|\
                    FNB.FNB_SMART_TABS|\
                    FNB.FNB_X_ON_TAB
        super(MyFlatNoteBook, self).__init__(parent, style=mystyle)

        #attribures
        self._imglst = wx.ImageList(16, 16)

        #setup
        bmp = wx.Bitmap("../image/bitmap/ab-1.png")
        self._imglst.Add(bmp)
        bmp = wx.Bitmap('../image/bitmap/ab-2.png')
        self._imglst.Add(bmp)
        self.SetImageList(self._imglst)

        # Event Handlers
        self.Bind(FNB.EVT_FLATNOTEBOOK_PAGE_CLOSING, self.OnClosing)
    
    def OnClosing(self, event):
        '''Called when a tab is closing'''
        page = self.GetCurrentPage()
        if page and hasattr(page, "IsModified"):
            if page.IsModified():
                r = wx.MessageBox("Warning unsaved changes"
                                    " will be lost",
                                    'Close Warning', 
                                    wx.ICON_WARNING|wx.OK|wx.CANCEL)
                if r == wx.CANCEL:
                    event.Veto()
        
# -----------FlatNotebook end------------------  
if __name__ == '__main__':
    app = wx.App()
    FlatNotebookFrame(None).Show()
    app.MainLoop()