import customtkinter as ctk
import time
import control_bd
from PIL import Image

delete_icon = Image.open("./img/delete.png")
delete_icon = ctk.CTkImage(dark_image= delete_icon, size=(20, 20))

add_icon = Image.open("./img/add.png")
add_icon = ctk.CTkImage(dark_image= add_icon, size=(20, 20))

back_icon = Image.open("./img/back.png")
back_icon = ctk.CTkImage(dark_image= back_icon, size=(20, 20))

edit_icon = Image.open("./img/edit.png")
edit_icon = ctk.CTkImage(dark_image= edit_icon, size=(20, 20))

search_icon = Image.open("./img/search.png")
search_icon = ctk.CTkImage(dark_image= search_icon, size=(20, 20))

error = Image.open("./img/error.png")
error = ctk.CTkImage(dark_image=error, size=(20,20))

check = Image.open("./img/check.png")
check = ctk.CTkImage(dark_image=check, size=(20,20))

warning = Image.open("./img/warning.png")
warning = ctk.CTkImage(dark_image=warning, size = (20,20))




class LoginFrame(ctk.CTkFrame):
    
    def __init__(self, master: ctk.CTk=None):
        super().__init__(master)
        self.master = master

        window_height = master.winfo_height()  # Altura de la ventana principal
        window_width = master.winfo_width()    # Ancho de la ventana principal

        frame_width = int(window_width * 0.95)
        frame_height = int(window_height * 0.9)

        icon_ini = Image.open("./img/energia.png")
        icon_ini = ctk.CTkImage(light_image=icon_ini, size=(20, 20))

        self.configure(width=frame_width, height=frame_height, corner_radius=15)
        self.place(relx=0.5, rely=0.5, anchor="center")


        entry_width = int(frame_width * 0.4)
        button_width = int(frame_width * 0.3)


        self.welcome_label = ctk.CTkLabel(
            self,
            text="Bienvenido",
            font=ctk.CTkFont(size=40, weight="bold")
        )
        self.welcome_label.place(relx=0.5, rely=0.15, anchor="center")

        # Label para URI
        self.uri_label = ctk.CTkLabel(self, text="URI")
        self.uri_label.place(relx=0.5, rely=0.25, anchor="center")

        # Entry para URI
        self.uri_entry = ctk.CTkEntry(self, width=entry_width)
        self.uri_entry.insert(0, "neo4j://127.0.0.1:7687")
        self.uri_entry.place(relx=0.5, rely=0.30, anchor="center")

        # Label para Usuario
        self.user_label = ctk.CTkLabel(self, text="Usuario")
        self.user_label.place(relx=0.5, rely=0.37, anchor="center")

        #entry para Usuario
        self.user_entry = ctk.CTkEntry(self, width=entry_width)
        self.user_entry.insert(0, "neo4j")
        self.user_entry.place(relx=0.5, rely=0.42, anchor="center")

        # Label para Password
        self.pass_label = ctk.CTkLabel(self, text="Password")
        self.pass_label.place(relx=0.5, rely=0.49, anchor="center")

        #entry para Password
        self.pass_entry = ctk.CTkEntry(self, show="*", width=entry_width)
        self.pass_entry.insert(0, "12345678")
        self.pass_entry.place(relx=0.5, rely=0.54, anchor="center")

        # Label para mostrar el estado de conexión
        self.void_label = ctk.CTkLabel(
            self,
            text="",
            font=ctk.CTkFont(size=16, weight="bold")
        )

        self.void_label.place(relx=0.5, rely=0.65, anchor="center")

        self.button = ctk.CTkButton(
            self,
            text="Conectar",
            font=ctk.CTkFont(size=16),
            command=self.conectar,
            image=icon_ini,
            compound="right",
            width=button_width
        )
        self.button.place(relx=0.5, rely=0.85, anchor="center")

    def conectar(self):
        user = self.user_entry.get()
        password = self.pass_entry.get()
        uri = self.uri_entry.get()

        self.void_label.configure(text="Conectando...")
        self.void_label.update_idletasks()  # Actualiza la interfaz para mostrar el mensaje inmediatamente
        time.sleep(0.3)

        mensaje, error = control_bd.conectar(uri, user, password)

        if(mensaje is None or error is not None):
            self.void_label.configure(text=error, text_color="#bf4345", image=error)
            self.void_label.update_idletasks()
            return
        
        # Divide el mensaje en varias líneas si es muy largo
        max_line_length = 70
        if len(mensaje) > max_line_length:
            # Divide el mensaje en líneas de máximo max_line_length caracteres
            lineas = [mensaje[i:i+max_line_length] for i in range(0, len(mensaje), max_line_length)]
            mensaje_multilinea = "\n".join(lineas)
            self.void_label.configure(text=mensaje_multilinea)
        else:
            self.void_label.configure(text=mensaje)

        self.void_label.update_idletasks()  # Actualiza la interfaz para mostrar el mensaje inmediatamente
        time.sleep(0.3)
        if mensaje is not None:
            self.destroy()
            MainFrame(master=self.master)

class MainFrame(ctk.CTkFrame):

    def __init__(self, master: ctk.CTk = None):
        super().__init__(master)

        self.master = master

        window_height = master.winfo_height()
        window_width = master.winfo_width()

        frame_width = int(window_width * 0.95)
        frame_height = int(window_height * 0.9)

        self.frames : ctk.CTkFrame = []

        icon_ruta = Image.open("./img/correr.png")
        icon_ruta = ctk.CTkImage(dark_image=icon_ruta, size=(24, 24))

        icon_settings = Image.open("./img/settings.png")
        icon_settings = ctk.CTkImage(dark_image=icon_settings, size=(24, 24))

        icon_add = Image.open("./img/add.png")
        icon_add = ctk.CTkImage(dark_image=icon_add, size=(24, 24))

        sitio_icon = Image.open("./img/sitio.png")
        sitio_icon = ctk.CTkImage(dark_image=sitio_icon, size=(24,24))

        salir_icon = Image.open("./img/salida.png")
        salir_icon = ctk.CTkImage(dark_image=salir_icon, size = (24,24))

        self.configure(
            width=frame_width,
            height=frame_height,
            corner_radius=15,
            fg_color="#1e1e1e"  # Fondo oscuro
        )
        self.place(relx = 0.5, rely = 0.08, anchor = "n")


        nav_width = int(frame_width * 0.2)
        content_width = int(frame_width * 0.8)

        # Navigation bar
        self.nav_frame = ctk.CTkFrame(
            self,
            width=nav_width,
            height=frame_height,
            corner_radius=15,
            fg_color="#1e1e1e"
        )
        self.nav_frame.place(relx=0, rely=0.01, relheight=1, anchor="nw")

        self.add_button = ctk.CTkButton(
            self.nav_frame,
            text="   Añadir",
            font=ctk.CTkFont(size=14),  # Espaciado a la izquierda
            width=nav_width,
            height=40,
            fg_color="transparent",
            border_width=0,
            corner_radius=0,
            image=icon_add,
            hover_color="#33393f",
            text_color="#f5f5f5",
            command=self.show_add
        )
        self.add_button.place(relx=0, rely=0.05, relwidth=1, anchor="w")


        self.config_button = ctk.CTkButton(
            self.nav_frame,
            text="  Modificar",  # Espaciado a la izquierda
            font=ctk.CTkFont(size=14),
            width=nav_width,
            height=40,
            fg_color="transparent",
            border_width=0,
            corner_radius=0,
            anchor="center",
            image=icon_settings,
            hover_color="#33393f",
            text_color="#f5f5f5",
            command=self.show_config
        )
        self.config_button.place(relx=0, rely=0.12, relwidth=1, anchor="w")

        self.ruta_button = ctk.CTkButton(
            self.nav_frame,
            text="  Buscar Ruta",
            font=ctk.CTkFont(size=14),  # Espaciado a la izquierda
            width=nav_width,
            height=40,
            fg_color="transparent",
            border_width=0,
            corner_radius=0,
            image=icon_ruta,
            anchor="center",
            hover_color="#33393f",
            text_color="#f5f5f5",
            command=self.show_buscarRuta
        )
        self.ruta_button.place(relx=0, rely=0.19, relwidth=1, anchor="w")

        self.rel_button = ctk.CTkButton(
            self.nav_frame,
            text="  Relaciones de rutas",
            font=ctk.CTkFont(size=14),  # Espaciado a la izquierda
            width=nav_width,
            height=40,
            fg_color="transparent",
            border_width=0,
            corner_radius=0,
            image=sitio_icon,
            anchor="center",
            hover_color="#33393f",
            text_color="#f5f5f5",
            command=self.show_rel
        )
        self.rel_button.place(relx=0, rely=0.26, relwidth=1, anchor="w")

        self.salir_button= ctk.CTkButton(
            self.nav_frame,
            text="  Salir",
            font=ctk.CTkFont(size=14),  # Espaciado a la izquierda
            width=nav_width,
            height=40,
            fg_color="transparent",
            border_width=0,
            corner_radius=0,
            image=salir_icon,
            anchor="center",
            hover_color="#33393f",
            text_color="#f5f5f5",
            command=self.salir
        )
        self.salir_button.place(relx=0, rely=0.94, relwidth=1, anchor="w")


        # Content frame (right side)
        self.content_frame = ctk.CTkFrame(
            self,
            width=content_width,
            height=frame_height,
            corner_radius=15,
            fg_color= "#2e2e2e"  # Fondo más claro para el contenido
        )

        self.content_frame.place(relx=0.2, rely=0, relheight=1, relwidth=0.79, anchor="nw")

        self.frame_config = FrameConfig(self.content_frame)
        self.frames.append(self.frame_config)

        self.frame_ruta = FrameRuta(self.content_frame)
        self.frames.append(self.frame_ruta)

        self.frame_add = FrameAdd(master=self.content_frame)
        self.frames.append(self.frame_add)

        self.frame_rel = FrameRelacion(master=self.content_frame)
        self.frames.append(self.frame_rel)

        self.show_add()

    def ocultar_frames(self):

        for frame in self.frames:
            if frame is self.frame_ruta:
                if frame.frame_nodos:
                    frame.frame_nodos.place_forget()

            frame.place_forget()

    def show_add(self):
        self.ocultar_frames()

        self.frame_add.place(relx=0, rely=0, relwidth=1, relheight=1)

    def show_rel(self):
        self.ocultar_frames()
        self.frame_rel.place(relx=0, rely=0, relwidth=1, relheight=1)

    def show_config(self):

        self.ocultar_frames()
        
        self.frame_config.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.frame_config.actualizar_combobox()

    def salir(self):
        self.destroy()
        LoginFrame(master=self.master)

    def show_buscarRuta(self):
        self.ocultar_frames()
        self.frame_ruta.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.frame_ruta.actualizar_comboboxes()

class FrameRuta(ctk.CTkFrame):
    def __init__(self, master: ctk.CTkFrame = None):
        super().__init__(master)

        master.update_idletasks()  # Ensure geometry info is updated
        window_height = master.winfo_height()
        window_width = master.winfo_width()

        button_width = int(window_width * 0.3)
        entry_width = int(window_width * 0.4)

        self.label = ctk.CTkLabel(
            self,
            text="Buscar ruta más optima",
            font=ctk.CTkFont(size=30, weight="bold")
        )
        self.label.place(relx=0.5, rely=0.05, anchor="n")

        zonas, _ = control_bd.consultar_zonas()
        zonas.insert(0, "")

        centros = control_bd.consultar_centros()
        centros.insert(0, "")

        self.label_zona = ctk.CTkLabel(self, text="Ingrese el nombre de una zona: ", font=ctk.CTkFont(size=16))
        self.label_zona.place(relx=0.25, rely=0.2, anchor="center")

        self.entry_zona = ctk.CTkComboBox(self, width= int(entry_width*0.8), values = zonas)
        self.entry_zona.place(relx=0.25, rely=0.25, anchor="center")


        self.label_centro = ctk.CTkLabel(self, text="Ingrese el nombre de un centro: ", font=ctk.CTkFont(size=16))
        self.label_centro.place(relx=0.75, rely=0.20, anchor="center")

        self.entry_centro = ctk.CTkComboBox(self, width= int(entry_width*0.8), values = centros)
        self.entry_centro.place(relx=0.75, rely=0.25, anchor="center")


        self.label_cbTrafico = ctk.CTkLabel(self, text="Máximo tráfico permitido: ", font=ctk.CTkFont(size=16))
        self.label_cbTrafico.place(relx=0.25, rely=0.35, anchor="center")

        self.cb_Trafico = ctk.CTkComboBox(self, width = int(entry_width*0.8), values=["Alto", "Medio", "Bajo"])
        self.cb_Trafico.place(relx=0.25, rely=0.40, anchor="center")


        self.label_cbCapacidad = ctk.CTkLabel(self, text="Capacidad de la vía: ", font=ctk.CTkFont(size=16))
        self.label_cbCapacidad.place(relx=0.75, rely=0.35, anchor="center")

        self.cb_Capacidad = ctk.CTkComboBox(self, width = int(entry_width*0.8), values=["Cualquiera", "<=20 (Baja)", "<=60 (Media)", "<=100 (Alta)"])
        self.cb_Capacidad.place(relx=0.75, rely=0.40, anchor="center")


        self.checkbox_status = ctk.CTkCheckBox(self, text="Permitir vías cerradas", font=ctk.CTkFont(size=16), checkbox_height=20, checkbox_width= 20)
        self.checkbox_status.place(relx=0.50, rely=0.50, anchor="center")

        self.label_resultado = ctk.CTkLabel(self,text="",font=ctk.CTkFont(size=14), text_color='#bf4345' )
        self.label_resultado.place(relx=0.5, rely=0.55, anchor="n")  # Ancla arriba, no al centro

        self.button = ctk.CTkButton(
            self,
            text= "Buscar ruta",
            command=self.buscar,
            image= search_icon,
            compound="right",
            width=button_width
        )

        self.button.place(relx=0.5, rely=0.90, anchor="center")
        self.frame_nodos = None

    def buscar(self):
        nombre_zona = self.entry_zona.get()

        centro = self.entry_centro.get()

        trafico = self.cb_Trafico.get()
        trafico = "0" if (trafico == "Bajo") else "1" if (trafico == "Medio") else "2"

        capacidad = self.cb_Capacidad.get().split()[0]

        status = self.checkbox_status.get()

        record = control_bd.buscar_centro(
            nombre_zona, centro,
            capacidad= None if (capacidad == "Cualquiera") else capacidad,
            trafico=f"<= {trafico}",
            status= ">= 0" if (status == 1) else "< 1"
        )

        if record:
            self.place_forget()
            self.frame_nodos = FrameNodos(master=self.master, origin = self, record=record)

        else: 
            self.label_resultado.configure(text= "No se encontró ningun resultado.")

    def actualizar_comboboxes(self):
        zonas, _ = control_bd.consultar_zonas()
        zonas.insert(0, "")
        self.entry_zona.configure(values= zonas)
        centros = control_bd.consultar_centros()
        centros.insert(0, "")
        self.entry_centro.configure(values= centros)

class FrameNodos(ctk.CTkFrame):

    def __init__(self, master, record, origin):
        super().__init__(master)
        self.master = master
        self.origin = origin
        self.record = record

        self.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.update_idletasks()
        width = self.winfo_width() or 400
        height = self.winfo_height() or 350

        self.text = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=16))
        self.text.place(relx=0.5, rely=0.01, anchor="n")

        self.canvas = ctk.CTkCanvas(self, width=width, height=height, bg="#2e2e2e", highlightthickness=0)
        self.canvas.place(relx=0.5, rely=0.06, anchor="n", relwidth=0.95, relheight=0.85)

        self.dibujar_nodos(width, height)
        
        self.button_volver = ctk.CTkButton(self, text="Volver", image= back_icon, command=self.volver)
        self.button_volver.place(relx=0.5, rely=0.98, anchor="s")

    def dibujar_nodos(self, width, height):
        self.canvas.delete("all")
        camino = self.record["camino"]
        trafico = self.record["trafico"]
        status_calles = self.record["status_calles"]
        tiempo_total = self.record["tiempo_total"]
        tiempo_min = self.record["tiempo_min"]

        self.text.configure(text=f"Tiempo total: {tiempo_total}")
        n = len(camino)
        if n == 0:
            return

        cx = int(width * 0.2)
        margin_y = 50
        available_height = height - margin_y * 2 - 80
        dy = available_height // max(1, n - 1) if n > 1 else 0
        r = int(min(30, width // 8, dy // 2) * 0.85)  

        def draw_text_with_outline(x, y, text, font, fill, outline="black"):
            offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for dx, dy in offsets:
                self.canvas.create_text(x + dx, y + dy, text=text, fill=outline, font=font)
                self.canvas.create_text(x, y, text=text, fill=fill, font=font)

        for i, nodo in enumerate(camino):
            cy = margin_y + i * dy
            self.canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill="#3a7ebf", outline="#cccccc", width=2)
            draw_text_with_outline(cx, cy - r - 8, nodo, ("Arial", 12, "bold"), "white", outline="#222222")

            
            if i < n - 1:
                cy_next = margin_y + (i + 1) * dy
                self.canvas.create_line(cx, cy + r, cx, cy_next - r, fill="#cccccc", width=3)
                status_str = "Abierto" if (int(status_calles[i]) == 0) else "Cerrado"
                trafico_str = "Bajo" if trafico[i] == 0 else "Medio" if trafico[i] == 1 else "Alto"
                label = f"{status_str} | Tráfico {trafico_str} | Tiempo: {tiempo_min[i]} min"
                label_x = int((cx + r + 80)*1.7)
                draw_text_with_outline(label_x, (cy + cy_next) // 2, label, ("Arial", 10), "#f5f5f5", outline="#222222")

    def volver(self):
        self.place_forget()
        self.origin.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.origin.actualizar_comboboxes()


class FrameConfig(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk=None):

        super().__init__(master)
        self.master = master

        master.update_idletasks() 
        window_height = master.winfo_height()
        window_width = master.winfo_width()

        button_width = int(window_width * 0.3)
        entry_width = int(window_width * 0.4)

        self.selector = ctk.CTkComboBox(
            self,
            width=entry_width,
            values=["Seleccione una opción", "Modificar zona", "Modificar centro", "Modificar vía"],
            command=self.on_option_selected
        )
        self.selector.place(relx=0.5, rely=0.08, anchor="center")


        self.frame = ctk.CTkFrame(
            self,
            width=int(window_width * 0.9),
            height=int(window_height * 0.88),
            bg_color="#2e2e2e",
            )
        self.frame.place(relx=0.5, rely=0.55, anchor="center")


        self.frames : ctk.CTkFrame = []

        self.frameVia = FrameConfigVia(master=self.frame)
        self.frames.append(self.frameVia)

        self.frameZona = FrameConfigZona(master=self.frame)
        self.frames.append(self.frameZona)

        self.frameCentro = FrameConfigCentro(master = self.frame)
        self.frames.append(self.frameCentro)
    
    def actualizar_combobox(self):
        for frame in self.frames:
            frame.actualizar_combobox()

    def ocultar_frames(self):

        for frame in self.frames:
            if frame is not None:
                frame.place_forget()

    def on_option_selected(self, value):

        if value == "Seleccione una opción":
            return
        
        self.ocultar_frames()

        if value == "Modificar zona":
            self.frameZona.place(relx=0, rely=0, relwidth=1, relheight=1)

        elif value == "Modificar centro":
            self.frameCentro.place(relx=0, rely=0, relwidth=1, relheight=1)

        elif value == "Modificar vía":
            self.frameVia.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        self.update_idletasks()

class FrameConfigZona(ctk.CTkFrame):
    def __init__(self, master: ctk.CTkFrame = None):
        super().__init__(master)

        master.update_idletasks()  # Ensure geometry info is updated
        window_height = master.winfo_height()
        window_width = master.winfo_width()

        button_width = int(window_width * 0.3)
        entry_width = int(window_width * 0.4)

        self.label = ctk.CTkLabel(
            self,
            text="Modificar zonas",
            font=ctk.CTkFont(size=30, weight="bold")
        )
        self.label.place(relx=0.5, rely=0.05, anchor="n")

        self.label_zona = ctk.CTkLabel(self, text="Seleccione una zona: ", font=ctk.CTkFont(size=16))
        self.label_zona.place(relx=0.5, rely=0.20, anchor="center")

        self.nombres_zonas, self.tipos = control_bd.consultar_zonas()
        self.nombres_zonas.insert(0, "Seleccione una zona")


        self.entry_zonas = ctk.CTkComboBox(
            self,
            width=entry_width,
            values=self.nombres_zonas,
            command=self.on_zona_selected
        )

        self.entry_zonas.place(relx=0.5, rely=0.25, anchor="center")

        self.label_nombre = ctk.CTkLabel(self, text="Nombre de la zona:", font=ctk.CTkFont(size=16))
        self.label_nombre.place(relx=0.5, rely=0.35, anchor="center")

        self.entry_nombre = ctk.CTkEntry(self, width=entry_width)
        self.entry_nombre.configure(placeholder_text="Ingrese el nombre de la zona")
        self.entry_nombre.place(relx=0.5, rely=0.4, anchor="center")


        self.combo_tipo_zona = ctk.CTkComboBox(
            self,
            width=entry_width,
            values=["Seleccione el tipo de zona", "rural", "comercial"]
        )
        self.combo_tipo_zona.place(relx=0.5, rely=0.5, anchor="center")

        # Botón para añadir la zona
        self.button_add = ctk.CTkButton(
            self,
            text="Modificar",
            width=button_width,
            image= edit_icon,
            command=self.añadir_zona
        )
        self.button_add.place(relx=0.25, rely=0.8, anchor="center")

        self.button_delete = ctk.CTkButton(
            self,
            text="Eliminar",
            width=button_width,
            image=delete_icon,
            command=self.eliminar_zona
        )
        self.button_delete.place(relx=0.75, rely=0.8, anchor="center")

        # Label para mostrar el resultado
        self.label_resultado = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=16), text_color='#bf4345')
    
    def on_zona_selected(self, value):

        value = self.entry_zonas.get()

        if value == "Seleccione una zona":
            return

        self.seleccion_nombre = value
        self.seleccion_tipo =  self.tipos[ self.nombres_zonas.index(value) - 1 ] 
        self.entry_nombre.delete(0, "end")
        self.entry_nombre.insert(0, value)
        self.combo_tipo_zona.set(self.seleccion_tipo)

    def actualizar_combobox(self):
        self.nombres_zonas, self.tipos = control_bd.consultar_zonas()
        self.nombres_zonas.insert(0, "Seleccione una zona")
        self.entry_zonas.configure(values=self.nombres_zonas)
        self.update_idletasks()

    def añadir_zona(self):
        nombre = self.entry_nombre.get()
        tipo_zona = self.combo_tipo_zona.get()

        if not nombre:
            self.label_resultado.configure(text="El nombre no puede estar vacío.", text_color='#bf4345')
            return

        if tipo_zona == "Seleccione el tipo de zona":
            self.label_resultado.configure(text="Debe seleccionar un tipo de zona.", text_color='#bf4345')
            return

        res = control_bd.modificar_zona(self.seleccion_nombre, self.seleccion_tipo, nombre, tipo_zona)
        if res:
            self.label_resultado.configure(text=f"Zona {self.seleccion_nombre} modificada correctamente.", text_color='#e4e3e2')
        else:
            self.label_resultado.configure(text="Error al añadir la zona.", text_color='#bf4345')
        self.entry_nombre.delete(0, "end")

        self.actualizar_combobox()
        self.update_idletasks()

    def eliminar_zona(self):
        if self.seleccion_nombre == "Seleccione una zona":
            self.label_resultado.configure(text="Debe seleccionar una zona.", text_color='#bf4345')
            return

        res = control_bd.eliminar_zona(self.seleccion_nombre, self.seleccion_tipo)
        if res:
            self.label_resultado.configure(text=f"Zona {self.seleccion_nombre} eliminada correctamente.", text_color='#e4e3e2')
        else:
            self.label_resultado.configure(text="Error al eliminar la zona.", text_color='#bf4345')
        self.entry_nombre.delete(0, "end")

        self.actualizar_combobox()
        self.update_idletasks()

class FrameConfigCentro(ctk.CTkFrame):
    def __init__(self, master: ctk.CTkFrame = None):
        super().__init__(master)

        master.update_idletasks()  # Ensure geometry info is updated
        window_height = master.winfo_height()
        window_width = master.winfo_width()

        button_width = int(window_width * 0.3)
        entry_width = int(window_width * 0.4)

        self.label = ctk.CTkLabel(
            self,
            text="Modificar centros",
            font=ctk.CTkFont(size=30, weight="bold")
        )
        self.label.place(relx=0.5, rely=0.05, anchor="n")

        self.label_centro = ctk.CTkLabel(self, text="Seleccione un centro: ", font=ctk.CTkFont(size=16))
        self.label_centro.place(relx=0.5, rely=0.20, anchor="center")

        self.nombres_centros = control_bd.consultar_centros()
        self.nombres_centros.sort()
        self.nombres_centros.insert(0, "Seleccione un centro")

        self.entry_centros = ctk.CTkComboBox(
            self,
            width=entry_width,
            values=self.nombres_centros,
            command=self.on_centro_selected
        )

        self.entry_centros.place(relx=0.5, rely=0.25, anchor="center")

        self.label_nombre = ctk.CTkLabel(self, text="Nombre del centro:", font=ctk.CTkFont(size=16))
        self.label_nombre.place(relx=0.5, rely=0.35, anchor="center")

        self.entry_nombre = ctk.CTkEntry(self, width=entry_width)
        self.entry_nombre.configure(placeholder_text="Ingrese el nombre del centro")
        self.entry_nombre.place(relx=0.5, rely=0.4, anchor="center")

        # Botón para añadir el centro
        self.button_add = ctk.CTkButton(
            self,
            text="Modificar",
            width=button_width,
            image=edit_icon,
            command=self.añadir_centro
        )
        self.button_add.place(relx=0.25, rely=0.8, anchor="center")

        self.button_delete = ctk.CTkButton(
            self,
            text="Eliminar",
            width=button_width,
            image= delete_icon,
            command=self.eliminar_centro
        )
        self.button_delete.place(relx=0.75, rely=0.8, anchor="center")

        # Label para mostrar el resultado
        self.label_resultado = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=16), text_color='#bf4345')
        self.label_resultado.place(relx=0.5, rely=0.65, anchor="center")

    def añadir_centro(self):
        nombre = self.entry_nombre.get()
        if self.seleccion == "Seleccione un centro":
            self.label_resultado.configure(text="Debe seleccionar un centro.", text_color='#bf4345')
            return

        if not nombre:
            self.label_resultado.configure(text="El nombre no puede estar vacío.", text_color='#bf4345')
            return
        
        if not nombre.startswith("Centro "):
            nombre = "Centro " + nombre

        res = control_bd.modificar_centro(self.seleccion, nombre)
        if res:
            self.label_resultado.configure(text=f"{self.seleccion} modificado correctamente a {nombre}.", text_color='#e4e3e2')
        else:
            self.label_resultado.configure(text="Error al añadir el centro.", text_color='#bf4345')

        self.entry_nombre.delete(0, "end")
        self.update_idletasks()
        self.actualizar_combobox()

    def eliminar_centro(self):

        if self.seleccion == "Seleccione un centro":
            self.label_resultado.configure(text="Debe seleccionar un centro.", text_color='#bf4345')
            return

        res = control_bd.eliminar_centro(self.seleccion)
        if res:
            self.label_resultado.configure(text=f"{self.seleccion} eliminado correctamente.", text_color='#e4e3e2')
        else:
            self.label_resultado.configure(text="Error al eliminar el centro.", text_color='#bf4345')

        self.entry_nombre.delete(0, "end")
        self.update_idletasks()
        self.actualizar_combobox()

    def on_centro_selected(self, value):
        if value == "Seleccione un centro":
            return

        self.seleccion = value
        self.entry_nombre.delete(0, "end")
        self.entry_nombre.insert(0, value)

    def actualizar_combobox(self):
        self.nombres_centros = control_bd.consultar_centros()
        self.nombres_centros.sort()
        self.nombres_centros.insert(0, "Seleccione un centro")
        self.entry_centros.configure(values=self.nombres_centros)
        self.update_idletasks()

class FrameConfigVia(ctk.CTkFrame):
    def __init__(self, master: ctk.CTkFrame = None):
        super().__init__(master)

        master.update_idletasks()  # Ensure geometry info is updated
        window_height = master.winfo_height()
        window_width = master.winfo_width()

        button_width = int(window_width * 0.3)
        entry_width = int(window_width * 0.4)

        
        self.label = ctk.CTkLabel(
            self,
            text="Modificar vías",
            font=ctk.CTkFont(size=30, weight="bold")
        )
        self.label.place(relx=0.5, rely=0.05, anchor="n")

        self.label_via = ctk.CTkLabel(self, text="Seleccione una vía: ", font=ctk.CTkFont(size=16))
        self.label_via.place(relx=0.5, rely=0.20, anchor="center")
        
        self.nombres_vias, self.vias = control_bd.consultar_vias()
        self.nombres_vias.sort()
        self.nombres_vias.insert(0, "Seleccione una vía")
        
        self.entry_vias = ctk.CTkComboBox(
            self,
            width=entry_width,
            values=self.nombres_vias,
            command=self.on_via_selected
        )

        self.entry_vias.place(relx=0.5, rely=0.25, anchor="center")

        self.bidireccional = ctk.CTkCheckBox(self, text= "Cambio bidireccional", font=ctk.CTkFont(size=16), checkbox_height=20, checkbox_width= 20)
        self.bidireccional.place(relx=0.5, rely=0.325, anchor="center")

        # Entry para ingresar solo números (por ejemplo, tiempo)
        self.label_tiempo = ctk.CTkLabel(self, text = "Tiempo estimado: ", font= ctk.CTkFont(size=16))
        self.label_tiempo.place(relx=0.75, rely=0.40, anchor="center")

        self.entry_tiempo = ctk.CTkEntry(self, width=int(entry_width*0.8))
        self.entry_tiempo.configure(placeholder_text="Ingrese un número")
        self.entry_tiempo.place(relx=0.75, rely=0.45, anchor="center")


        self.label_tiempo = ctk.CTkLabel(self, text = "Capacidad máxima: ", font= ctk.CTkFont(size=16))
        self.label_tiempo.place(relx=0.25, rely=0.40, anchor="center")

        self.entry_capacidad = ctk.CTkEntry(self, width=int(entry_width*0.8))
        self.entry_capacidad.configure(placeholder_text="Ingrese un número")
        self.entry_capacidad.place(relx=0.25, rely=0.45, anchor="center")

        # Validación para permitir solo números
        def validate_number(P):
            return P.isdigit() or P == ""
        vcmd = (self.register(validate_number), "%P")
        self.entry_tiempo.configure(validate="key", validatecommand=vcmd)
        self.entry_capacidad.configure(validate="key", validatecommand=vcmd)

        
        self.label_trafico = ctk.CTkLabel(self, text= "Estado del tráfico: ", font= ctk.CTkFont(size=16))
        self.label_trafico.place(relx=0.25, rely=0.525, anchor="center")
        self.entry_trafico = ctk.CTkComboBox(self,width=int(entry_width*0.8),values = ["","Alto", "Medio", "Bajo"])
        self.entry_trafico.place(relx=0.25, rely=0.575, anchor="center")

        self.entry_status = ctk.CTkCheckBox(self, text= "Cerrado", font=ctk.CTkFont(size=16), checkbox_height=24, checkbox_width= 24)
        self.entry_status.place(relx=0.75, rely=0.575, anchor="center")

        self.button = ctk.CTkButton(
            self,
            text= "Modificar",
            command=self.añadir,
            image=edit_icon,
            width=button_width
        )
        self.button.place(relx=0.25, rely=0.8, anchor="center")

        self.button_delete = ctk.CTkButton(
            self,
            text="Eliminar",
            width=button_width,
            image=delete_icon,
            command=self.eliminar
        )
        self.button_delete.place(relx=0.75, rely=0.8, anchor="center")


        self.label = ctk.CTkLabel(self, text = "", font = ctk.CTkFont(size=16), text_color='#e4e3e2')
        self.label.place(relx=0.5, rely=0.65, anchor="center")

    def on_via_selected(self, value):
            
            if(value == "Seleccione una vía"):
                return
            indice = self.nombres_vias.index(value)
            self.n_origen, self.n_fin = self.nombres_vias[indice].split(" - ")
            via = self.vias[indice-1]

            self.entry_capacidad.delete(0, "end")
            self.entry_capacidad.insert(0, via["capacidad"])

            self.entry_tiempo.delete(0, "end")
            self.entry_tiempo.insert(0, via["tiempo_minutos"])
            if via["status"] == 1:
                self.entry_status.select()
            else:
                self.entry_status.deselect()

            self.entry_trafico.set("Bajo" if(via["trafico_actual"] == 0) else "Medio" if(via["trafico_actual"] == 1) else "Alto")

    def actualizar_combobox(self):
        self.nombres_vias, self.vias = control_bd.consultar_vias()
        self.nombres_vias.sort()
        self.nombres_vias.insert(0, "Seleccione una vía")
        self.entry_vias.configure(values=self.nombres_vias)
        self.update_idletasks()

    def añadir(self):
        
        capacidad = self.entry_capacidad.get()
        if(capacidad == ""):
            capacidad = "0"
        
        tiempo = self.entry_tiempo.get()
        if(tiempo == ""):
            tiempo = "0"
        trafico = self.entry_trafico.get()
        trafico = "0" if (trafico == "Bajo") else "1" if (trafico == "Medio") else "2"

        res = control_bd.modificar_via(n_origen= self.n_origen, n_fin= self.n_fin , tiempo= tiempo, trafico= trafico, capacidad=capacidad, status=self.entry_status.get())

        if(res):
            self.label.configure(text = "Añadido", text_color= '#e4e3e2')
        else:
            self.label.configure(text = "Error al modificar", text_color= '#bf4345')
            
        self.update_idletasks()

        if(self.bidireccional.get()):
            res = control_bd.modificar_via(n_origen= self.n_fin, n_fin= self.n_origen , tiempo= tiempo, trafico= trafico, capacidad=capacidad, status=self.entry_status.get())
            if(res):
                self.label.configure(text = "Añadido en ambas direcciones", text_color= '#e4e3e2')
            else:
                self.label.configure(text = "Error al modificar", text_color= '#bf4345')

            self.update_idletasks()
        self.actualizar_combobox()

    def eliminar(self):
        
        capacidad = self.entry_capacidad.get()
        if(capacidad == ""):
            capacidad = "0"
        
        tiempo = self.entry_tiempo.get()
        if(tiempo == ""):
            tiempo = "0"
        trafico = self.entry_trafico.get()
        trafico = "0" if (trafico == "Bajo") else "1" if (trafico == "Medio") else "2"

        res = control_bd.eliminar_via(n_origen= self.n_origen, n_fin= self.n_fin , tiempo= tiempo, trafico= trafico, capacidad=capacidad, status=self.entry_status.get())

        if(res):
            self.label.configure(text = "Eliminado", text_color= '#e4e3e2')
        else:
            self.label.configure(text = "Error al eliminar", text_color= '#bf4345')
            
        self.update_idletasks()

        if(self.bidireccional.get()):
            res = control_bd.modificar_via(n_origen= self.n_fin, n_fin= self.n_origen , tiempo= tiempo, trafico= trafico, capacidad=capacidad, status=self.entry_status.get())
            if(res):
                self.label.configure(text = "Eliminada en ambas direcciones", text_color= '#e4e3e2')
            else:
                self.label.configure(text = "Error al eliminar", text_color= '#bf4345')

            self.update_idletasks()
        self.actualizar_combobox()


class FrameAdd(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk=None):

        super().__init__(master)
        self.master = master

        master.update_idletasks() 
        window_height = master.winfo_height()
        window_width = master.winfo_width()

        button_width = int(window_width * 0.3)
        entry_width = int(window_width * 0.4)

        self.selector = ctk.CTkComboBox(
            self,
            width=entry_width,
            values=["Seleccione una opción", "Añadir zona", "Añadir centro", "Añadir vía"],
            command=self.on_option_selected
        )
        self.selector.place(relx=0.5, rely=0.08, anchor="center")


        self.frame = ctk.CTkFrame(
            self,
            width=int(window_width * 0.9),
            height=int(window_height * 0.88),
            bg_color="#2e2e2e",
            )
        self.frame.place(relx=0.5, rely=0.55, anchor="center")


        self.frames : ctk.CTkFrame = []

        self.frameVia = FrameAddVia(master=self.frame)
        self.frames.append(self.frameVia)

        self.frameZona = FrameAddZona(master=self.frame)
        self.frames.append(self.frameZona)

        self.frameCentro = FrameAddCentro(master=self.frame)
        self.frames.append(self.frameCentro)
        
    def ocultar_frames(self):

        for frame in self.frames:
            if frame is not None:
                frame.place_forget()

    def on_option_selected(self, value):

        if value == "Seleccione una opción":
            return
        
        self.ocultar_frames()

        if value == "Añadir zona":
            self.frameZona.place(relx=0, rely=0, relwidth=1, relheight=1)

        elif value == "Añadir centro":
            self.frameCentro.place(relx=0, rely=0, relwidth=1, relheight=1)

        elif value == "Añadir vía":
            self.frameVia.place(relx=0, rely=0, relwidth=1, relheight=1)
            self.frameVia.actualizar_combobox()
        
        self.update_idletasks()

class FrameAddZona(ctk.CTkFrame):

    def __init__(self, master: ctk.CTk=None):

        super().__init__(master)
        self.master = master

        master.update_idletasks() 
        window_height = master.winfo_height()
        window_width = master.winfo_width()

        button_width = int(window_width * 0.3)
        entry_width = int(window_width * 0.4)

        self.label = ctk.CTkLabel(self, text="Añadir zona", font=ctk.CTkFont(size=30, weight="bold"))
        self.label.place(relx=0.5, rely=0.05, anchor="n")

        self.entry_zona = ctk.CTkEntry(self, width=entry_width)
        self.entry_zona.configure(placeholder_text="Ingrese el nombre de la zona")
        self.entry_zona.place(relx=0.5, rely=0.2, anchor="center")

        self.label_tipo = ctk.CTkLabel(self, text="Seleccione el tipo de zona:", font=ctk.CTkFont(size=16))
        self.label_tipo.place(relx=0.5, rely=0.35, anchor="center")

        self.combobox_tipo = ctk.CTkComboBox(
            self, 
            width=int(entry_width * 0.8), 
            values=["Seleccione el tipo de zona", "rural", "comercial"]
        )
        self.combobox_tipo.place(relx=0.5, rely=0.4, anchor="center")

        self.button_add = ctk.CTkButton(
            self, text="Añadir",
            command=self.añadir_zona,
            width=button_width,
            image= add_icon
        )
        self.button_add.place(relx=0.5, rely=0.8, anchor="center")

        self.label_resultado = ctk.CTkLabel(
            self, text="",
            font=ctk.CTkFont(size=16),
            text_color='#bf4345')
        self.label_resultado.place(relx=0.5, rely=0.65, anchor="center")

    def añadir_zona(self):

        nombre_zona = self.entry_zona.get()
        tipo_zona = self.combobox_tipo.get()

        if not nombre_zona:
            self.label_resultado.configure(text="El nombre de la zona no puede estar vacío.")
            return
        
        if tipo_zona == "Seleccione el tipo de zona":
            self.label_resultado.configure(text="Debe seleccionar un tipo de zona.")
            return

        if control_bd.añadir_zona(nombre_zona, tipo_zona):
            self.label_resultado.configure(text="Zona añadida correctamente.", text_color='#e4e3e2')
        else:
            self.label_resultado.configure(text="Error al añadir la zona.", text_color='#bf4345')

        self.update_idletasks()
        self.entry_zona.delete(0, "end")

class FrameAddCentro(ctk.CTkFrame):

    def __init__(self, master: ctk.CTk=None):

        super().__init__(master)
        self.master = master

        master.update_idletasks() 
        window_height = master.winfo_height()
        window_width = master.winfo_width()

        button_width = int(window_width * 0.3)
        entry_width = int(window_width * 0.4)

        self.label = ctk.CTkLabel(self, text="Añadir centro", font=ctk.CTkFont(size=30, weight="bold"))
        self.label.place(relx=0.5, rely=0.05, anchor="n")

        self.entry_centro = ctk.CTkEntry(self, width=entry_width)
        self.entry_centro.configure(placeholder_text="Ingrese el nombre del centro")
        self.entry_centro.place(relx=0.5, rely=0.2, anchor="center")

        self.button_add = ctk.CTkButton(
            self,
            text="Añadir",
            command=self.añadir_centro,
            width=button_width,
            image=add_icon
            )
        self.button_add.place(relx=0.5, rely=0.8, anchor="center")

        self.label_resultado = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=16), text_color='#bf4345')
        self.label_resultado.place(relx=0.5, rely=0.65, anchor="center")

    def añadir_centro(self):

        nombre_centro = self.entry_centro.get()

        if not nombre_centro:
            self.label_resultado.configure(text="El nombre del centro no puede estar vacío.")
            return
        
        if not nombre_centro.startswith("Centro "):
            nombre_centro = "Centro " + nombre_centro

        if control_bd.añadir_centro(nombre_centro):
            self.label_resultado.configure(text="Centro añadido correctamente.", text_color='#e4e3e2')
        else:
            self.label_resultado.configure(text="Error al añadir el centro.", text_color='#bf4345')

        self.update_idletasks()
        self.entry_centro.delete(0, "end")

class FrameAddVia(ctk.CTkFrame):

    def __init__(self, master: ctk.CTk=None):

        super().__init__(master)
        self.master = master

        master.update_idletasks() 
        window_height = master.winfo_height()
        window_width = master.winfo_width()

        button_width = int(window_width * 0.3)
        entry_width = int(window_width * 0.4)

        self.label = ctk.CTkLabel(self, text="Añadir vía entre dos nodos", font=ctk.CTkFont(size=30, weight="bold"))
        self.label.place(relx=0.5, rely=0.05, anchor="n")

        # Obtener valores de zonas y centros y combinarlos en un solo arreglo
        zonas, _ = control_bd.consultar_zonas()
        centros = control_bd.consultar_centros()
        opciones = zonas + centros

        self.combo_origen = ctk.CTkComboBox(self, width=int(entry_width * 0.8), values= ["Seleccione un nodo de origen"] + opciones)
        self.combo_origen.place(relx=0.25, rely=0.2, anchor="center")

        self.combo_destino = ctk.CTkComboBox(self, width=int(entry_width * 0.8), values=["Seleccione un nodo de destino"] + opciones)
        self.combo_destino.place(relx=0.75, rely=0.2, anchor="center")

        self.bidireccional = ctk.CTkCheckBox(self, text= "Via bidireccional", font=ctk.CTkFont(size=16), checkbox_height=20, checkbox_width= 20)
        self.bidireccional.place(relx=0.5, rely=0.325, anchor="center")

        # Entry para ingresar solo números (por ejemplo, tiempo)
        self.label_tiempo = ctk.CTkLabel(self, text = "Tiempo estimado: ", font= ctk.CTkFont(size=16))
        self.label_tiempo.place(relx=0.75, rely=0.40, anchor="center")

        self.entry_tiempo = ctk.CTkEntry(self, width=int(entry_width*0.8))
        self.entry_tiempo.configure(placeholder_text="Ingrese un número")
        self.entry_tiempo.place(relx=0.75, rely=0.45, anchor="center")


        self.label_tiempo = ctk.CTkLabel(self, text = "Capacidad máxima: ", font= ctk.CTkFont(size=16))
        self.label_tiempo.place(relx=0.25, rely=0.40, anchor="center")

        self.entry_capacidad = ctk.CTkEntry(self, width=int(entry_width*0.8))
        self.entry_capacidad.configure(placeholder_text="Ingrese un número")
        self.entry_capacidad.place(relx=0.25, rely=0.45, anchor="center")

        # Validación para permitir solo números
        def validate_number(P):
            return P.isdigit() or P == ""
        vcmd = (self.register(validate_number), "%P")
        self.entry_tiempo.configure(validate="key", validatecommand=vcmd)
        self.entry_capacidad.configure(validate="key", validatecommand=vcmd)

        
        self.label_trafico = ctk.CTkLabel(self, text= "Estado del tráfico: ", font= ctk.CTkFont(size=16))
        self.label_trafico.place(relx=0.25, rely=0.525, anchor="center")
        self.entry_trafico = ctk.CTkComboBox(self,width=int(entry_width*0.8),values = ["","Alto", "Medio", "Bajo"])
        self.entry_trafico.place(relx=0.25, rely=0.575, anchor="center")

        self.entry_status = ctk.CTkCheckBox(self, text= "Cerrado", font=ctk.CTkFont(size=16), checkbox_height=24, checkbox_width= 24)
        self.entry_status.place(relx=0.75, rely=0.575, anchor="center")



        self.button_add = ctk.CTkButton(
            self,
            text="Añadir",
            command=self.añadir_via,
            width=button_width,
            image= add_icon
            )
        self.button_add.place(relx=0.5, rely=0.8, anchor="center")

        self.label_resultado = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=16), text_color='#bf4345')
        self.label_resultado.place(relx=0.5, rely=0.65, anchor="center")

    def añadir_via(self):
        origen = self.combo_origen.get()
        destino = self.combo_destino.get()
        
        capacidad = self.entry_capacidad.get()
        if(capacidad == ""):
            self.label_resultado.configure(text="Debe asignar un valor a la capacidad.")
            return
        
        tiempo = self.entry_tiempo.get()
        if(tiempo == ""):
            self.label_resultado.configure(text="Debe asignar un valor al tiempo.")

        trafico = self.entry_trafico.get()
        trafico = "0" if (trafico == "Bajo") else "1" if (trafico == "Medio") else "2"

        status = self.entry_status.get()

        if origen == "Seleccione un nodo de origen" or destino == "Seleccione un nodo de destino":
            self.label_resultado.configure(text="Debe seleccionar un nodo de origen y uno de destino.")
            return

        if origen == destino:
            self.label_resultado.configure(text="El nodo de origen y el nodo de destino no pueden ser el mismo.")
            return

        if control_bd.añadir_via(origen, destino, tiempo, trafico, capacidad, status):
            self.label_resultado.configure(text="Vía añadida correctamente.", text_color='#e4e3e2')
        else:
            self.label_resultado.configure(text="Error al añadir la vía.", text_color='#bf4345')

        if self.bidireccional.get():
            if control_bd.añadir_via(destino, origen, tiempo, trafico, capacidad, status):
                self.label_resultado.configure(text="Vía añadida en ambas direcciones.", text_color='#e4e3e2')
            else:
                self.label_resultado.configure(text="Error al añadir la vía en ambas direcciones.", text_color='#bf4345')

        self.update_idletasks()
        self.combo_origen.set("Seleccione un nodo de origen")
        self.combo_destino.set("Seleccione un nodo de destino")

    def actualizar_combobox(self):
        zonas, _ = control_bd.consultar_zonas()
        centros = control_bd.consultar_centros()
        opciones = zonas + centros
        self.combo_origen.configure(values=["Seleccione un nodo de origen"] + opciones)
        self.combo_destino.configure(values=["Seleccione un nodo de destino"] + opciones)
        self.update_idletasks()

class FrameRelacion(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk=None):

        super().__init__(master)
        self.master = master

        master.update_idletasks() 
        window_height = master.winfo_height()
        window_width = master.winfo_width()

        button_width = int(window_width * 0.3)
        entry_width = int(window_width * 0.4)

        self.label = ctk.CTkLabel(self, text="Relaciones entre zonas", font=ctk.CTkFont(size=30, weight="bold"))
        self.label.place(relx=0.5, rely=0.05, anchor="n")
        
        zonas, _ = control_bd.consultar_zonas()
        centros = control_bd.consultar_centros()
        self.zonas = zonas + centros

        self.combobox = ctk.CTkComboBox(
            self,
            width=entry_width,
            values= ["Seleccione una zona"] + self.zonas,
            command=self.on_option_selected
        )
        self.combobox.place(relx=0.5, rely=0.15, anchor="center")

        # Cambiar a CTkScrollableFrame para permitir scroll
        self.tablas_frame = ctk.CTkScrollableFrame(self, width=int(window_width * 0.9), height=int(window_height * 0.7), fg_color="#232323")
        self.tablas_frame.place(relx=0.5, rely=0.2, anchor="n", relwidth=0.95, relheight=0.78)


    def on_option_selected(self,value):
        if value == "Seleccione una zona":
            return
        
        # Obtener las relaciones de la zona seleccionada
        conectadas, no_conectadas = control_bd.consultar_relaciones(value)

        accesibles = []

        for nodo in no_conectadas:

            camino = control_bd.buscar_camino(nodo, value)
            
            if camino is not None:
                camino["direccion"] = "<-"
                accesibles.append( camino )
            
            camino = control_bd.buscar_camino(value, nodo)
            if camino is not None:
                camino["direccion"] = "->"
                accesibles.append( camino )

        for camino in accesibles:
            origen = camino.get("nodo_origen")
            destino = camino.get("nodo_destino")


            if destino == value:
                camino["nodo_origen"] = value
                camino["nodo_destino"] = origen

            if destino in no_conectadas:
                no_conectadas.remove(destino)



        # Llamar al método para rellenar las tablas con los datos obtenidos
        self.rellenar_tablas(conectadas, accesibles, no_conectadas)

    def rellenar_tablas(self, conectadas, accesibles, no_conectadas):
        # Limpiar el frame
        for widget in self.tablas_frame.winfo_children():
            widget.destroy()

        # --- Tabla de Zonas Conectadas ---
        titulo_con = ctk.CTkLabel(self.tablas_frame, text="Zonas Conectadas", font=ctk.CTkFont(size=20, weight="bold"), text_color="#e4e3e2")
        titulo_con.grid(row=0, column=0, columnspan=3, pady=(10, 5), sticky="w")

        columnas = 3
        fila = 1
        col = 0

        for idx, nodo in enumerate(conectadas):
            nombre = nodo["nombre"]
            minutos = nodo["minutos"]
            direc = nodo["direccion"]
            status = nodo["status"]

            icon = check if (status == 0) else warning
            
            frame_item = ctk.CTkFrame(self.tablas_frame, fg_color="transparent")
            frame_item.grid(row=fila, column=col, padx=10, pady=5, sticky="w")
            icono = ctk.CTkLabel(frame_item, image=icon, text="")
            icono.pack(side="left", padx=(0, 5))
            label_nombre = ctk.CTkLabel(frame_item, text=f"{direc} | {nombre}", font=ctk.CTkFont(size=14), text_color="#e4e3e2")
            label_nombre.pack(side="left")
            label_min = ctk.CTkLabel(frame_item, text=f"| {minutos} min", font=ctk.CTkFont(size=14), text_color="#bfbfbf")
            label_min.pack(side="left", padx=(5, 0))
            col += 1
            if col == columnas:
                col = 0
                fila += 1
        if col != 0:
            fila += 1  # Dejar espacio si la última fila no está completa

        # --- Tabla de Zonas Accesibles ---
        titulo_acc = ctk.CTkLabel(self.tablas_frame, text="Zonas Accesibles", font=ctk.CTkFont(size=20, weight="bold"), text_color="#e4e3e2")
        titulo_acc.grid(row=fila, column=0, columnspan=3, pady=(20, 5), sticky="w")
        fila += 1
        col = 0
        for idx, acc in enumerate(accesibles):
            direccion = acc["direccion"]
            nodo_destino = acc["nodo_destino"]
            minutos = acc["tiempo_total"]
            status_ruta = acc["status_ruta"]
            icon = check if (status_ruta == 0) else warning
            frame_item = ctk.CTkFrame(self.tablas_frame, fg_color="transparent")
            frame_item.grid(row=fila, column=col, padx=10, pady=5, sticky="w")
            icono = ctk.CTkLabel(frame_item, image=icon, text="")
            icono.pack(side="left", padx=(0, 5))
            label_nombre = ctk.CTkLabel(frame_item, text=f"{direccion} | {nodo_destino}", font=ctk.CTkFont(size=14), text_color="#e4e3e2")
            label_nombre.pack(side="left")
            label_min = ctk.CTkLabel(frame_item, text=f"| {minutos} min", font=ctk.CTkFont(size=14), text_color="#bfbfbf")
            label_min.pack(side="left", padx=(5, 0))
            col += 1
            if col == columnas:
                col = 0
                fila += 1
        if col != 0:
            fila += 1

        # --- Tabla de Zonas No Conectadas ---
        titulo_no_con = ctk.CTkLabel(self.tablas_frame, text="Zonas no conectadas", font=ctk.CTkFont(size=20, weight="bold"), text_color="#e4e3e2")
        titulo_no_con.grid(row=fila, column=0, columnspan=3, pady=(20, 5), sticky="w")
        fila += 1
        col = 0
        for idx, nombre in enumerate(no_conectadas):
            frame_item = ctk.CTkFrame(self.tablas_frame, fg_color="transparent")
            frame_item.grid(row=fila, column=col, padx=10, pady=5, sticky="w")
            icono = ctk.CTkLabel(frame_item, image=error, text="")
            icono.pack(side="left", padx=(0, 5))
            label_nombre = ctk.CTkLabel(frame_item, text=nombre, font=ctk.CTkFont(size=14), text_color="#e4e3e2")
            label_nombre.pack(side="left")
            col += 1
            if col == columnas:
                col = 0
                fila += 1


app = ctk.CTk()  # Crear la instancia de la aplicación
app.geometry("1080x720")  # Establecer el tamaño de la ventana
app.title("Sistema Delivery")
app.resizable(False, False)

login = LoginFrame(master=app)
label = ctk.CTkLabel(
    app,
    text="Sistema Delivery",
    font=ctk.CTkFont(size=30, weight="bold"),
    text_color="#e4e3e2"
)
label.place(relx=0.5, rely=0.01, anchor="n")
login.place(relx = 0.5, rely = 0.08, anchor = "n")

app.mainloop()