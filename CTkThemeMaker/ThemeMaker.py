import platform
import tkinter
import customtkinter
from tkinter.colorchooser import askcolor
from tkinter import filedialog, messagebox
import json
import os
import subprocess

"""
Author: Akash Bora (Akascape)
Quick Guide:
This program can be used to create custom themes for customtkinter.
You can easily create and edit themes for your applications.
Customtkinter themefiles are .json files that can be used with customtkinter using the 'customtkinter.set_default_color_theme(theme_file)' method.
Example: customtkinter.set_default_color_theme("Path/my_theme.json")
A customtkinter theme has one dark and one light color attribute for each widget type and you have to choose the 2 colors for each widget type.
(You can switch between them with the 'set_appearance_mode' method)
Currently it is not possible to switch between themes, so only appearance_mode can be changed.
Default none color is "transparent" which has no color, leaving a widget with this value will give you a blank widget.
(Do not set transparent to CTk window)
"""

class App(customtkinter.CTk):
    
    #--------------------Main Structure of the Theme File--------------------#
    
    json_data = {
                  "CTk": {
                    "fg_color": ["gray92", "gray14"]
                  },
                  "CTkToplevel": {
                    "fg_color": ["gray92", "gray14"]
                  },
                  "CTkFrame": {
                    "corner_radius": 6,
                    "border_width": 0,
                    "fg_color": ["gray86", "gray17"],
                    "top_fg_color": ["gray81", "gray20"],
                    "border_color": ["gray65", "gray28"]
                  },
                  "CTkButton": {
                    "corner_radius": 6,
                    "border_width": 0,
                    "fg_color": ["#3B8ED0", "#1F6AA5"],
                    "hover_color": ["#36719F", "#144870"],
                    "border_color": ["#3E454A", "#949A9F"],
                    "text_color": ["#DCE4EE", "#DCE4EE"],
                    "text_color_disabled": ["gray74", "gray60"]
                  },
                  "CTkLabel": {
                    "corner_radius": 0,
                    "fg_color": "transparent",
                    "text_color": ["gray10", "#DCE4EE"]
                  },
                  "CTkEntry": {
                    "corner_radius": 6,
                    "border_width": 2,
                    "fg_color": ["#F9F9FA", "#343638"],
                    "border_color": ["#979DA2", "#565B5E"],
                    "text_color":["gray10", "#DCE4EE"],
                    "placeholder_text_color": ["gray52", "gray62"]
                  },
                  "CTkCheckbox": {
                    "corner_radius": 6,
                    "border_width": 3,
                    "fg_color": ["#3B8ED0", "#1F6AA5"],
                    "border_color": ["#3E454A", "#949A9F"],
                    "hover_color": ["#3B8ED0", "#1F6AA5"],
                    "checkmark_color": ["#DCE4EE", "gray90"],
                    "text_color": ["gray10", "#DCE4EE"],
                    "text_color_disabled": ["gray60", "gray45"]
                  },
                  "CTkSwitch": {
                    "corner_radius": 1000,
                    "border_width": 3,
                    "button_length": 0,
                    "fg_color": ["#939BA2", "#4A4D50"],
                    "progress_color": ["#3B8ED0", "#1F6AA5"],
                    "button_color": ["gray36", "#D5D9DE"],
                    "button_hover_color": ["gray20", "gray100"],
                    "text_color": ["gray10", "#DCE4EE"],
                    "text_color_disabled": ["gray60", "gray45"]
                  },
                  "CTkRadiobutton": {
                    "corner_radius": 1000,
                    "border_width_checked": 6,
                    "border_width_unchecked": 3,
                    "fg_color": ["#3B8ED0", "#1F6AA5"],
                    "border_color": ["#3E454A", "#949A9F"],
                    "hover_color": ["#36719F", "#144870"],
                    "text_color": ["gray10", "#DCE4EE"],
                    "text_color_disabled": ["gray60", "gray45"]
                  },
                  "CTkProgressBar": {
                    "corner_radius": 1000,
                    "border_width": 0,
                    "fg_color": ["#939BA2", "#4A4D50"],
                    "progress_color": ["#3B8ED0", "#1F6AA5"],
                    "border_color": ["gray", "gray"]
                  },
                  "CTkSlider": {
                    "corner_radius": 1000,
                    "button_corner_radius": 1000,
                    "border_width": 6,
                    "button_length": 0,
                    "fg_color": ["#939BA2", "#4A4D50"],
                    "progress_color": ["gray40", "#AAB0B5"],
                    "button_color": ["#3B8ED0", "#1F6AA5"],
                    "button_hover_color": ["#36719F", "#144870"]
                  },
                  "CTkOptionMenu": {
                    "corner_radius": 6,
                    "fg_color": ["#3B8ED0", "#1F6AA5"],
                    "button_color": ["#36719F", "#144870"],
                    "button_hover_color": ["#27577D", "#203A4F"],
                    "text_color": ["#DCE4EE", "#DCE4EE"],
                    "text_color_disabled": ["gray74", "gray60"]
                  },
                  "CTkComboBox": {
                    "corner_radius": 6,
                    "border_width": 2,
                    "fg_color": ["#F9F9FA", "#343638"],
                    "border_color": ["#979DA2", "#565B5E"],
                    "button_color": ["#979DA2", "#565B5E"],
                    "button_hover_color": ["#6E7174", "#7A848D"],
                    "text_color": ["gray10", "#DCE4EE"],
                    "text_color_disabled": ["gray50", "gray45"]
                  },
                  "CTkScrollbar": {
                    "corner_radius": 1000,
                    "border_spacing": 4,
                    "fg_color": "transparent",
                    "button_color": ["gray55", "gray41"],
                    "button_hover_color": ["gray40", "gray53"]
                  },
                  "CTkSegmentedButton": {
                    "corner_radius": 6,
                    "border_width": 2,
                    "fg_color": ["#979DA2", "gray29"],
                    "selected_color": ["#3B8ED0", "#1F6AA5"],
                    "selected_hover_color": ["#36719F", "#144870"],
                    "unselected_color": ["#979DA2", "gray29"],
                    "unselected_hover_color": ["gray70", "gray41"],
                    "text_color": ["#DCE4EE", "#DCE4EE"],
                    "text_color_disabled": ["gray74", "gray60"]
                  },
                  "CTkTextbox": {
                    "corner_radius": 6,
                    "border_width": 0,
                    "fg_color": ["#F9F9FA", "#1D1E1E"],
                    "border_color": ["#979DA2", "#565B5E"],
                    "text_color":["gray10", "#DCE4EE"],
                    "scrollbar_button_color": ["gray55", "gray41"],
                    "scrollbar_button_hover_color": ["gray40", "gray53"]
                  },
                  "CTkScrollableFrame": {
                    "label_fg_color": ["gray78", "gray23"]
                  },
                  "DropdownMenu": {
                    "fg_color": ["gray90", "gray20"],
                    "hover_color": ["gray75", "gray28"],
                    "text_color": ["gray10", "gray90"]
                  },
                  "CTkFont": {
                    "macOS": {
                      "family": "SF Display",
                      "size": 13,
                      "weight": "normal"
                    },
                    "Windows": {
                      "family": "Roboto",
                      "size": 13,
                      "weight": "normal"
                    },
                    "Linux": {
                      "family": "Roboto",
                      "size": 13,
                      "weight": "normal"
                    }
                  }
                }


    #--------------------Widget Type and Content--------------------#
    
    widgets = {'CTk':['fg_color'],
             'CTkToplevel':['fg_color'],
             'CTkFrame':['fg_color', 'top_fg_color', 'border_color'],
             'CTkButton':['fg_color','hover_color','border_color','text_color','text_color_disabled'],
             'CTkCheckbox':["fg_color", "border_color", "hover_color","checkmark_color", "text_color",
                            "text_color_disabled"],
             'CTkEntry':['fg_color','text_color','border_color','placeholder_text_color'],
             'CTkLabel':['fg_color', 'text_color'], 
             'CTkProgressBar':['fg_color','progress_color','border_color'],
             'CTkSlider':["fg_color", "progress_color", "button_color", "button_hover_color"],
             'CTkSwitch':["fg_Color", "progress_color", "button_color", "button_hover_color",
                          "text_color", "text_color_disabled"],
             'CTkOptionMenu':["fg_color", "button_color", "button_hover_color","text_color",
                              "text_color_disabled"],
             'CTkComboBox':["fg_color", "border_color", "button_color", "button_hover_color",
                            "text_color", "text_color_disabled"],
             'CTkScrollbar':["fg_color", "button_color", "button_hover_color"],
             'CTkRadiobutton':["fg_color", "border_color", "hover_color", "text_color", "text_color_disabled"],
             'CTkTextbox':["fg_color", "border_color", "text_color", "scrollbar_button_color",
                           "scrollbar_button_hover_color"],
             'CTkSegmentedButton':["fg_color", "selected_color", "selected_hover_color", "unselected_color",
                                   "unselected_hover_color", "text_color", "text_color_disabled"],
             'CTkScrollableFrame':["label_fg_color"],
             'DropdownMenu':["fg_color", "hover_color", "text_color"]}

    widgetlist = [key for key in widgets] # This is a dynamic list of all the widget type
    current = widgetlist[0] # This is the current widget type selected

    for i in json_data:
        for key, value in json_data.get(i).items():
            if value=="transparent":
                json_data[i][key] = ["transparent", "transparent"]
            
    def __init__(self):
        
        #--------------------Main root Window--------------------#
        super().__init__()
        customtkinter.set_default_color_theme("blue")
        self.title("CustomTkinter ThemeMaker")
        self.geometry("500x450")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.grid_columnconfigure((0,1,2,3,4,5), weight=1)
        self.grid_rowconfigure(2, weight=1)
        
        self.frame_info = customtkinter.CTkFrame(master=self, height=80)
        self.frame_info.grid(row=0, column=0, columnspan=6, sticky="nswe", padx=20, pady=20)
        self.frame_info.grid_columnconfigure(0, weight=1)

        self.widget_type = customtkinter.CTkLabel(master=self.frame_info, text=self.current, corner_radius=10, width=200, height=20,
                                        fg_color=("white", "gray38"))
        self.widget_type.grid(row=0, column=0, sticky="nswe", padx=80, pady=20)

        self.left_button = customtkinter.CTkButton(master=self.frame_info, text="<", width=20, height=20, corner_radius=10,
                                        fg_color=("white", "gray38"), command=self.change_mode_left)
        self.left_button.grid(row=0, column=0, sticky="nsw", padx=20, pady=20)

        self.right_button = customtkinter.CTkButton(master=self.frame_info, text=">", width=20, height=20, corner_radius=10,
                                        fg_color=("white", "gray38"), command=self.change_mode_right)
        self.right_button.grid(row=0, column=0, sticky="nse", padx=20, pady=20)

        self.menu = customtkinter.CTkOptionMenu(master=self, fg_color=("white", "gray38"), button_color=("white", "gray38"),
                                         height=30, values=list(self.widgets.items())[0][1], command=self.update)   
        self.menu.grid(row=1, column=0, columnspan=6, sticky="nswe", padx=20)

        self.button_light = customtkinter.CTkButton(master=self, height=100, width=200, corner_radius=10, border_color="white",
                                         text_color="grey50", border_width=2, text="Light", hover=False, command=self.change_color_light)
        self.button_light.grid(row=2, column=0, sticky="nswe", columnspan=3, padx=(20,5), pady=20)
    
        self.button_dark = customtkinter.CTkButton(master=self, height=100, width=200, corner_radius=10, border_color="white",
                                         text_color="gray80", border_width=2, text="Dark", hover=False,
                                         command=self.change_color_dark)
        self.button_dark.grid(row=2, column=3, sticky="nswe", columnspan=3, padx=(5,20), pady=20)

        self.button_load = customtkinter.CTkButton(master=self, height=40, width=110, text="Load Theme", command=self.load)
        self.button_load.grid(row=3, column=0,  columnspan=2, sticky="nswe", padx=(20,5), pady=(0,20))

        self.button_export = customtkinter.CTkButton(master=self, height=40, width=110, text="Save Theme", command=self.save)
        self.button_export.grid(row=3, column=2,  columnspan=2, sticky="nswe", padx=(5,5), pady=(0,20))
    
        self.button_reset = customtkinter.CTkButton(master=self, height=40, width=110, text="Reset", command=self.reset)
        self.button_reset.grid(row=3, column=4,  columnspan=2, sticky="nswe", padx=(5,20), pady=(0,20))

        self.quick_test = customtkinter.CTkButton(master=self, height=40, width=110, text="QUICK TEST", command=self.test)
        self.quick_test.grid(row=4, column=0, columnspan=6, sticky="nswe", padx=20, pady=(0,20))
        
        self.update(None)


    #--------------------class App Functions--------------------#

    # Function for changing current widget type wih right button
    def change_mode_right(self):
        self.widgetlist.append(self.widgetlist.pop(0))
        self.current = self.widgetlist[0]
        self.widget_type.configure(text=self.current)
        self.menu.configure(values=self.widgets[self.current])
        self.menu.set(self.widgets[self.current][0])
        self.update(self.menu.get())
        
    # Function for changing current widget type with left button  
    def change_mode_left(self):
        self.widgetlist.insert(0, self.widgetlist.pop())
        self.current = self.widgetlist[0]
        self.widget_type.configure(text=self.current)
        self.menu.configure(values=self.widgets[self.current])
        self.menu.set(self.widgets[self.current][0])
        self.update(self.menu.get())
        
    # Function for updating the contents and their colors
    def update(self, value):
        for i in self.json_data[self.current]:
            if i==self.menu.get():
                if (self.json_data[self.current][i])[0]!="transparent":
                    self.button_light.configure(fg_color=(self.json_data[self.current][i])[0])
                else:
                    self.button_light.configure(fg_color="transparent")
                if (self.json_data[self.current][i])[1]!="transparent":    
                    self.button_dark.configure(fg_color=(self.json_data[self.current][i])[1])
                else:
                    self.button_dark.configure(fg_color="transparent")
                    
    # Function for choosing the color for Light mode of the theme
    def change_color_light(self):
        default = self.button_light._apply_appearance_mode(self.button_light._fg_color)
        if default=="transparent":
            default = "white"
        color1 = askcolor(title="Choose color for "+self.menu.get()+" (Light)",
                          initialcolor=default)
        if color1[1] is not None:
            self.button_light.configure(fg_color=color1[1])
            for i in self.json_data[self.current]:
                if i==self.menu.get():
                    (self.json_data[self.current][i])[0] = color1[1]
                    
    # Function for choosing the color for Dark mode of the theme                
    def change_color_dark(self):
        default = self.button_dark._apply_appearance_mode(self.button_dark._fg_color)
        if default=="transparent":
            default = "white"      
        color2 = askcolor(title="Choose color for "+self.menu.get()+" (Dark)",
                          initialcolor=default)
        if color2[1] is not None:
            self.button_dark.configure(fg_color=color2[1])
            for i in self.json_data[self.current]:
                if i==self.menu.get():
                    (self.json_data[self.current][i])[1] = color2[1]

    # Function for exporting the theme file         
    def save(self):
        save_file = tkinter.filedialog.asksaveasfilename(initialfile="Untitled.json", filetypes=[('json', ['*.json']),('All Files', '*.*')], defaultextension=".json")
        try:
            if save_file:
                with open(save_file, "w") as f:
                    json.dump(self.json_data, f, indent=2)
                    f.close()
                tkinter.messagebox.showinfo("Exported!","Theme saved successfully!")
        except:
            tkinter.messagebox.showerror("Error!","Something went wrong!")
            
    # Function for loading the theme file            
    def load(self):
        global json_data
        open_json = tkinter.filedialog.askopenfilename(filetypes=[('json', ['*.json']),('All Files', '*.*')])
        try:
            if open_json:
                with open(open_json) as f:
                    self.json_data = json.load(f)
                    f.close()
                    
            for i in self.json_data:
                for key, value in self.json_data.get(i).items():
                    if value=="transparent":
                        self.json_data[i][key] = ["transparent", "transparent"]
                        
            self.update(self.menu.get())
        except:
            tkinter.messagebox.showerror("Error!","Unable to load the theme file!")
        

    # Function for resetting the current colors of the widget to null (default value)
    def reset(self):
        for i in self.json_data[self.current]:
            if i==self.menu.get():
                self.json_data[self.current][i][0] = "transparent"
                self.button_light.configure(fg_color="transparent")
                self.json_data[self.current][i][1] = "transparent"
                self.button_dark.configure(fg_color="transparent")

    # Function for quick testing the theme
    def test(self):
        DIRPATH = f"{__file__}".replace("ThemeMaker.py", "")
        if not os.path.exists(os.path.join(DIRPATH, "CTkExample.py")):
            tkinter.messagebox.showerror("Sorry!","Cannot test, example is missing!")
            return

        with open("CTkTheme_test.json", "w") as f:
            json.dump(self.json_data, f, indent=2)
            f.close()
          
        ch = os.path.join(DIRPATH, "CTkExample.py")
        if platform.system().lower() == "darwin":
          subprocess.run(["python3", ch])
        elif platform.system().lower() == "windows":
          subprocess.run(["python", ch])
        else:
          tkinter.messagebox.showerror("Sorry!","Operating system not supported!")
          return

    # Closing function   
    def on_closing(self):
        quit = tkinter.messagebox.askokcancel(title="Exit?", message= "Do you want to exit?")
        if quit:
            self.destroy()
            
if __name__ == "__main__":
    app = App()
    app.mainloop()
