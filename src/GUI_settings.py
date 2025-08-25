# -*- coding: utf-8 -*-

"""
*
*
* INVOICER-V - invoice making software
* Created by Ign555
* Version : v0.9
* Project Creation : 10/04/2025
*
*
"""

import tkinter as tk
from tkinter import ttk
import styles

"""
*
* Settings GUI
*
"""

class SettingsGUI(tk.Toplevel):
    
    def __init__(self, app):

        ##############################-Toplevel init-##############################
        
        super().__init__(app, bg=styles.COLORS["window_background"])
        
        ##############################-Set Class Attributes-##############################
        
        self.app = app
        
        ##############################-Toplevel Settings-##############################
        
        #Define window settings
        self.title('Edit settings')
        self.grab_set() #Locking the interraction only for the popup
        
        #Set Toplevel size
        screen_width = int(self.winfo_screenwidth()/3)
        screen_height = int(self.winfo_screenheight()/2)
        self.geometry(f"{screen_width}x{screen_height}")
        
        ##############################-Set GUI Settings-##############################
        
        settings_tabs = ttk.Notebook(self)
        tab1 = ttk.Frame(settings_tabs)
        tab2 = ttk.Frame(settings_tabs)
        
        settings_tabs.add(tab1, text="t1")
        settings_tabs.add(tab2, text="t2")
        
        settings_tabs.pack(expand=True, fill="both")
        