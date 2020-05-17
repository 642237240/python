import wx

if __name__ == '__main__':
    app = wx.App()
    provider = wx.TipWindow('tips.txt', 0)
    