import wx
import os

def SetClipboardText(text):
    '''Put text in the clipboard
    @param text: string
    '''
    data_o = wx.TextDataObject()
    data_o.SetText(text)
    if wx.Clipboard.IsOpened() or wx.Clipboard.Open():
        wx.Clipboard.SetData(data_o)
        wx.Clipboard.Close()

def GetClipboardText():
    '''Get text from the clipboard
    @return: string
    '''
    text_obj = wx.TextDataObject()
    rtext = ''
    if wx.Clipboard.IsOpened() or wx.Clipboard.Open():
        if wx.Clipboard.GetData(text_obj):
            rtext = text_obj.GetText()
        wx.Clipboard.Close()
    return rtext

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title='The Main Frame')
        self.SetTopWindow(self.frame)
        self.frame.Show()

        #wx.MessageBox('Hello wxpython', 'wxApp')
        return True

class MyFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title='', pos=wx.DefaultPosition,
        size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, name='MyFrame'):
        super(MyFrame, self).__init__(parent, id, title, pos, size, style, name)

        # Attributes
        self.panel = wx.Panel(self)
        #V2 add
        self.panel.SetBackgroundColour(wx.BLACK)
        self.button = wx.Button(self.panel, label='Push Me', pos=(280, -1), size=(100, -1))
        #V3 add
        btn = self.button
        self.btnId = btn.GetId() # self.button.GetID()直接使用报错，不知道原因
        # Event Handlers
        self.Bind(wx.EVT_BUTTON, self.OnButton, self.button)

        img_path = os.path.abspath('../image/tip.png')#获取图片的绝对路径
        bitmap = wx.Bitmap(img_path, type=wx.BITMAP_TYPE_PNG)#加载图片到内存
        self.bitmap = wx.StaticBitmap(self.panel, bitmap=bitmap)#显示图片到屏幕

        icon_path = os.path.abspath('../image/warning.png')
        icon = wx.Icon(icon_path, wx.BITMAP_TYPE_PNG)#use an icon load image into memory
        self.SetIcon(icon) #call Frame's SetIcon method to set the icon

        # 使用默认的id创建OK和Cancel按钮，控件上生成合适的label 
        ok_btn = wx.Button(self.panel, wx.ID_OK, pos=(50,-1))
        cancel_btn = wx.Button(self.panel, wx.ID_CANCEL, pos=(150, -1))

        menu_bar = wx.MenuBar() #生成一个menuBar
        edit_menu = wx.Menu() #生成一个menu
        edit_menu.Append(wx.NewId(), "Test") #添加Test标签项到menu
        edit_menu.Append(wx.ID_PREFERENCES) #添加偏好菜单项到menu
        menu_bar.Append(edit_menu, 'Edit') #添加菜单到菜单栏
        self.SetMenuBar(menu_bar)   #添加菜单栏到Frame

    def OnButton(self, event):
        '''Called when the button is clicked'''
        print('\nFrame GetChildren:')
        for child in self.GetChildren():
            print("%s" % repr(child))

        print('\nPanel FindWindowById:')
        button = self.panel.FindWindowById(self.btnId)
        print('%s' % repr(button))
        #change the Button's label
        button.SetLabel("Changed Label")

        print('\nButton GetParent:')
        panel = button.GetParent()
        print('%s' % repr(panel))

        print('\nGet the Application Object:') 
        app = wx.GetApp()
        print('%s' % repr(app))

        print('\nGet the Frame from the App:')
        frame = app.GetTopWindow()
        print('%s' % frame)

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()
