import wx
import os

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
        self.button = wx.Button(self.panel, label='Push Me', pos=(50, 50), size=(150, 50))
        #V3 add
        btn = self.button
        self.btnId = btn.GetId() # self.button.GetID()直接使用报错，不知道原因
        # Event Handlers
        self.Bind(wx.EVT_BUTTON, self.OnButton, self.button)

        img_path = os.path.abspath('../image/tip.png')#获取图片的绝对路径
        bitmap = wx.Bitmap(img_path, type=wx.BITMAP_TYPE_PNG)#加载图片到内存
        self.bitmap = wx.StaticBitmap(self.panel, bitmap=bitmap)#显示图片到屏幕

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
