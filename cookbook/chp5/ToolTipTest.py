import wx

#----------------ToolTip start--------------
'''
wx.Window的SetToolTip()方法，将ToolTip和windon时联系起来
'''
class ToolTipFrame(wx.Frame):
    def __init__(self, parent):
        super(ToolTipFrame, self).__init__(parent)

        # Attributes
        self.tltp = ToolTipPanel(self)

        # Layout
        self.CreateStatusBar()

class ToolTipPanel(wx.Panel):
    def __init__(self, parent):
        super(ToolTipPanel, self).__init__(parent)

        # Attributes
        self.button = wx.Button(self, label='Go')

        # Setup
        self.button.SetToolTip("Launch the shuttle")
        self.timer = wx.Timer(self)
        self.count = 11

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.button, 0, wx.ALIGN_CENTER)
        msizer = wx.BoxSizer(wx.HORIZONTAL)
        msizer.Add(sizer, 1, wx.ALIGN_CENTER)
        self.SetSizer(msizer)

        # Event Handlers
        self.Bind(wx.EVT_BUTTON, self.OnGo, self.button)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
    
    def OnGo(self, event):
        self.button.Disable()
        print(self.timer.Start(1000))
        tlw = self.GetTopLevelParent()
        tlw.PushStatusText("Launch initiated...")
    
    def OnTimer(self, event):
        tlw = self.GetTopLevelParent()
        self.count -= 1
        tlw.PushStatusText('%d' % self.count)
        if self.count == 0:
            self.timer.Stop()
            wx.MessageBox("Shttle Launched!")
#--------------ToolTip end--------------------

#----------------SuperToolTip start--------------
'''
1、导入wx.lib.agw包
2、使用SuperToolTip类创建实例对象
3、使用SetBodyImage()方法设置tip的body message，image显示在message的左边
4、使用SetHeader()为tip添加header text
5、使用SetFooter()和SetFooterBitmap()方法设置footer的message和image
6、使用ApplyStyle()方法设置主题样式
7、使用SetTarget()方法将tip和对象绑定
样式：
    使用方法GetStyleKeys()获取内建的样式列表
自定义方法：
    SetDrawHeaderLine(bool):在header和body之间设置水平分割线
    SetDrawFooterLine(bool):在body和footer之间设置水平分割线
    SetDropShadow(bool):设置drop shadow
    SetUseFade(tool):使用逐渐消失的视图
    SetEndDelay(bool):设置tip显示的时间
    SetTopGradientColour(colour):设置top梯度颜色
    SetBottomGradientColour(colour):设置bottom梯度颜色
    SetMiddleGradientColour(colour):设置Middle梯度颜色
'''
import wx.lib.agw.supertooltip as supertooltip
class SuperToolTipFrame(wx.Frame):
    def __init__(self, parent):
        super(SuperToolTipFrame, self).__init__(parent)

        # Attributes
        self.stltp = SuperToolTipPanel(self)

        # Layout
        self.CreateStatusBar()

class SuperToolTipPanel(wx.Panel):
    def __init__(self, parent):
        super(SuperToolTipPanel, self).__init__(parent)

        # Attributes
        self.button = wx.Button(self, label='Go')
        msg = "Launch the shuttle"
        self.stip = wx.lib.agw.supertooltip.SuperToolTip(msg)

        # Setup SuperToolTip
        bodybmp = wx.Bitmap('../image/search.png', wx.BITMAP_TYPE_PNG)
        self.stip.SetBodyImage(bodybmp)
        self.stip.SetHeader('Launch Control')
        footbmp = wx.Bitmap('../image/tip.png', wx.BITMAP_TYPE_PNG)
        self.stip.SetFooterBitmap(footbmp)
        footer = 'Warning: This is serious bussiness'
        self.stip.SetFooter(footer)
        self.stip.ApplyStyle('XP Blue')
        self.stip.SetTarget(self.button)
        self.stip.SetDrawHeaderLine(True)
        self.stip.SetDrawFooterLine(True)
        self.stip.SetDropShadow(True)
        self.stip.SetUseFade(True)
        self.stip.SetEndDelay(5)
        self.stip.SetTopGradientColour(wx.RED)
        self.stip.SetMiddleGradientColour(wx.WHITE)
        self.stip.SetBottomGradientColour(wx.BLACK)
#--------------SuperToolTip end--------------------

#----------------BallonTip start--------------
'''
参数shape：BT_RECTANGLE或BT_ROUNDED(默认)
样式：
    BT_LEAVE：离开目标时，tip消失
    BT_CLICK：敲击目标时，tip消失
    BT_BUTTON：敲击tip窗口的关闭按钮时，tip消失
方法：
    SetBalloonColour(colour):设置tip的背景色
    SetMessageColour(colour):设置tip message的颜色
    SetMessageFont(font):设置tip message的字体
    SetTitleColour(colour):设置tip标题的颜色
    SetTitleFont(Font):设置tip标题的字体
'''
import wx.lib.agw.balloontip as btip

class BalloonTipFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "BalloonTip Demo")

        # Attributes
        panel = wx.Panel(self)

        txtctrl = wx.TextCtrl(panel, -1, "I am a textctrl", pos=(100,100))

        bmp = wx.Bitmap('../image/critical.png', wx.BITMAP_TYPE_PNG)

        tipballoon = btip.BalloonTip(topicon=bmp, 
                            toptitle='textctrl', message='this is a textctrl',
                            shape=btip.BT_ROUNDED, tipstyle=btip.BT_LEAVE)
        
        # Set the BalloonTip target
        tipballoon.SetTarget(txtctrl)
        # Set the BalloonTip background colour
        tipballoon.SetBalloonColour(wx.WHITE)

        # Set the font for the balloon title
        tipballoon.SetTitleFont(wx.Font(9, wx.FONTFAMILY_SWISS, 
                                        wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        # Set the colour for balloon title 
        tipballoon.SetTitleColour(wx.BLACK)

        # Leave the message font as default
        tipballoon.SetMessageFont()
        # Set message (tip) foreground colour
        tipballoon.SetMessageColour(wx.RED)

        # Set the start delay for the BalloonTip
        tipballoon.SetStartDelay(1000)
        # Set the time after which the BalloonTip is destroyed
        #tipballoon.SetEndDelay(3000)

        # Layout

#--------------BallonTip end--------------------

if __name__ == '__main__':
    app = wx.App()
    ToolTipFrame(None).Show()
    SuperToolTipFrame(None).Show()
    BalloonTipFrame(None).Show()
    app.MainLoop()
