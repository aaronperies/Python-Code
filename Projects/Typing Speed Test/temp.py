import tkinter as tk
import time
import threading
import random

#this program is designed to be used as a way of calculating a person's typing speed
class TypeSpeedGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing Speed Application")
        self.root.geometry("800x600")
        
        self.texts = open("Text_Samples.txt", "r").read().split("\n")
        
        self.frame = tk.Frame(self.root)
        
        self.sample_label = tk.Label(self.frame, text = random.choice(self.texts), font = ("Helvetica", 18))
        self.sample_label.grid(row=0, column = 0, columnspan=2, padx=5, pady=10)
        
        self.input_entry = tk.Entry(self.frame, width = 40, font = ("Helvetica", 24))
        self.input_entry.grid(row = 1, column = 0, columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<KeyPress>", self.start)
        
        self.speed_label = tk.Label(self.frame, text = "Speed: \n0.00 CPS\n0.00 CPM", font = ("Helvetica", 18))
        self.speed_label.grid(row=2, column = 0, columnspan=2, padx=5, pady=10)
        
        self.reset_button = tk.Button(self.frame, text = "Reset", command=self.reset)
        self.reset_button.grid(row=3, column = 0, columnspan=2, padx=5, pady=10)
        
        self.frame.pack(expand=True)
        
        self.counter = 0
        self.running = False
        
        self.root.mainloop()
        
    #this function is meant to be called as soon as the typing begins
    def start(self, event):
        if not self.running:
            if not event.keycode in [16,17,18]:
                self.running = True
                t = threading.Thread(target = self.time_thread)
                t.start()
                
        if not self.sample_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
            
        else:
            self.input_entry.config(fg="black")
            
        if self.input_entry.get() == self.sample_label.cget('text')[:-1]:
            self.running = False
            self.input_entry.config(fg="green")
    
    #this function will perform all the speed calculations once typing has begun
    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            cps = len(self.input_entry.get()) / self.counter
            cpm = cps * 60
            self.speed_label.config(text=f"Speed: \n{cps:.2f} CPS\n{cpm:.2f} CPM")
            
    def reset(self):
        
    

TypeSpeedGUI()