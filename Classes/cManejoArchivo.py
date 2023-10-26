import datetime

import pandas as pd
from .cPaciente import cPaciente
class LecturaDeArchivos:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
        try:
            # Intenta cargar el archivo CSV si existe, o crea uno nuevo si no.
            self.base_de_pacientes = pd.read_csv(archivo_csv)
        except FileNotFoundError:
            self.base_de_pacientes = pd.DataFrame(columns=["Nombre", "Edad", "Gravedad", "Historial", "Enfermero","Fecha"])

    def agregar_paciente(self, cPaciente):

        nuevo_paciente = pd.DataFrame({"Nombre": [cPaciente.getNombre()], "Edad": [cPaciente.getNombre()], "Gravedad": [cPaciente.getGravedad()],
                                      "Historial": [cPaciente.getHistorial()], "Enfermero": [cPaciente.getEnfermero().nombre ],"Matricula": [cPaciente.getEnfermero().Matricula],
                                       "Fecha": [cPaciente.getTiempoLLegada()]})
        self.base_de_pacientes = pd.concat([self.base_de_pacientes, nuevo_paciente], ignore_index=True)
        self.base_de_pacientes.to_csv(self.archivo_csv, index=False)

    def buscar_paciente(self, nombre):
        paciente = self.base_de_pacientes[self.base_de_pacientes["Nombre"] == nombre]
        return paciente if not paciente.empty else None

    def editar_paciente(self, nombre, nueva_edad, nueva_gravedad, nuevo_historial, nuevo_enfermero):
        paciente = self.buscar_paciente(nombre)
        if paciente is not None:
            paciente["Edad"] = nueva_edad
            paciente["Gravedad"] = nueva_gravedad
            paciente["Historial"] = nuevo_historial
            paciente["Enfermero"] = nuevo_enfermero
            self.base_de_pacientes.to_csv(self.archivo_csv, index=False)
            return True
        else:
            return False

    def leer_otro_archivo(self, archivo_csv_otro):
        try:
            pacientes_otro = pd.read_csv(archivo_csv_otro)
            self.base_de_pacientes = pd.concat([self.base_de_pacientes, pacientes_otro], ignore_index=True)
            self.base_de_pacientes.to_csv(self.archivo_csv, index=False)
            return True
        except FileNotFoundError:
            return False

