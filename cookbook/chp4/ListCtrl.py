import wx

#------------ListCtrl start-------------------
'''

'''
class ListCtrlFrame(wx.Frame):
    def __init__(self, parent, *args, **kwagrs):
        super(ListCtrlFrame, self).__init__(parent, *args, **kwagrs)
        #Attibutes
        self.panel = ListCtrlPanel(self)
        self.CreateStatusBar()

class ListCtrlPanel(wx.Panel):
    def __init__(self, parent):
        super(ListCtrlPanel, self).__init__(parent)

        # attibutes
        self.lstc = MyListCtrl(self)

        # Setup
        data = [('row %d' % x, 'value %d' % x, 'data %d' % x) for x in range(3)]
        self.lstc.PopulateList(data)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.lstc, 1, wx.EXPAND)
        self.SetSizer(sizer)

        # event handlers
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
    
    def OnItemSelected(self, event):
        selected_row = event.GetIndex()
        val = list()
        for column in range(3):
            item = self.lst.GetItem(selected_row, column)
            val.append(item.GetText())
        #show what was selected in the frames status bar
        frame = self.GetTopLevelParent()
        frame.PushStatusText(','.join(val))

class MyListCtrl(wx.ListCtrl):
    def __init__(self, parent):
        super(MyListCtrl, self).__init__(parent, style=wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES)

        #add three columns to the list
        self.InsertColumn(0, 'Column 1')
        self.InsertColumn(1, 'Column 2')
        self.InsertColumn(2, 'Column 3')

    def PopulateList(self, data):
        '''Populate the list with the set of data. Data
        should be a list of tuples that have a value for
        each column in the list.
        [('hello', 'list', 'control'),]
        '''
        for item in data:
            self.Append(item)

#------------ListCtrl end------------------- --       

if __name__ == '__main__':
    app = wx.App()
    ListCtrlFrame(None).Show()
    app.MainLoop()
