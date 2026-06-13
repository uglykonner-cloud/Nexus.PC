import tkinter as tk
from tkinter import font
import time
from datetime import datetime

class WindowsBootScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Windows Boot Screen")
        self.root.geometry("1024x768")
        self.root.configure(bg="#000080")  # Windows classic blue
        self.root.resizable(False, False)
        
        # Center the window on screen
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        
        self.user_name = tk.StringVar()
        self.create_boot_screen()
    
    def create_boot_screen(self):
        """Create the boot screen UI"""
        # Main frame
        main_frame = tk.Frame(self.root, bg="#000080")
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Windows logo text (simulate)
        logo_font = font.Font(family="Arial", size=36, weight="bold")
        logo_label = tk.Label(
            main_frame,
            text="Windows",
            font=logo_font,
            fg="white",
            bg="#000080"
        )
        logo_label.pack(pady=(0, 30))
        
        # Loading animation frame
        loading_frame = tk.Frame(main_frame, bg="#000080")
        loading_frame.pack(pady=(20, 40))
        
        loading_text = tk.Label(
            loading_frame,
            text="Starting up...",
            font=("Arial", 14),
            fg="white",
            bg="#000080"
        )
        loading_text.pack(pady=10)
        
        # Progress bar simulation
        progress_canvas = tk.Canvas(
            loading_frame,
            width=300,
            height=20,
            bg="#000080",
            highlightthickness=1,
            highlightbackground="white"
        )
        progress_canvas.pack(pady=10)
        self.progress_rect = progress_canvas.create_rectangle(0, 0, 0, 20, fill="white")
        
        # Animate progress
        self.animate_progress(progress_canvas, loading_text)
    
    def animate_progress(self, canvas, loading_label):
        """Animate the progress bar"""
        total_steps = 40
        for i in range(total_steps):
            width = (300 / total_steps) * (i + 1)
            canvas.coords(self.progress_rect, 0, 0, width, 20)
            self.root.update()
            time.sleep(0.05)
        
        loading_label.config(text="Ready for login")
        self.root.after(500, self.show_login_screen)
    
    def show_login_screen(self):
        """Replace boot screen with login screen"""
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Login frame
        login_frame = tk.Frame(self.root, bg="#000080")
        login_frame.pack(expand=True, fill="both", padx=40, pady=40)
        
        # Welcome text
        welcome_font = font.Font(family="Arial", size=16, weight="bold")
        welcome_label = tk.Label(
            login_frame,
            text="Welcome",
            font=welcome_font,
            fg="white",
            bg="#000080"
        )
        welcome_label.pack(pady=(0, 20))
        
        # Name input section
        input_frame = tk.Frame(login_frame, bg="#000080")
        input_frame.pack(pady=20)
        
        name_label = tk.Label(
            input_frame,
            text="Enter your name:",
            font=("Arial", 12),
            fg="white",
            bg="#000080"
        )
        name_label.pack(pady=(0, 10))
        
        # Input field
        name_entry = tk.Entry(
            input_frame,
            textvariable=self.user_name,
            font=("Arial", 14),
            width=30,
            bg="white",
            fg="black"
        )
        name_entry.pack(pady=10)
        name_entry.focus()
        
        # Bind Enter key to submit
        name_entry.bind("<Return>", lambda e: self.submit_name())
        
        # Submit button
        submit_btn = tk.Button(
            input_frame,
            text="Login",
            font=("Arial", 12, "bold"),
            command=self.submit_name,
            bg="#0078D4",
            fg="white",
            padx=20,
            pady=10,
            relief="raised",
            cursor="hand2"
        )
        submit_btn.pack(pady=20)
        
        # Clock display
        clock_label = tk.Label(
            login_frame,
            text="",
            font=("Arial", 10),
            fg="white",
            bg="#000080"
        )
        clock_label.pack(pady=(40, 0))
        self.update_clock(clock_label)
    
    def update_clock(self, clock_label):
        """Update the clock display"""
        current_time = datetime.now().strftime("%I:%M:%S %p")
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        clock_label.config(text=f"{current_time}\n{current_date}")
        self.root.after(1000, lambda: self.update_clock(clock_label))
    
    def submit_name(self):
        """Handle name submission"""
        name = self.user_name.get().strip()
        if name:
            self.show_welcome_message(name)
        else:
            self.user_name.set("")
    
    def show_welcome_message(self, name):
        """Show welcome message after login"""
        for widget in self.root.winfo_children():
            widget.destroy()
        
        message_frame = tk.Frame(self.root, bg="#000080")
        message_frame.pack(expand=True, fill="both", padx=40, pady=40)
        
        welcome_msg_font = font.Font(family="Arial", size=20, weight="bold")
        welcome_msg = tk.Label(
            message_frame,
            text=f"Welcome, {name}!",
            font=welcome_msg_font,
            fg="white",
            bg="#000080"
        )
        welcome_msg.pack(pady=20)
        
        loading_msg = tk.Label(
            message_frame,
            text="Preparing your desktop...",
            font=("Arial", 12),
            fg="white",
            bg="#000080"
        )
        loading_msg.pack(pady=20)
        
        # Simulate desktop loading
        self.root.after(2000, lambda: self.show_desktop(name))
    
    def show_desktop(self, name):
        """Show the desktop after login"""
        for widget in self.root.winfo_children():
            widget.destroy()
        
        desktop_frame = tk.Frame(self.root, bg="#1e90ff")
        desktop_frame.pack(expand=True, fill="both")
        
        # Taskbar
        taskbar = tk.Frame(self.root, bg="#0c0c0c", height=40)
        taskbar.pack(side="bottom", fill="x")
        
        taskbar_label = tk.Label(
            taskbar,
            text="Windows Nexus PC",
            font=("Arial", 10),
            fg="white",
            bg="#0c0c0c"
        )
        taskbar_label.pack(side="left", padx=10, pady=8)
        
        # Main desktop content
        desktop_label = tk.Label(
            desktop_frame,
            text=f"Hello, {name}!",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#1e90ff"
        )
        desktop_label.pack(expand=True, pady=20)
        
        info_label = tk.Label(
            desktop_frame,
            text="Your desktop is ready",
            font=("Arial", 14),
            fg="white",
            bg="#1e90ff"
        )
        info_label.pack(pady=10)
        
        # Exit button
        exit_btn = tk.Button(
            desktop_frame,
            text="Exit",
            font=("Arial", 12),
            command=self.root.quit,
            bg="#D9534F",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        exit_btn.pack(pady=20)

def main():
    root = tk.Tk()
    app = WindowsBootScreen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
