'''
Created on Jul 24, 2012

@author: Admin
'''


from view.fullscreenwrapper2 import *
import android
import init_resource as ir
import datetime
import os
import view.pathhelpers as pathhelpers
import sys
import time
import threading
droid = android.Android()


# Main Screen Class
class MainScreen(Layout):
    itemms=['history']
    def __init__(self):
        #initialize your class data attributes
        
        #load & set your xml
        super(MainScreen,self).__init__(pathhelpers.read_layout_xml("main.xml"),"Ocr")

    def on_show(self):
    	
    	#self.views.tt.add_event(click_EventHandler(self.views.tt,self.get_options))
    	#self.views.lists.set_listitems(["semir","worku","semir","worku","semir","worku"])
        #initialize your layout views on screen_show
        #self.views.history.set_listitems(self.itemms)
        self.views.logo.src = pathhelpers.get_drawable_pathname("logo.png")
        self.views.close_app.add_event(click_EventHandler(self.views.close_app,self.cls_app))
        self.views.speak_text.add_event(click_EventHandler(self.views.speak_text,self.say_text))
        #self.views.history.add_event(itemclick_EventHandler(self.views.history,self.item_click))
        self.views.search.add_event(click_EventHandler(self.views.search,self.search_term))
    def search_term(self,view,event ):
    	#print view
        term=self.views.search_box.text
        self.itemms.append(term)
        
        #t = threading.Thread(target=ir.getDefinition,args=(term,self))
    	res= ir.getDefinition(term,self)
    	#
    	#v=t.start()
    	#self.views.history.set_listitems(self.itemms)
    	#return v
    	#return True
        #FullScreenWrapper2App.close_layout()
    def cls_app(self,view,event):
        FullScreenWrapper2App.close_layout()
    def item_click(self,view,event):
    	#position = int(event["data"]["position"])
    	#term=self.itemms[position]
    	#t = threading.Thread(target=ir.getDefinition,args=(term,self))
    	#v=t.start()
    	#self.views.result.text=res
    	#print position
    	return
    def say_text(self,view,event):
    	droid.ttsSpeak(self.views.search_box.text)
        return True
    
        
    def get_options(self,view,event):
    	title = 'GUI Test?'
    	choices=['Continue', 'Skip', 'baz']
    	droid.dialogCreateAlert(title)
    	droid.dialogSetSingleChoiceItems(choices)
    	droid.dialogSetPositiveButtonText('Yay!')
    	droid.dialogShow()
    	response = droid.dialogGetResponse().result
		
    	selected_choices = droid.dialogGetSelectedItems().result
    	print selected_choices
    	self.views.tt.text=choices[selected_choices[0]]
        return True
    def on_close(self):
        pass

if __name__ == '__main__':
    FullScreenWrapper2App.initialize(droid)
    FullScreenWrapper2App.show_layout(MainScreen())
    FullScreenWrapper2App.eventloop()
    
