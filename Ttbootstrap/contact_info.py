import ttkbootstrap as ttk
from ttkbootstrap.constants import * # Nos puede ayudar a prevenir errores de tipeo

app = ttk.Window(themename="superhero")
app.geometry("600x500")

label = ttk.Label(app, text="Contact Information")
label.pack(pady=30)
label.config(font=("Arial", 20, "bold"))

name_frame = ttk.Frame(app)
name_frame.pack(pady=15, padx=10, fill="x")
ttk.Label(name_frame, text="Name").pack(side="left", padx=5)
ttk.Entry(name_frame).pack(side="left", fill="x", expand=True, padx=5)

email_frame = ttk.Frame(app)
email_frame.pack(pady=15, padx=10, fill="x")
ttk.Label(email_frame, text="Email").pack(side="left", padx=5)
ttk.Entry(email_frame).pack(side="left", fill="x", expand=True, padx=5)

checkbox_frame = ttk.Frame(app)
checkbox_frame.pack(pady=15, padx=10, fill="x")
ttk.Checkbutton(checkbox_frame, bootstyle="round-toggle", text="Remember info?").pack(side="left", padx=10)

button_frame = ttk.Frame(app)
button_frame.pack(pady=50, padx=10, fill="x")
ttk.Button(button_frame, text="Submit", bootstyle=SUCCESS).pack(side="left", padx=10)
ttk.Button(button_frame, text="Cancel", bootstyle=SECONDARY).pack(side="left", padx=10)

app.mainloop()