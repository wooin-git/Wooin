from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication,QPalette,QColor, QResizeEvent
from PySide6.QtWidgets import QMainWindow,QApplication, QSizePolicy
from PySide6.QtCore import Qt, QSize

import os,sys
sys.path.append("/home/rapa/yummy/pipeline/scripts/loader")
from loader_ui.main_window_v005_ui import Ui_MainWindow
from loader_script.loader_shot import Mainloader
from loader_script.loader_my_task_v002 import My_task
from loader_script.loader_clip_v002 import Libraryclip
from loader_script.loader_asset import Libraryasset
from loader_module.project_data import project_data
from loader_script.loader_pub import Loader_pub
import json
import subprocess

# class Merge(QWidget,Mainloader,project_data,Loader_pub):
class Merge(QMainWindow,Libraryclip,project_data,My_task,Loader_pub,Mainloader,Libraryasset):
    def __init__(self,info):
        super().__init__()
        self.set_up()
        self.setPalette(self.get_darkModePalette())
        self.tab_enable(info)
        self.set_main_loader(info)

        
        info = project_data.__init__(self,info)
        self.write_project_json(info)
        
        self.connect_script()
        self.ui.pushButton_reset.clicked.connect(self.reset_ui)


    def set_main_loader(self,info):
        
        project   = info["project"]
        user      = info["name"]
        rank      = info["rank"]
        
        self.ui.label_projectname.setText(f"{project}")
        self.ui.label_username.setText(f"{user}")
        self.ui.label_rank.setText(f"{rank}")
    
    def write_project_json(self,info):
        with open("/home/rapa/yummy/pipeline/json/project_data.json", "w") as w:
            json.dump(info,w,indent = "\n")
    
    def tab_enable(self,info):
        if not info["rank"] == "Admin":
            self.ui.tabWidget_all.removeTab(3)

    def reset_ui(self):
        print("0000000000")
        login_path = "python3.9 /home/rapa/yummy/pipeline/scripts/loader/loader_script/singin.py"
        subprocess.Popen(login_path, shell=True,executable="/bin/bash")

        sys.exit()


    def center_window(self):
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.geometry() 
        screen_center = screen_geometry.center() 
        window_geometry = self.frameGeometry()  
        window_geometry.moveCenter(screen_center)  
        adjusted_position = window_geometry.topLeft()
        self.move(adjusted_position)

        user = info["name"]
        self.setWindowTitle(f"{user} Loader")

    def resizeEvent(self, event):
        new_size = event.size()
        
        self.shot.resize_shot_status(new_size)

        self.my_task.resize_my_task_status(new_size)
        self.my_task.resize_mytask_table(new_size)
        self.my_task.resize_mytask_object(new_size)
        
        
    def get_darkModePalette(self) :

        darkPalette = self.palette()
        darkPalette.setColor( QPalette.Window, QColor( 53, 53, 53 ) )
        darkPalette.setColor( QPalette.WindowText, QColor(211, 215, 207))
        darkPalette.setColor( QPalette.Disabled, QPalette.WindowText, QColor( 127, 127, 127 ) )
        darkPalette.setColor( QPalette.Base, QColor( 42, 42, 42 ) )
        darkPalette.setColor( QPalette.AlternateBase, QColor( 66, 66, 66 ) )
        darkPalette.setColor( QPalette.ToolTipBase, QColor( 53, 53, 53 ) )
        darkPalette.setColor( QPalette.ToolTipText, QColor(211, 215, 207) )
        darkPalette.setColor( QPalette.Text, QColor(211, 215, 207) )
        darkPalette.setColor( QPalette.Disabled, QPalette.Text, QColor( 127, 127, 127 ) )
        darkPalette.setColor( QPalette.Dark, QColor( 35, 35, 35 ) )
        darkPalette.setColor( QPalette.Shadow, QColor( 20, 20, 20 ) )
        darkPalette.setColor( QPalette.Button, QColor( 53, 53, 53 ) )
        darkPalette.setColor( QPalette.ButtonText, QColor(211, 215, 207) )
        darkPalette.setColor( QPalette.Disabled, QPalette.ButtonText, QColor( 127, 127, 127 ) )
        darkPalette.setColor( QPalette.BrightText, Qt.red )
        darkPalette.setColor( QPalette.Link, QColor( 42, 130, 218 ) )
        darkPalette.setColor( QPalette.Highlight, QColor( 42, 130, 218 ) )
        darkPalette.setColor( QPalette.Disabled, QPalette.Highlight, QColor( 80, 80, 80 ) )
        darkPalette.setColor( QPalette.HighlightedText, QColor(211, 215, 207) )
        darkPalette.setColor( QPalette.Disabled, QPalette.HighlightedText, QColor( 127, 127, 127 ), )

        return darkPalette

    def set_up(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.center_window()

    def connect_script(self):
        self.my_task = My_task(self.ui)
        self.shot = Mainloader(self.ui)

        Libraryclip.__init__(self,self.ui)
        Libraryasset.__init__(self,self.ui)
        Loader_pub.__init__(self,self.ui)


info = {"project": "YUMMIE", "name": "Wooin JUNG", "rank": "Admin"}

if __name__ == "__main__":
    app  = QApplication()
    my = Merge(info)
    my.show()
    app.exec()