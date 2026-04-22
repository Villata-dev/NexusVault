import customtkinter as ctk
from security import encrypt_password
from database import init_db, save_credential

class NexusApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("NexusVault")
        self.geometry("400x550")
        ctk.set_appearance_mode("dark")
        
        init_db() # Crea la base de datos al abrir
        
        # --- UI MINIMALISTA ---
        self.label = ctk.CTkLabel(self, text="🔒 NEXUS VAULT", font=("Inter", 24, "bold"))
        self.label.pack(pady=40)

        self.btn_unlock = ctk.CTkButton(self, text="Desbloquear Bóveda", 
                                        fg_color="#10b981", height=45,
                                        command=self.unlock)
        self.btn_unlock.pack(pady=20)

    def unlock(self):
        print("Buscando Huella / FaceID...")
        # Aquí irá el paso a la lista de contraseñas

if __name__ == "__main__":
    app = NexusApp()
    app.mainloop()