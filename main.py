import customtkinter as ctk
import re

class NexusApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("NexusVault")
        self.geometry("400x600")
        ctk.set_appearance_mode("dark")
        
        self.label = ctk.CTkLabel(self, text="🔒 NUEVA CREDENCIAL", font=("Inter", 20, "bold"))
        self.label.pack(pady=30)

        # Campo de entrada de contraseña
        self.pass_entry = ctk.CTkEntry(self, placeholder_text="Ingresa la contraseña", show="*", width=300)
        self.pass_entry.pack(pady=10)
        self.pass_entry.bind("<KeyRelease>", self.check_strength) # Detecta cada tecla

        # Contenedor de la barra de seguridad
        self.strength_frame = ctk.CTkFrame(self, fg_color="gray30", height=8, width=300)
        self.strength_frame.pack(pady=5)
        
        # La barra que crece y cambia de color
        self.strength_bar = ctk.CTkFrame(self.strength_frame, fg_color="red", height=8, width=0)
        self.strength_bar.place(x=0, y=0)

        self.strength_text = ctk.CTkLabel(self, text="Fortaleza: Muy débil", font=("Inter", 12))
        self.strength_text.pack()

    def check_strength(self, event):
        password = self.pass_entry.get()
        strength = 0
        
        # Lógica de validación
        if len(password) >= 8: strength += 1
        if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password): strength += 1
        if re.search(r"\d", password): strength += 1
        if re.search(r"[ !@#$%^&*(),.?\":{}|<>]", password): strength += 1

        # Actualizar visualmente (Ancho y Color)
        colors = ["#ef4444", "#f59e0b", "#3b82f6", "#10b981"] # Rojo, Naranja, Azul, Verde
        texts = ["Muy débil", "Débil", "Media", "Fuerte"]
        
        # Calcular ancho (máximo 300)
        new_width = (strength + 1) * 60 if password else 0
        if strength >= 3 and len(password) >= 12: 
            color = colors[3]
            txt = "Muy Fuerte"
            new_width = 300
        else:
            color = colors[min(strength, 3)]
            txt = texts[min(strength, 3)]

        self.strength_bar.configure(width=new_width, fg_color=color)
        self.strength_text.configure(text=f"Fortaleza: {txt}", text_color=color)

if __name__ == "__main__":
    app = NexusApp()
    app.mainloop()