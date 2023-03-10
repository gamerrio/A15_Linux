import tkinter
import tkinter.messagebox
import customtkinter as ctk

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("green")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("A15 Controller")
        self.geometry(f"{500}x{580}")

        self.grid_columnconfigure((1,2),weight=1)

        #Led Status
        self.Status_label = ctk.CTkLabel(self,text="Led Status:",font=ctk.CTkFont(size=20, weight="bold"))
        self.Status_label.grid(row=0,column=0,padx=20, pady=(20, 10))
        self.radiobutton_1 = ctk.CTkRadioButton(self, text="ON", value=1)
        self.radiobutton_2 = ctk.CTkRadioButton(self, text="OFF", value=0)
        self.radiobutton_1.grid(row=1,column=0,padx=20, pady=(20, 10))
        self.radiobutton_2.grid(row=1,column=1, pady=(20, 10))

        #Led Modes
        self.LedMode = ctk.CTkLabel(self,text="Led Mode:",font=ctk.CTkFont(size=20, weight="bold"))
        self.LedMode.grid(row=3,column=0,padx=20, pady=(20, 10))
        self.ModeCombobox = ctk.CTkOptionMenu(self,values=["DPI", "Multi Color", "Rainbow", "Floe Light", "Waltz", "Four Seasons"])
        self.ModeCombobox.grid(row=4,column=0,padx=20, pady=(20, 10))
        self.LedSpeed = ctk.CTkLabel(self,text="Led Speed:",font=ctk.CTkFont(size=20, weight="bold"))
        self.LedSpeed.grid(row=5,column=0,padx=20, pady=(20, 10))        
        self.LedSpeedSlider = ctk.CTkSlider(self, from_=0, to=8)
        self.LedSpeedSlider.grid(row=6,column=0,padx=20, pady=(20, 10))

        self.DPILabel = ctk.CTkLabel(self,text="DPI Speed:",font=ctk.CTkFont(size=20, weight="bold"))
        self.DPILabel.grid(row=7,column=0,padx=20, pady=(20, 10))        
        self.DPISlider = ctk.CTkSlider(self, from_=0, to=8)
        self.DPISlider.grid(row=8,column=0,padx=20, pady=(20, 10))
        self.ApplyButton = ctk.CTkButton(self, text="Apply")
        self.ApplyButton.grid(row=9,column=0,padx=20, pady=(20, 10))
        

if __name__ == "__main__":
    app = App()
    app.mainloop()