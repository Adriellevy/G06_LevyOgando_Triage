from .cEnfermero import *
from Classes.cQuesMaestra import *
from Classes.cManejoArchivo import cManejoArchivo
from Classes import cPaciente_sinGravedad
from Classes import cPaciente
from .Errores.cErrorSalaEspera import cErrorSalaEspera
import datetime as dt
class cSalaEspera:
    def __init__(self):
        self.algo = 1
        self.Lista_enfermeros_triage=[]
        self.HandlerArchivos=cManejoArchivo()
        self.Lista_pacientes = cQuesMaestra()
        self.Sala_Espera = []
        self.Num_ulitmo_caso_clinico=self.HandlerArchivos.BusquedaUltimo()
        self.Iniciosesion()

    def Pacientes_sin_Clasificar(self,paciente):
        self.Sala_Espera.append(paciente)

    def Iniciosesion(self):
        """Aca va a estar el metodo con el cual el enfermero va a poder iniciar sesion y se lo agregara a la lista de pacientes"""
        Enfermero_ingresado=cEnfermero("Alejandra","000000")
        self.Lista_enfermeros_triage.append(Enfermero_ingresado)
    def NoMasDe3Mins(self,paciente):
        fecha=dt.timedelta(0,0,0,0,paciente.getTiempoLLegada().minute,paciente.getTiempoLLegada().hour,0)
        hora=dt.datetime.now()
        ahora= dt.timedelta(0,0,0,0,hora.minute,hora.hour,0)
        diferencia = (fecha - ahora).total_seconds() / 60
        if (paciente.getClasificado == 'false' and diferencia > 3):
            raise cErrorSalaEspera("El paciente lleva mas de 3 minutos en la sala de espera")

    def Pacientes_Clasificados(self,color,nombre,edad,historial):
        self.Num_ulitmo_caso_clinico= self.Num_ulitmo_caso_clinico+1
        _casoClinico = self.Num_ulitmo_caso_clinico
        enfermero = self.Lista_enfermeros_triage[0]
        pac=self.generarPaciente(color,nombre,edad,_casoClinico,enfermero,historial)
        self.Lista_pacientes.insert(pac)

    def AtenderProximo(self):
        paciente = self.Lista_pacientes.ObtenerProximo()
        paciente.atender()

    def generar_Paciente_sin_gravedad(self,edad,textoHistorial):
        self.Num_ulitmo_caso_clinico= self.Num_ulitmo_caso_clinico+1
        _casoClinico = self.Num_ulitmo_caso_clinico
        enfermero = self.Lista_enfermeros_triage[0]
        return cPaciente_sinGravedad(edad,_casoClinico,enfermero,textoHistorial)

    def Atender(self,paciente,medico):
       #if medico.getDisponibilidad()=='true':

        #else :
            #raise cErrorSalaEspera("Error No hay medicos disponibles")

      return 0

    def generarPaciente(self, color, nombre, edad, _casoClinico, enfermero, historial):
        return cPaciente(nombre,color,edad,_casoClinico,enfermero,historial)



