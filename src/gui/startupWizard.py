'''
Created on 21 juin 2010. Copyright 2010, David GUEZ
@author: david guez (guezdav@gmail.com)
This file is a part of the source code of the MALODOS project.
You can use and distribute it freely, but have to conform to the license
attached to this project (LICENSE.txt file)
=====================================================================
class related to the document to go wizard
'''

import wx.adv
class StartupWizard(wx.adv.Wizard):
    '''
    wizard helping user to configure the preferences
    '''


    def __init__(self,params):
        '''
        Constructor
        '''
 
class PageScannerChoice (wx.adv.PyWizardPage):
    def __init__(self,parent):
        wx.adv.PyWizardPage.__init__(self,parent)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)
        
    def GetNext(self):
        return None
    def GetPrev(self):
        return None


class PageOCRChoice (wx.adv.PyWizardPage):
    def __init__(self,parent):
        wx.adv.PyWizardPage.__init__(self,parent)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)
        
    def GetNext(self):
        return None
    def GetPrev(self):
        return None

class PageSurveyChoice (wx.adv.PyWizardPage):
    def __init__(self,parent):
        wx.adv.PyWizardPage.__init__(self,parent)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)
        
    def GetNext(self):
        return None
    def GetPrev(self):
        return None

class PageFoldersChoice (wx.adv.PyWizardPage):
    def __init__(self,parent):
        wx.adv.PyWizardPage.__init__(self,parent)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)
        
    def GetNext(self):
        return None
    def GetPrev(self):
        return None