import RPi.GPIO as GPIO
import tkinter as tk

ledRed = 11
ledGreen = 13
ledBlue = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledRed, GPIO.OUT)
GPIO.setup(ledGreen, GPIO.OUT)
GPIO.setup(ledBlue, GPIO.OUT)

class Window(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)  
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1) 
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)       

        self.currentState = 0

        # widget can take all window
        self.pack(fill=tk.BOTH, expand=1)

        redButton = tk.Button(self, text="Red", command=lambda: self.turn_on_led_callback(led=ledRed))
        greenButton = tk.Button(self, text="Green", command=lambda: self.turn_on_led_callback(led=ledGreen))
        blueButton = tk.Button(self, text="Blue", command=lambda: self.turn_on_led_callback(led=ledBlue))

        # create exit button, link it to exit_callback()
        exitButton = tk.Button(self, text="Exit", command=self.exit_callback)

        # place button at (0,0)
        redButton.grid(row=0,column=0)
        greenButton.grid(row=0,column=1)
        blueButton.grid(row=0,column=2)
        exitButton.grid(row=1, column=1)

    def turn_on_led_callback(self, led):
        if self.currentState != 0:
            GPIO.output(self.currentState, GPIO.LOW)
        GPIO.output(led, GPIO.HIGH)
        self.currentState = led

    def exit_callback(self):
        if self.currentState != 0:
            GPIO.output(self.currentState, GPIO.LOW)
        GPIO.cleanup()
        exit()
        
root = tk.Tk()
app = Window(root)
root.wm_title("Task 5.2C: Make a GUI!")
root.geometry("320x320")
root.mainloop()