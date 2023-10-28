#import datetime

import pandas as pd
from .cPaciente import cPaciente


class cManejoArchivo:
    def __init__(self, archivo_csv=None):
        self._archivo_csv = None
        if (archivo_csv):
            self._archivo_csv = archivo_csv
            try:
                # Intenta cargar el archivo CSV si existe, o crea uno nuevo si no.
                self._base_de_pacientes = pd.read_csv(archivo_csv)
            except FileNotFoundError:
                self._base_de_pacientes = pd.DataFrame(
                    columns=["Nombre", "Edad", "Gravedad", "Historial", "Enfermero", "Fecha","Caso Clinico"])
        else:

            self._base_de_pacientes = pd.DataFrame(
                columns=["Nombre", "Edad", "Gravedad", "Historial", "Enfermero", "Fecha","Caso Clinico"])

    def agregar_paciente(self, cPaciente):

        nuevo_paciente = pd.DataFrame(
            {"Nombre": [cPaciente.getNombre()], "Edad": [cPaciente.getEdad()], "Gravedad": [cPaciente.getGravedad()],
             "Historial": [cPaciente.getHistorial()], "Enfermero": [cPaciente.getEnfermero().getNombre()],
             "Matricula": [cPaciente.getEnfermero().getMatricula()],
             "Caso Clinico": [cPaciente.getCasoClinico()],
             "Fecha": [cPaciente.getTiempoLLegada()]})
        self._base_de_pacientes = pd.concat([self._base_de_pacientes, nuevo_paciente], ignore_index=True)
        self._base_de_pacientes.to_csv(self._archivo_csv, index=False)

    def buscar_paciente(self, nombre,fecha):
        # Filtra el DataFrame en función del nombre y la fecha
        pacientes_filtrados = self._base_de_pacientes[
            (self._base_de_pacientes["Nombre"] == nombre) & (self._base_de_pacientes["Fecha"] == fecha)
            ]

        # Si no se encontraron pacientes, devuelve None
        if pacientes_filtrados.empty:
            return None

        # Extrae los datos del primer paciente encontrado
        paciente_data = pacientes_filtrados.iloc[0]

        _color = 0
        if(paciente_data["Gravedad"]==0):
            _color = "rojo"
        elif(paciente_data["Gravedad"]==1):
            _color = "naranja"
        elif (paciente_data["Gravedad"] == 2):
            _color = "amarillo"
        elif (paciente_data["Gravedad"] == 3):
            _color = "verde"
        elif (paciente_data["Gravedad"] == 4):
            _color = "azul"

        # Crea un objeto cPaciente con los datos extraídos
        paciente = cPaciente(
            paciente_data["Nombre"],
            _color,
            paciente_data["Edad"],
            paciente_data["Caso Clinico"],  # Puedes modificar esto si tienes un campo correspondiente
            paciente_data["Enfermero"],  # Puedes modificar esto si tienes un campo correspondiente
            paciente_data["Historial"]
        )

        return paciente

    def editar_paciente(self, nombre,fecha, nueva_edad, nueva_gravedad, nuevo_historial, nuevo_enfermero):
        paciente = self.buscar_paciente(nombre,fecha)
        if paciente is not None:
            paciente["Edad"] = nueva_edad
            paciente["Gravedad"] = nueva_gravedad
            paciente["Historial"] = nuevo_historial
            paciente["Enfermero"] = nuevo_enfermero
            self._base_de_pacientes.to_csv(self._archivo_csv, index=False)
            return True
        else:
            return False

    def leer_otro_archivo(self, archivo_csv_otro):
        try:
            pacientes_otro = pd.read_csv(archivo_csv_otro)
            self._base_de_pacientes = pd.concat([self._base_de_pacientes, pacientes_otro], ignore_index=True)
            self._base_de_pacientes.to_csv(self._archivo_csv, index=False)
            return True
        except FileNotFoundError:
            return False
