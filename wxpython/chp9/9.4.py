import wx


if __name__ == '__main__':
    app = wx.App()
    choices = ['Alpha', 'Baker', 'Charlie', 'Delta']
    dialog = wx.SingleChoiceDialog(None, "Pick A Word", 'Choices', choices)
    dialog.SetSelection(1)
    print(dialog.GetSelection())
    if dialog.GetStringSelection() == choices[dialog.GetSelection()]:
        print(choices[dialog.GetSelection()])
    ret = dialog.ShowModal()
    if ret == wx.ID_OK:
        print('You selected: %s\n' % dialog.GetStringSelection())
    
    dialog.Destroy()
