import wx

image_path = 'D:\\CodeProject\\python\\image\\'

filenames = ['image.bmp', 'image.gif', 'image.jpg', 'image.png']

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='Loading Images')
        p = wx.Panel(self)

        fgs = wx.FlexGridSizer(cols=2, hgap=10, vgap=10)
        for name in filenames:
            name = image_path + name
            #print(name)
            img1 = wx.Image(name, wx.BITMAP_TYPE_ANY)

            w = img1.GetWidth()*4
            h = img1.GetHeight()*4
            img2 = img1.Scale(w/2, h/2)

            sb1 = wx.StaticBitmap(p, -1, wx.BitmapFromImage(img1))
            sb2 = wx.StaticBitmap(p, -1, wx.BitmapFromImage(img2))

            fgs.Add(sb1)
            fgs.Add(sb2)

        p.SetSizerAndFit(fgs)
        self.Fit()

app = wx.App()
frm = TestFrame()
frm.Show()
app.MainLoop()
