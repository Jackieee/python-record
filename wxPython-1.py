import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title="创建Frame", pos=(100, 100), size=(600, 400))

        # 创建面板
        panel = wx.Panel(self)
        # 创建文本
        self.ipInfo = wx.StaticText(panel, label="请输入IP地址", pos=(20, 20))
        self.ipInput = wx.TextCtrl(panel, pos=(100, 20))
        self.rackInfo = wx.StaticText(panel, label="请输入机架号", pos=(20, 60))
        self.rackInput = wx.TextCtrl(panel, pos=(100, 60))
        self.slotInfo = wx.StaticText(panel, label="请输入插槽", pos=(20, 100))
        self.slotInput = wx.TextCtrl(panel, pos=(100, 100))
        self.runningTitle = wx.StaticText(panel, label="运行信息", pos=(260, 20))
        self.runningInfo = wx.TextCtrl(panel, pos=(250, 40), size=(200, 200), style=wx.TE_MULTILINE)
        # 创建按钮
        self.bt_confirm = wx.Button(panel, label="连接", pos=(20, 140))
        # 按钮触发事件
        self.bt_confirm.Bind(wx.EVT_BUTTON, self.OnClickSubmit)
        self.bt_cancel = wx.Button(panel, label="断开", pos=(120, 140))

        # 按钮触发函数定义

    def OnClickSubmit(self, event):
        ip = self.ipInput.GetValue()
        self.runningInfo.SetValue(ip)


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
