#!/usr/bin/env python
'''
Originally found at Mouse vs Python
http://www.blog.pythonlibrary.org/2010/01/17/configobj-wxpython-geek-happiness/

Please see http://www.blog.pythonlibrary.org/license/ for license information
'''

import configobj
import wx

########################################################################
class PreferencesDialog(wx.Dialog):
    '''
    Creates and displays a preferences dialog that allows the user to
    change some settings.
    '''

    #----------------------------------------------------------------------
    def __init__(self, parentFrame):
        '''
        Initialize the dialog
        '''

        wx.Dialog.__init__(self, parentFrame, wx.ID_ANY, 'Preferences', size=(900,200))
        self.CenterOnParent()
        self.createWidgets()
 
    #----------------------------------------------------------------------
    def createWidgets(self):
        '''
        Create and layout the widgets in the dialog
        '''
        # lblSizer = wx.BoxSizer(wx.VERTICAL)
        # valueSizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = wx.StdDialogButtonSizer()
        colSizer = wx.BoxSizer(wx.HORIZONTAL)
        mainSizer = wx.BoxSizer(wx.VERTICAL)
 
        iniFile = 'config.ini'
        self.config = configobj.ConfigObj(iniFile)
 
        labels = self.config['Labels']
        values = self.config['Values']
        self.widgetNames = values

        if wx.Platform == '__WXMAC__':
            font = wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
        else:
            font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)

        gs = wx.FlexGridSizer(len(labels), 2, 5, 5)

        for key in labels:
            value = labels[key]
            lbl = wx.StaticText(self, label=value)
            lbl.SetFont(font)
            # lblSizer.Add(lbl, 0, wx.ALL, 5)
            gs.Add(lbl, 1, wx.ALIGN_LEFT)

            value2 = values[key]
            if isinstance(value2, list):
                default = value2[0]
                choices = value2[1:]
                cbo = wx.ComboBox(self, value=value2[0],
                                  size=wx.DefaultSize, choices=choices,
                                  style=wx.CB_DROPDOWN|wx.CB_READONLY,
                                  name=key)
                # valueSizer.Add(cbo, 0, wx.ALL, 5)
                gs.Add(cbo, 3, wx.EXPAND)
            else:
                txt = wx.TextCtrl(self, value=value2, name=key)
                #valueSizer.Add(txt, 0, wx.ALL|wx.EXPAND, 5)
                gs.Add(txt, 3, wx.EXPAND)
        gs.AddGrowableCol(1, 1)
        
        # for key in values:
            # # print key
            # value = values[key]
            # if isinstance(value, list):
                # default = value[0]
                # choices = value[1:]
                # cbo = wx.ComboBox(self, value=value[0],
                # size=wx.DefaultSize, choices=choices,
                # style=wx.CB_DROPDOWN|wx.CB_READONLY,
                # name=key)
                # #valueSizer.Add(cbo, 0, wx.ALL, 5)
                # gs.Add(cbo, 0, wx.ALIGN_RIGHT)
            # else:
                # txt = wx.TextCtrl(self, value=value, name=key)
                # #valueSizer.Add(txt, 0, wx.ALL|wx.EXPAND, 5)
                # gs.Add(txt, 0, wx.ALIGN_RIGHT)
 
        saveBtn = wx.Button(self, wx.ID_OK, label='Save')
        saveBtn.Bind(wx.EVT_BUTTON, self.onSave)
        btnSizer.AddButton(saveBtn)
 
        cancelBtn = wx.Button(self, wx.ID_CANCEL)
        btnSizer.AddButton(cancelBtn)
        btnSizer.Realize()
 
        #colSizer.Add(lblSizer)
        #colSizer.Add(valueSizer, 1, wx.EXPAND)
        #colSizer.Add(gs, 1, wx.EXPAND)
        colSizer.Add(gs, proportion=1, flag=wx.ALL|wx.EXPAND, border=15)
        mainSizer.Add(colSizer, 0, wx.EXPAND)
        mainSizer.Add(btnSizer, 0, wx.ALL | wx.ALIGN_RIGHT, 5)
        self.SetSizer(mainSizer)
 
    #----------------------------------------------------------------------
    def onSave(self, event):
        '''
        Saves values to disk
        '''
        for name in self.widgetNames:
            widget = wx.FindWindowByName(name)
            if isinstance(widget, wx.ComboBox):
                selection = widget.GetValue()
                choices = widget.GetItems()
                choices.insert(0, selection)
                self.widgetNames[name] = choices
            else:
                value = widget.GetValue()
                self.widgetNames[name] = value
        self.config.write()
        self.EndModal(0)
 