import tkinter as tk
from main import WebAutomation

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Automation GUI")

        #Login Frame
        self.loginFrame = tk.Frame(self.root)
        self.loginFrame.pack(padx=10, pady=10)

        tk.Label(self.loginFrame, text='Username').grid(row=0, column=0, sticky="w")
        self.entry_username = tk.Entry(self.loginFrame)
        self.entry_username.grid(row=0, column=1, sticky="ew")

        tk.Label(self.loginFrame, text='Password').grid(row=1, column=0, sticky="w")
        self.entry_password = tk.Entry(self.loginFrame)
        self.entry_password.grid(row=1, column=1, sticky="ew")

        #Submission Frame
        self.formFrame = tk.Frame(self.root)
        self.formFrame.pack(padx=10, pady=10)

        tk.Label(self.formFrame, text='Full Name').grid(row=0, column=0, sticky="w")
        self.entry_fname = tk.Entry(self.formFrame)
        self.entry_fname.grid(row=0, column=1, sticky="ew")

        tk.Label(self.formFrame, text='Email id').grid(row=1, column=0, sticky="w")
        self.entry_email = tk.Entry(self.formFrame)
        self.entry_email.grid(row=1, column=1, sticky="ew")

        tk.Label(self.formFrame, text='Current Address').grid(row=2, column=0, sticky="w")
        self.entry_curradr = tk.Entry(self.formFrame)
        self.entry_curradr.grid(row=2, column=1, sticky="ew")

        tk.Label(self.formFrame, text='Permanent Address').grid(row=3, column=0, sticky="w")
        self.entry_permadr = tk.Entry(self.formFrame)
        self.entry_permadr.grid(row=3, column=1, sticky="ew")

        #Buttons
        self.buttonFrame = tk.Frame(self.root)
        self.buttonFrame.pack(padx=10, pady=10)

        tk.Button(self.buttonFrame, text="Submit", command=self.submit_data).grid(row=0, column=0, padx=5)
        tk.Button(self.buttonFrame, text="Close", command=self.close_browser).grid(row=0, column=1, padx=5)

    def submit_data(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        fname = self.entry_fname.get()
        emailid = self.entry_email.get()
        curradr = self.entry_curradr.get()
        permadr = self.entry_permadr.get()


    def close_browser(self):
        pass

root = tk.Tk()
app = App(root)
root.mainloop()