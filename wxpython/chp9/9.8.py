import wx


if __name__ == '__main__':
    app = wx.App()
    fontData = wx.FontData()
    fontData.SetAllowSymbols(True)
    fontData.SetShowHelp(True)
    #fontData.SetRange(5, 5)
    fontData.EnableEffects(True)
    dialog = wx.FontDialog(None, fontData)
    ret = dialog.ShowModal()
    if ret == wx.ID_OK:
        data = dialog.GetFontData()
        font = data.GetChosenFont()
        colour = data.GetColour()
        print('You selected:"%s", %d points\n' % (font.GetFaceName(), font.GetPointSize()))
    
    dialog.Destroy()
    
