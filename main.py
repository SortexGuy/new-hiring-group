import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, scrolledtext
# import db_manager
# from datetime import datetime

BG_COLOR = "#0F172A"
FG_COLOR = "#E2E8F0"
ENTRY_BG = "#1E293B"
BUTTON_BG = "#334155"
ACCENT_COLOR = "#9333EA"
ACCENT_ACTIVE = "#A855F7"
FONT_NORMAL = ("Segoe UI", 10)
FONT_BOLD = ("Segoe UI", 10, "bold")
FONT_TITLE = ("Segoe UI", 16, "bold")
FONT_MENU_TITLE = ("Segoe UI", 12, "bold")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión Hiring Group")
        self.geometry("950x700")
        self.minsize(800, 600)
        self.configure(bg=BG_COLOR)
        self.conexion = None
        self.usuario_actual = None
        self.rol_actual = None
        self.setup_styles()
        self.container = tk.Frame(self, bg=BG_COLOR)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        # self.show_frame(LoginFrame)

    def setup_styles(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure(
            "TButton",
            background=BUTTON_BG,
            foreground=FG_COLOR,
            borderwidth=0,
            font=FONT_BOLD,
            padding=10,
        )
        style.map(
            "TButton",
            background=[("active", ACCENT_ACTIVE)],
            foreground=[("active", FG_COLOR)],
        )
        style.configure("Accent.TButton", background=ACCENT_COLOR, foreground=FG_COLOR)
        style.map("Accent.TButton", background=[("active", ACCENT_ACTIVE)])
        style.configure(
            "Treeview",
            background=ENTRY_BG,
            foreground=FG_COLOR,
            fieldbackground=ENTRY_BG,
            rowheight=25,
            font=FONT_NORMAL,
        )
        style.map(
            "Treeview",
            background=[("selected", ACCENT_COLOR)],
            foreground=[("selected", FG_COLOR)],
        )
        style.configure(
            "Treeview.Heading",
            background=BUTTON_BG,
            foreground=FG_COLOR,
            font=FONT_BOLD,
            relief="flat",
            padding=5,
        )
        style.map("Treeview.Heading", background=[("active", BUTTON_BG)])
        style.configure(
            "TCombobox",
            fieldbackground=ENTRY_BG,
            background=BUTTON_BG,
            foreground=FG_COLOR,
            arrowcolor=FG_COLOR,
            selectbackground=ENTRY_BG,
            selectforeground=FG_COLOR,
        )
        self.option_add("*TCombobox*Listbox.background", ENTRY_BG)
        self.option_add("*TCombobox*Listbox.foreground", FG_COLOR)
        self.option_add("*TCombobox*Listbox.selectBackground", ACCENT_COLOR)
        self.option_add("*TCombobox*Listbox.font", FONT_NORMAL)

    # def show_frame(self, FrameClass):
    #     for widget in self.container.winfo_children():
    #         widget.destroy()
    #     frame = FrameClass(parent=self.container, controller=self)
    #     frame.grid(row=0, column=0, sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()
