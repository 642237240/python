import wx

class FileAndTextDropTarget(wx.PyDropTarget):
    '''Drop target capable of accepting drop files and text'''
    def __init__(self, file_callback, text_callback):
        assert callable(file_callback)
        assert callable(text_callback)
        super(FileAndTextDropTarget, self).__init__()

        #attributes
        self.fcallback = file_callback # drop file callback
        self.tcallback = text_callback #drop text callback
        self._data = None
        self.txtdo = None
        self.filedo = None

        #setup
        self.InitObjects()
    
    def InitObjects(self):
        '''Initializes the text and file data objects'''
        self._data = wx.DataObjectComposite()
        self.txtdo = wx.TextDataObject()
        self.filedo = wx.FileDataObject()
        self._data.Add(self.txtdo, False)
        self._data.Add(self.filedo, True)
        self.SetDataObject(self._data)
    
    def OnData(self, x_cord, y_cord, drag_result):
        '''Called by the framework when data is dropped on the target'''
        if self.GetData():
            data_format = self._data.GetReceivedFormat()
            if data_format.GetType() == wx.DF_FILENAME:
                self.fcallback(self.filedo.GetFilenames())
            else:
                self.tcallback(self.txtdo.GetText())
        
        return drag_result

class DropTargetFrame(wx.Frame):
    def __init__(self, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, 
        size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, name='DropTargetFrame'):
        super(DropTargetFrame, self).__init__(None, id, title, pos, size, style, name)

        # Attributes
        choices = ['Drag and drop text or files here',]
        self.list = wx.ListBox(self, choices=choices)
        self.dt = FileAndTextDropTarget(self.OnFileDrop, self.OnTextDrop)
        self.list.SetDropTarget(self.dt)

        #setup
        self.CreateStatusBar()
    def OnFileDrop(self, files):
        self.PushStatusText('Files Dropped')
        for f in files:
            self.list.Append(f)
    
    def OnTextDrop(self, text):
        self.PushStatusText("Text dropped")
        self.list.Append(text)

if __name__ == '__main__':
    app = wx.App()
    frm = DropTargetFrame()
    frm.Show()
    app.MainLoop()
