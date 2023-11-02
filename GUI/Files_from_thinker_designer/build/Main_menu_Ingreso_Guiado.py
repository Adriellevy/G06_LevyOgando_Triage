import sys
import tkinter as tk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

sys.path.insert(1,r"C:\Users\Adri\Desktop\Laboratorio de programacion 2\Triage\Classes")
from Classes.cSalaEspera import *

#--------------------------Variables Globales---------------------------------

#-- Path's--
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"C:\Users\Adri\Desktop\Laboratorio de programacion 2\Triage\GUI\Files_from_thinker_designer\build\assets\frame0")

global Father_off_windows

#-- Ventana de Ejecucion --
window = tk.Tk()
window.geometry("1440x900")
window.configure(bg="#F0F0F0")

#-- Imagenes de Bottones --
button_image_1 = None
button_image_2 = None
button_image_3 = None
button_image_4 = None

#----- Ventanas -----
Ventana_aux = None

#--- cSalaEspera ---
Sala_de_espera = cSalaEspera()

#------------------------------Metodosaccesorios----------------------------
def relative_to_assets_menu_ingreso_guiado(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def relative_to_assets_rojo(path: str) -> Path:
    ASSETS_PATH = OUTPUT_PATH / Path(
        r"C:\Users\Adri\Desktop\Laboratorio de programacion 2\Triage\GUI\Files_from_thinker_designer\build\assets\frame4")
    return ASSETS_PATH / Path(path)

def relative_to_assets_amarillo(path: str) -> Path:
    ASSETS_PATH = OUTPUT_PATH / Path(
        r"C:\Users\Adri\Desktop\Laboratorio de programacion 2\Triage\GUI\Files_from_thinker_designer\build\assets\frame6")
    return ASSETS_PATH / Path(path)

def relative_to_assets_naranja(path: str) -> Path:
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Adri\Desktop\Laboratorio de programacion 2\Triage\GUI\Files_from_thinker_designer\build\assets\frame5")
    return ASSETS_PATH / Path(path)


def relative_to_assets_Verde(path: str) -> Path:
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Adri\Desktop\Laboratorio de programacion 2\Triage\GUI\Files_from_thinker_designer\build\assets\frame7")
    return ASSETS_PATH / Path(path)

def relative_to_assets_Ingreso_ya_clasificado(path: str) -> Path:
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Adri\Desktop\Laboratorio de programacion 2\Triage\GUI\Files_from_thinker_designer\build\assets\frame1")
    return ASSETS_PATH / Path(path)


#------------------------------ Ventanas ----------------------------

def Ingresar_paciente_con_guia():
    """
    En esta funcion se ejecuta el GUI general
    para poder categorzar a un paciente que llego a
    la sala de espera
    :return:
    """

    button_image_ventana_rojo_1 = PhotoImage(file=relative_to_assets_rojo("button_1.png"))
    button_image_ventana_rojo_2 = PhotoImage(file=relative_to_assets_rojo("button_2.png"))

    canvas = Canvas(window, bg="#F0F0F0",
                    height=900,
                    width=1440,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge"
                    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        64.0,
        815.0,
        167.0,
        835.0,
        fill="#000000",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("image_1.png"))
    image_1 = canvas.create_image(
        125.0,
        450.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("image_2.png"))
    image_2 = canvas.create_image(
        148.0,
        162.0,
        image=image_image_2
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=56.0,
        y=272.0,
        width=135.0,
        height=20.0
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("image_3.png"))
    image_3 = canvas.create_image(
        73.0,
        341.0,
        image=image_image_3
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=64.0,
        y=328.0,
        width=158.0,
        height=31.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=64.0,
        y=212.0,
        width=142.0,
        height=20.0
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("image_4.png"))
    image_4 = canvas.create_image(
        115.0,
        825.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("image_5.png"))
    image_5 = canvas.create_image(
        466.0,
        76.0,
        image=image_image_5
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        940.0,
        73.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#DBDBDB",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=715.0,
        y=48.0,
        width=450.0,
        height=48.0
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("image_6.png"))
    image_6 = canvas.create_image(
        736.2000122070312,
        72.199951171875,
        image=image_image_6
    )

    canvas.create_text(
        773.0,
        65.0,
        anchor="nw",
        text="Search Something",
        fill="#9A9A9A",
        font=("Montserrat Medium", 14 * -1)
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("image_7.png"))
    image_7 = canvas.create_image(
        1253.0,
        73.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("image_8.png"))
    image_8 = canvas.create_image(
        456.0,
        172.0,
        image=image_image_8
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Rojo(window,button_image_ventana_rojo_1,button_image_ventana_rojo_2),
        relief="flat"
    )
    button_4.place(
        x=320.0,
        y=151.0,
        width=275.3648681640625,
        height=43.0
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("image_9.png"))
    image_9 = canvas.create_image(
        117.0,
        69.0,
        image=image_image_9
    )

    image_image_10 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("image_10.png"))
    image_10 = canvas.create_image(
        72.81015014648438,
        397.76214599609375,
        image=image_image_10
    )

    canvas.create_text(
        108.00003051757812,
        393.0,
        anchor="nw",
        text="Settings",
        fill="#FFFFFF",
        font=("Montserrat Medium", 16 * -1)
    )

    window.resizable(True, True)
    window.mainloop()

def Rojo(_window,button_image_1,button_image_2):
    global Father_off_windows
    """
    Para empezar a categorizar empiezo realizando preguntas,
    Empiezo por las pregutnas que tendría un paciente que requiere de una atencion urgente
    :param _window:
    :return:
    """
    print("button_4 clicked")
        # Creo una nueva ventana

    ventana_roja = tk.Toplevel(_window)
    Father_off_windows = _window
    ventana_roja.title("Es rojo?")
    ventana_roja.geometry("680x282")
    ventana_roja.configure(bg="#FFFFFF")

    canvas = Canvas(
        ventana_roja,
        bg="#FFFFFF",
        height=282,
        width=680,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets_rojo("image_1.png"))
    image_1 = canvas.create_image(
        485.0,
        141.0,
        image=image_image_1
    )
    button_1 = Button(
        master=ventana_roja,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=447.576904296875,
        y=120.0,
        width=76.784423828125,
        height=43.0
    )


    image_image_2 = PhotoImage(
        file=relative_to_assets_rojo("image_2.png"))
    image_2 = canvas.create_image(
        245.0,
        141.0,
        image=image_image_2
    )

    button_2 = Button(
        master=ventana_roja,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Naranja(ventana_roja, button_image_1, button_image_2),
        relief="flat"
    )
    button_2.place(
        x=207.576904296875,
        y=120.0,
        width=75.784423828125,
        height=43.0
    )
    canvas.create_text(
        186.0,
        16.0,
        anchor="nw",
        text="¿Tiene Politraumatismo?",
        fill="#000000",
        font=("Montserrat SemiBold", 24 * -1)
    )

def Naranja(_window, button_image_1, button_image_2):
    print("button_4 clicked")
    global Father_off_windows
    _window.destroy() #destruyo la ventana anterior
    Father_off_windows.wm_state('zoomed')
    Ventana_naranja = tk.Toplevel(Father_off_windows)  # Crea una nueva ventana con el padre de menu
    Ventana_naranja.title("Es Naranja?")
    Ventana_naranja.geometry("680x282")
    Ventana_naranja.configure(bg="#FFFFFF")

    canvas = Canvas(
        Ventana_naranja,
        bg="#FFFFFF",
        height=282,
        width=680,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets_naranja("image_1.png"))
    image_1 = canvas.create_image(
        474.0,
        92.0,
        image=image_image_1
    )

    button_1 = Button(
        master=Ventana_naranja,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=436.0,
        y=69.0,
        width=76.784423828125,
        height=43.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets_naranja("image_2.png"))
    image_2 = canvas.create_image(
        474.0,
        204.0,
        image=image_image_2
    )

    button_2 = Button(

        master=Ventana_naranja,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Amarillo(Ventana_naranja,button_image_1,button_image_2),
        relief="flat"
    )
    button_2.place(
        x=436.576904296875,
        y=183.0,
        width=76.107177734375,
        height=43.0
    )

    canvas.create_text(
        64.0,
        7.0,
        anchor="nw",
        text="Actualmente tiene algun sintoma de :  \nComa \n\nConvulsion \n\nHemorragia Digestiva\n Isquemia",
        fill="#000000",
        font=("MontserratRoman Medium", 24 * -1)
    )

def Amarillo(_window, button_image_1, button_image_2):
    print("Botton No Naranja Apretado")
    global Father_off_windows
    _window.destroy() #destruyo la ventana anterior
    Father_off_windows.wm_state('zoomed')
    Ventana_amarillo = tk.Toplevel(Father_off_windows)  # Crea una nueva ventana con el padre de menu
    Ventana_amarillo.title("Es Amarillo? ")
    Ventana_amarillo.geometry("680x282")
    Ventana_amarillo.configure(bg="#FFFFFF")

    canvas = Canvas(
        Ventana_amarillo,
        bg="#FFFFFF",
        height=282,
        width=680,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets_amarillo("image_1.png"))
    image_1 = canvas.create_image(
        599.0,
        69.0,
        image=image_image_1
    )

    button_1 = Button(
        master=Ventana_amarillo,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=561.0,
        y=46.0,
        width=76.784423828125,
        height=43.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets_amarillo("image_2.png"))
    image_2 = canvas.create_image(
        595.0,
        204.0,
        image=image_image_2
    )

    button_2 = Button(
        master=Ventana_amarillo,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda:Verde(Ventana_amarillo,button_image_1,button_image_2),
        relief="flat"
    )
    button_2.place(
        x=557.576904296875,
        y=183.0,
        width=76.107177734375,
        height=43.0
    )

    canvas.create_text(
        64.0,
        7.0,
        anchor="nw",
        text="Cefalea brusca,  paresia, \nhipertensión arterial,  \nvértigo con afectación vegetativa \nsíncope \nurgencias psiquiátricas",
        fill="#000000",
        font=("MontserratRoman Medium", 24 * -1)
    )

def Verde(_window, button_image_1, button_image_2):
    print("Botton No Naranja Apretado")
    global Father_off_windows
    _window.destroy() #destruyo la ventana anterior
    Father_off_windows.wm_state('zoomed')
    Ventana_verde = tk.Toplevel(Father_off_windows)  # Crea una nueva ventana con el padre de menu
    Ventana_verde.title("Es verde? ")
    Ventana_verde.geometry("680x282")
    Ventana_verde.configure(bg="#FFFFFF")

    canvas = Canvas(
        Ventana_verde,
        bg="#FFFFFF",
        height=282,
        width=680,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets_Verde("image_1.png"))
    image_1 = canvas.create_image(
        474.0,
        92.0,
        image=image_image_1
    )

    button_1 = Button(
        master=Ventana_verde,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=436.0,
        y=69.0,
        width=76.784423828125,
        height=43.0
    )


    image_image_2 = PhotoImage(
        file=relative_to_assets_Verde("image_2.png"))
    image_2 = canvas.create_image(
        474.0,
        204.0,
        image=image_image_2
    )


    button_2 = Button(
        master=Ventana_verde,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Abrir_menu_ingreso_datos_cargados(_window,"azul"),
        relief="flat"
    )


    button_2.place(
        x=436.576904296875,
        y=183.0,
        width=76.107177734375,
        height=43.0
    )

    canvas.create_text(
        60.0,
        65.0,
        anchor="nw",
        text="categoría normal.\n Otalgias,\n odontalgias, \ndolores inespecíficos leves, \ntraumatismos \n esguinces",
        fill="#000000",
        font=("MontserratRoman Medium", 24 * -1)
    )

def Abrir_menu_ingreso_datos_cargados(_window,color):
    print("Botton No Naranja Apretado")
    global Father_off_windows
    _window.destroy()  # destruyo la ventana anterior
    Father_off_windows.destroy()
    Ingreso_ya_clasificado(color)

def Ingreso_ya_clasificado(color):
    window = tk.Tk()
    window.geometry("1440x1024")
    window.configure(bg="#F0F0F0")

    canvas = Canvas(
        window,
        bg="#F0F0F0",
        height=1024,
        width=1440,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_1.png"))
    image_1 = canvas.create_image(
        125.0,
        450.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=64.00000000000045,
        y=152.0,
        width=168.0,
        height=31.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=64.00000000000045,
        y=272.0,
        width=106.0,
        height=20.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_2.png"))
    image_2 = canvas.create_image(
        73.00000000000045,
        341.0,
        image=image_image_2
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=56.000000000000455,
        y=328.0,
        width=166.0,
        height=31.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=64.00000000000045,
        y=212.0,
        width=142.0,
        height=20.0
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_3.png"))
    image_3 = canvas.create_image(
        115.00000000000045,
        825.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_4.png"))
    image_4 = canvas.create_image(
        464.00000000000045,
        76.0,
        image=image_image_4
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        940.0000000000005,
        73.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#DBDBDB",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=715.0000000000005,
        y=48.0,
        width=450.0,
        height=48.0
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_5.png"))
    image_5 = canvas.create_image(
        736.2000122070317,
        72.19999694824219,
        image=image_image_5
    )

    canvas.create_text(
        773.0000000000005,
        65.0,
        anchor="nw",
        text="Search Something",
        fill="#9A9A9A",
        font=("Montserrat Medium", 14 * -1)
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_6.png"))
    image_6 = canvas.create_image(
        1253.0000000000005,
        73.0,
        image=image_image_6
    )

    canvas.create_text(
        290.00000000000045,
        352.0,
        anchor="nw",
        text="Distribucion pacientes por gravedad",
        fill="#000000",
        font=("Montserrat SemiBold", 24 * -1)
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_7.png"))
    image_7 = canvas.create_image(
        518.0000000000005,
        228.0,
        image=image_image_7
    )

    canvas.create_rectangle(
        290.00000000000045,
        735.0,
        746.0000000000005,
        927.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        315.00000000000045,
        786.0,
        716.0000000000005,
        787.0,
        fill="#E2E2E2",
        outline="")

    image_image_8 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_8.png"))
    image_8 = canvas.create_image(
        926.0000000000005,
        198.0,
        image=image_image_8
    )

    canvas.create_text(
        797.0000000000005,
        135.2288818359375,
        anchor="nw",
        text="Ingreso Personalizado",
        fill="#000000",
        font=("Montserrat Medium", 16 * -1)
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_9.png"))
    image_9 = canvas.create_image(
        1263.0000000000005,
        359.0,
        image=image_image_9
    )

    canvas.create_text(
        1131.0000000000005,
        152.0,
        anchor="nw",
        text="Ingreso  Masivo",
        fill="#000000",
        font=("Montserrat Medium", 16 * -1)
    )

    image_image_10 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_10.png"))
    image_10 = canvas.create_image(
        1263.0000000000005,
        750.0,
        image=image_image_10
    )

    image_image_11 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_11.png"))
    image_11 = canvas.create_image(
        926.0000000000005,
        662.0,
        image=image_image_11
    )

    image_image_12 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_12.png"))
    image_12 = canvas.create_image(
        921.0000000000005,
        395.0,
        image=image_image_12
    )

    canvas.create_rectangle(
        780.0000000000005,
        355.0,
        1071.0000000000005,
        356.0,
        fill="#DDDDDD",
        outline="")

    canvas.create_text(
        855.0000000000005,
        321.0,
        anchor="nw",
        text="Recien Derivados",
        fill="#000000",
        font=("Montserrat Medium", 16 * -1)
    )

    canvas.create_rectangle(
        1121.0000000000005,
        674.0,
        1412.0000000000005,
        675.0,
        fill="#DDDDDD",
        outline="")

    canvas.create_text(
        1126.0000000000005,
        639.0,
        anchor="nw",
        text="Pacientes Ingresados en el Día",
        fill="#2A2A2A",
        font=("Montserrat Medium", 16 * -1)
    )

    image_image_13 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_13.png"))
    image_13 = canvas.create_image(
        1142.0000000000005,
        767.0,
        image=image_image_13
    )

    image_image_14 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_14.png"))
    image_14 = canvas.create_image(
        1285.0000000000005,
        767.0,
        image=image_image_14
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Agregar_paciente_clasificado(entry_2.get(),entry_3.get()) ,
        relief="flat"
    )
    button_5.place(
        x=974.0000000000005,
        y=195.0,
        width=74.0,
        height=24.0
    )

    image_image_15 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_15.png"))
    image_15 = canvas.create_image(
        117.00000000000045,
        69.0,
        image=image_image_15
    )

    image_image_16 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_16.png"))
    image_16 = canvas.create_image(
        72.81015777587936,
        397.76214599609375,
        image=image_image_16
    )

    canvas.create_text(
        108.00001525878952,
        393.0,
        anchor="nw",
        text="Settings",
        fill="#FFFFFF",
        font=("Montserrat Medium", 16 * -1)
    )

    image_image_17 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_17.png"))
    image_17 = canvas.create_image(
        519.0000000000005,
        548.0,
        image=image_image_17
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        865.0000000000005,
        194.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#F3F3F3",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=804.5000000000005,
        y=184.0,
        width=121.0,
        height=19.0
    )

    canvas.create_text(
        801.0000000000005,
        163.0,
        anchor="nw",
        text="Nombre",
        fill="#000000",
        font=("Montserrat Medium", 16 * -1)
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        865.0000000000005,
        247.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#F3F3F3",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=806.0000000000005,
        y=235.0,
        width=118.0,
        height=22.0
    )
    entry_3.insert(0, color)

    canvas.create_text(
        798.0000000000005,
        219.0,
        anchor="nw",
        text="Gravedad",
        fill="#000000",
        font=("Montserrat Medium", 16 * -1)
    )

    window.resizable(True, True)
    window.mainloop()

def Agregar_paciente_clasificado(nombre,color):
    Sala_de_espera.Pacientes_Clasificados(color,nombre,"18","Unkown")

def Agregar_paciente_sin_clasificar():
    """
    Este metodo simula la llegada de un paciente random a la sala de espera
    este no fue categorizado
    :return:
    """
    paciente = Sala_de_espera.generar_Paciente_sin_gravedad("20","",)
    Sala_de_espera.Pacientes_sin_Clasificar(paciente)

if __name__ == '__main__':
    # Handler()
    Ingresar_paciente_con_guia()
