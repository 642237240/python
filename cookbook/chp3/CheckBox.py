import wx
import wx.lib.platebtn as pbtn
import wx.lib.agw.gradientbutton as gbtn

# --------------Button start--------------
class ButtonFrame(wx.Frame):
    def __init__(self, parent, *args, **kwagrs):
        super(ButtonFrame, self).__init__(parent, *args, **kwagrs)
        self.panel = ButtonPanel(self)

class ButtonPanel(wx.Panel):
    def __init__(self, parent):
        super(ButtonPanel, self).__init__(parent)

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
        menu.Append(wx.NewIdRef(), item="Hello World")
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
#--------Button end----------------

#---------CheckBox start-----------
class CheckBoxFrame(wx.Frame):
    def __init__(self, parent, *args, **kwagrs):
        super(CheckBoxFrame, self).__init__(parent, *args, **kwagrs)

        # attributes
        self.panel = wx.Panel(self)
        self.checkbox1 = wx.CheckBox(self.panel, label='2 State CheckBox')
        style = wx.CHK_3STATE|wx.CHK_ALLOW_3RD_STATE_FOR_USER
        self.checkbox2 = wx.CheckBox(self.panel, label='3 State CheckBox', style=style)

        # layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.checkbox1, 0, wx.ALL, 15)
        sizer.Add(self.checkbox2, 0, wx.ALL, 15)
        self.panel.SetSizer(sizer)
        self.CreateStatusBar()

        #Wvent Handlers
        self.Bind(wx.EVT_CHECKBOX, self.OnCheck)

    def OnCheck(self, event):
        e_obj = event.GetEventObject()
        if e_obj == self.checkbox1:
            checked = self.checkbox1.GetValue()
            msg = 'Two State Clicked: %d' % checked
            self.PushStatusText(msg)
        elif e_obj == self.checkbox2:
            state = self.checkbox2.Get3StateValue()
            msg = 'Three State Clicked: %d' % state
            self.PushStatusText(msg)
        else:
            event.Skip()
#-----------CheckBox end-----------------

# -----------TextCtrl start--------------
'''
wx.TE_PROCESS_ENTER: Enter键按下，控件产生的事件
wx.TE_PRECESS_TAB: 设置时，Tab键按下时，产生wx.EVT_CHAR事件；否则切换到下一个控件
wx.TE_MULTILINE：允许TextCtrl控件多行
wx.TE_READONLY：控件只读，不允许输入
wx.TE_RICH2：控件使用RichText版本
wx.TE_LEFT: 输入text左对齐
wx.TE_CENTER: 居中对齐
wx.TE_RIGHT: 右对齐

'''
class LoginDialog(wx.Dialog):
    def __init__(self, *args, **kwagrs):
        super(LoginDialog, self).__init__(*args, **kwagrs)

        #attibutes
        self.panel = LoginPanel(self)

        #layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize()
    
    def GetUsername(self):
        return self.panel.GetUsername()
    
    def GetPassword(self):
        return self.panel.GetPassword()

class LoginPanel(wx.Panel):
    def __init__(self, parent):
        super(LoginPanel, self).__init__(parent)

        #attributes
        self._username = wx.TextCtrl(self)
        self._passwd = wx.TextCtrl(self, style=wx.TE_PASSWORD)

        # Layout
        sizer = wx.FlexGridSizer(2, 2, 8, 8)
        sizer.Add(wx.StaticText(self, label="Username:", style=wx.ALIGN_CENTER_VERTICAL))
        sizer.Add(self._username, 0, wx.EXPAND)
        sizer.Add(wx.StaticText(self, label='Password:', style=wx.ALIGN_CENTER_VERTICAL))
        sizer.Add(self._passwd, 0, wx.EXPAND)
        msizer = wx.BoxSizer(wx.VERTICAL)
        msizer.Add(sizer, 1, wx.EXPAND|wx.ALL, 20)
        btnszr = wx.StdDialogButtonSizer()
        button = wx.Button(self, wx.ID_OK)
        button.SetDefault()
        btnszr.AddButton(button)
        msizer.Add(btnszr, 0, wx.ALIGN_CENTER|wx.ALL, 12)
        btnszr.Realize()

        self.SetSizer(msizer)
    def GetUsername(self):
        return self._username.GetValue()

    def GetPassword(self):
        return self._passwd.GetValue()
# -------------TextCtrl end---------------

#--------------Choice start----------------
'''
Choice控件被创建后，可以通过控件的方法操作和改变控件的内容
Append(): 控件list最后添加item
AppendItems(): 控件最后添加item list
Insert():  指定位置添加item
SetItems(): 修改显示的items
'''
class ChoiceFrame(wx.Frame):
    def __init__(self, parent, *args, **kwagrs):
        super(ChoiceFrame, self).__init__(parent, *args, **kwagrs)
        self.panel = ChoicePanel(self)

class ChoicePanel(wx.Panel):
    def __init__(self, parent):
        super(ChoicePanel, self).__init__(parent)

        #attibutes
        items = ['item 1', 'item 2', 'item 3']
        self.choice = wx.Choice(self, choices=items)
        self.choice.SetSelection(0)     # 设置选择的初始值
        self.choice.Append('append item 1')     #最后添加item
        apptenItems = ['appendItems item1', 'appendItems item2']
        self.choice.AppendItems(apptenItems)    # 最后添加items列表
        self.choice.Insert('pos 0 insert item', pos=0) #在pos处插入item
        setItems = ['setItem 1', 'setItem 2']
        self.choice.SetItems(setItems)  #修改显示的list为setItems


        #layout
        sizer = wx.BoxSizer()
        sizer.Add(self.choice, 1, wx.EXPAND|wx.ALL, 20)
        self.SetSizer(sizer)

        # Event Handlers
        self.Bind(wx.EVT_CHOICE, self.OnChoice)

    def OnChoice(self, event):
        selection = self.choice.GetStringSelection()
        index = self.choice.GetSelection()
        print('Selected Item: %d "%s"' % (index, selection))
#--------------Choice end------------------

#-------------Menu start-------------------
'''
菜单Menu相关的控件包括：
MenuBar：菜单栏，包含Menu，绑定到框架上
Menu：菜单，包含MenuItem，绑定到MenuBar
MenuItem：菜单项，绑定到Menu
'''
ID_READ_ONLY = wx.NewIdRef()   # 不建议使用wx.NewId()

class MenuFrame(wx.Frame):
    def __init__(self, parent, *args, **kwagrs):
        super(MenuFrame, self).__init__(parent, *args, **kwagrs)

        # attributes
        self.panel = wx.Panel(self)
        self.txtctrl = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)

        # Layout
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.txtctrl, 1, wx.EXPAND)
        self.panel.SetSizer(sizer)
        self.CreateStatusBar()

        # setup the Menu
        menub = wx.MenuBar()

        #file Menu
        filem = wx.Menu()
        filem.Append(wx.ID_OPEN, 'Open\tCtrl+O')

        # file option Submenu
        OptionSubmenu = wx.Menu()
        OptionSubmenu.Append(-1, "setting")
        OptionSubmenu.Append(-1, 'Expension')
        #filem.AppendMenu(-1, 'Option', OptionSubmenu, help='option setting')
        filem.AppendSubMenu(OptionSubmenu, 'Option', help='option setting')
        menub.Append(filem, '&File')

        # Edit Menu
        editm = wx.Menu()
        editm.Append(wx.ID_COPY, 'Copy\tCtrl+C')
        editm.Append(wx.ID_CUT, 'Cut\tCtrl+X')
        editm.Append(wx.ID_PASTE, 'Paste\tCtrl+V')
        editm.AppendSeparator()
        editm.Append(ID_READ_ONLY, "Read Only", kind=wx.ITEM_CHECK)
        menub.Append(editm, 'E&dit')

        # View Menu
        viewm = wx.Menu()
        viewm.Append(-1, "View Space", kind=wx.ITEM_CHECK)
        viewm.Append(-1, 'Always on top', kind=wx.ITEM_CHECK)
        viewm.Append(-1, 'Toggle Full Screen Mode', kind=wx.ITEM_CHECK)
        menub.Append(viewm, 'View')

        # Encoding Menu
        Encodingm = wx.Menu()
        Encodingm.Append(-1, 'ANSI', kind=wx.ITEM_RADIO)
        Encodingm.Append(-1, 'UTF-8', kind=wx.ITEM_RADIO)
        menub.Append(Encodingm, 'Encoding')

        
        self.SetMenuBar(menub)

        # Event Handlets
        self.Bind(wx.EVT_MENU, self.OnMenu)
    
    def OnMenu(self, event):
        '''Handle menu clicks'''
        evt_id = event.GetId()
        actions = { wx.ID_COPY : self.txtctrl.Copy,
                    wx.ID_CUT : self.txtctrl.Cut,
                    wx.ID_PASTE : self.txtctrl.Paste }
        action = actions.get(evt_id, None)
        if action:
            action()
        elif evt_id == ID_READ_ONLY:
            # Toggle enabled state
            self.txtctrl.Enable(not self.txtctrl.Enabled)
        elif evt_id == wx.ID_OPEN:
            dlg = wx.FileDialog(self, "Open File", style=wx.FD_OPEN)
            if dlg.ShowModal() == wx.ID_OK:
                fname = dlg.GetPath()
                print(fname)
                handle = open(fname, 'r')
                self.txtctrl.SetValue(handle.read())
                handle.close()
        else:
            event.Skip()
#-------------Menu end---------------------

#-------------ToolBar start----------------
'''
添加ToolBar的方法：
1、创建ToolBar
2、添加tools
3、调用ToolBar的Realize()方法
4、使用框架Frame的SetToolBar(toolbar)将toolbar绑定到框架
style样式：
wx.TB_FLAT：扁平化显示
wx.TB_HORIZONTAL：水平放置，默认
wx.TB_VERTICAL：垂直放置
wx.TB_TEXT：显示tools的text(label)，默认只显示icons
wx.TB_NOICONS：不显示icons
wx.TB_NODIVIDER：不显示divider(border)
wx.TB_NOALIGN：不使用对齐
wx.TB_HORZ_LAYOUT：必须和wx.TB_TEXT一起使用，text显示在icons的左边
wx.TB_HORZ_TEXT：相当于wx.TB_HORZ_LAYOUT|wx.TB_TEXT
wx.TB_NO_TOOLTIPS：鼠标停靠时，不显示short help
wx.TB_BOTTON：底部对齐
wx.TB_RIGHT：右对齐
wx.TB_DEFAULT_STYLE：相当于wx.TB_HORIZONTAL|wx.TB_FLAT

'''
class ToolBarFrame(wx.Frame):
    def __init__(self, parent, *args, **kw):
        super(ToolBarFrame, self).__init__(parent, *args, **kw)

        tb = wx.ToolBar(self, -1, style=wx.TB_TEXT)
        
        tb.AddTool(-1, label='search', bitmap=wx.Bitmap('../image/search.png'))
        tb.AddTool(-1, label='save', bitmap=wx.Bitmap('../image/bitmap/Save.png'))
        #tb.AddSeparator()
        tb.AddTool(-1, label='printer', bitmap=wx.Bitmap('../image/bitmap/Printer.png'))
        tb.Realize()
        self.SetToolBar(tb)

        # Event Handlers
        self.Bind(wx.EVT_TOOL, self.OnToolBar)

    def OnToolBar(self, event):
        print('ToolBarItem Clicked', event.GetId())

#-------------ToolBar end------------------

#-------------PopupMenu start--------------
class PopupMenuFrame(wx.Frame):
    def __init__(self, parent):
        super(PopupMenuFrame, self).__init__(parent)

        # Attributes
        self.panel = wx.Panel(self)

        # Event Handlers
        self.Bind(wx.EVT_CONTEXT_MENU, self.OnContextMenu)
        self.CreateStatusBar()
    
    def OnContextMenu(self, event):
        '''Create and shows the Menu'''
        menu = wx.Menu()
        menu.Append(wx.ID_CUT)
        menu.Append(wx.ID_COPY)
        menu.Append(wx.ID_PASTE)
        self.Bind(wx.EVT_MENU, self.OnPopupMenu)
        self.PopupMenu(menu)

    def OnPopupMenu(self, event):
        evt_id = event.GetId()
        if evt_id == wx.ID_CUT:
            self.PushStatusText('Press cut menu')
        elif evt_id == wx.ID_COPY:
            self.PushStatusText('Press copy menu')
        else:
            self.PushStatusText('Press paste menu')
#-------------PopupMenu end----------------

#-------------StaticBox start--------------
class StaticBoxFrame(wx.Frame):
    def __init__(self, parent):
        super(StaticBoxFrame, self).__init__(parent)

        #attributes
        self.panel = StaticBoxPanel(self)

class StaticBoxPanel(wx.Panel):
    def __init__(self, parent):
        super(StaticBoxPanel, self).__init__(parent)

        # layout
        sbox = wx.StaticBox(self, label='Box Label')
        sboxsz = wx.StaticBoxSizer(sbox, wx.VERTICAL)

        # Add some controls to the box
        cb = wx.CheckBox(self, label='Enable')
        sboxsz.Add(cb, 0, wx.ALL, 8)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(wx.StaticText(self, label="Value: "))
        sizer.Add((5, 5))
        sizer.Add(wx.TextCtrl(self))
        sboxsz.Add(sizer, 0, wx.ALL, 8)

        msizer = wx.BoxSizer(wx.VERTICAL)
        msizer.Add(sboxsz, 0, wx.EXPAND|wx.ALL, 20)
        self.SetSizer(msizer)


#-------------StaticBox end

if __name__ == '__main__':
    app = wx.App()

#    ButtonFrame(None).Show()    # for Button

#    CheckBoxFrame(None).Show()      # for CheckBox

#    ChoiceFrame(None).Show()        # for Choice

#    MenuFrame(None).Show()          #for Menu

#    ToolBarFrame(None).Show()

#    PopupMenuFrame(None).Show()

    StaticBoxFrame(None).Show()

    app.MainLoop()

    #LoginDialog().ShowModal()      #for TextCtrl