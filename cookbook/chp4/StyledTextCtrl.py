import wx
import wx.stc as stc
import keyword

#------------StyledTextCtrl start-------------------
'''
StyleSetSpec(stylenum, spec)方法:
参数stylenum时样式id，以STC_STYLE_开头
参数spec：样式字符串，格式
ATTRIBUTE:VALUE,ATTRIBUTE:VALUE,MODIFIER
attribute       value
fore            Foreground color，使用颜色名称(black)或hex颜色字符串（#000000)
back            Background color
face            字体名称，如Monaco
size            字体大小，如10
modifier        Desciption
bold            粗体
italic          斜体
underline       下划线
eol             行尾扩展背景颜色
'''
class StyledTextCtrlFrame(wx.Frame):
    def __init__(self, parent, *args, **kwagrs):
        super(StyledTextCtrlFrame, self).__init__(parent, *args, **kwagrs)
        #Attibutes
        self.panel = StyledTextCtrlPanel(self)
        self.CreateStatusBar()

class StyledTextCtrlPanel(wx.Panel):
    def __init__(self, parent):
        super(StyledTextCtrlPanel, self).__init__(parent)

        # attibutes
        self.stc = PythonCodeEditor(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.stc, 1, wx.EXPAND)
        self.SetSizer(sizer)

class CodeEditorBase(wx.stc.StyledTextCtrl):
    def __init__(self, parent):
        super(CodeEditorBase, self).__init__(parent)

        #Attributs
        font = wx.Font(10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.face = font.GetFaceName()
        self.size = font.GetPointSize()

        # Setup
        self.SetupBaseStyles()

    def EnableLineNumbers(self, enable=True):
        '''Enable/Disable line number margin'''
        if enable:
            self.SetMarginType(1, wx.stc.STC_MARGIN_NUMBER)
            self.SetMarginMask(1, 0)
            self.SetMarginWidth(1, 25)
        else:
            self.SetMarginWidth(1, 0)
    
    def GetFaces(self):
        '''Get font style dictionary'''
        return dict(font=self.face, size=self.size)
    
    def SetupBaseStyles(self):
        '''Sets up the basic non lexer specific styles.'''
        faces = self.GetFaces()
        default = 'face: %(font)s, size:%(size)d' % faces
        self.StyleSetSpec(wx.stc.STC_STYLE_DEFAULT, default)
        line = 'fore: #C0C0C0, ' + default
        self.StyleSetSpec(wx.stc.STC_STYLE_LINENUMBER, line)
        self.StyleSetSpec(wx.stc.STC_STYLE_CONTROLCHAR, 'face:%(font)s' % faces)

'''
1、使用SetLexer方法设置语法分析程序(lexer)的模式
2、设置lexer的关键字，使用SetKeyWords()方法
3、设置lexer的样式，使用StyleSetSpec()方法
'''
class PythonCodeEditor(CodeEditorBase):
    def __init__(self, parent):
        super(PythonCodeEditor, self).__init__(parent)

        #setup
        self.SetLexer(wx.stc.STC_LEX_PYTHON)
        self.SetupKeywords()
        self.SetupStyles()
        self.EnableLineNumbers(True)
    
    def SetupKeywords(self):
        '''Sets up the lexers keywords'''
        kwlist = u' '.join(keyword.kwlist)
        self.SetKeyWords(0, kwlist)
    
    def SetupStyles(self):
        '''Sets up the lexers styles'''
        #python styles
        faces = self.GetFaces()
        fonts = 'face:%(font)s,size:%(size)d' % faces
        default = 'fore:#000000, ' + fonts

        #default
        self.StyleSetSpec(wx.stc.STC_P_DEFAULT, default)
        #comments
        self.StyleSetSpec(wx.stc.STC_P_COMMENTLINE, 'fore:#007F00' + fonts)
        #number
        self.StyleSetSpec(wx.stc.STC_P_NUMBER, 'fore:#007F7F,' + fonts)
        #string
        self.StyleSetSpec(wx.stc.STC_P_STRING, 'fore:#7F007F,' + fonts)
        #Single quoted string
        self.StyleSetSpec(wx.stc.STC_P_CHARACTER, 'fore:#7F007F, ' + fonts)
        #keyword
        self.StyleSetSpec(wx.stc.STC_P_WORD, 'fore:00007F,bold,' + fonts)
        #Triple quotes
        self.StyleSetSpec(wx.stc.STC_P_TRIPLE, 'fore:#7F0000,' + fonts)
        #Tiple double quotes
        self.StyleSetSpec(wx.stc.STC_P_TRIPLEDOUBLE, 'fore:#7F0000' + fonts)
        #Class  name definition
        self.StyleSetSpec(wx.stc.STC_P_CLASSNAME, 'fore:#0000FF,bold,' + fonts)
        #Function or method name definition
        self.StyleSetSpec(wx.stc.STC_P_DEFNAME, 'fore:#007F7F,bold,' + fonts)
        #Operators
        self.StyleSetSpec(wx.stc.STC_P_OPERATOR, 'bold,' + fonts)
        # Identifiers
        self.StyleSetSpec(wx.stc.STC_P_IDENTIFIER, default)
        # Comment-blocks
        self.StyleSetSpec(wx.stc.STC_P_COMMENTBLOCK, 'fore:#7F7F7F,' + fonts)
        #end of line where string is not closed
        eol_style = 'fore:#000000,back:#E0C0E0,eol,' + fonts
        self.StyleSetSpec(wx.stc.STC_P_STRINGEOL, eol_style)

#------------StyledTextCtrl end---------------------

if __name__ == '__main__':
    app = wx.App()
    StyledTextCtrlFrame(None).Show()
    app.MainLoop()
