from .cEnfermero import cEnfermero
from Classes import cQuesMaestra

from Classes import cPaciente
from .Errores.cErrorSalaEspera import cErrorSalaEspera
import datetime as dt
class cSalaEsera:
    def __init__(self):
        self.algo = 1
        self.Lista_pacientes = cQuesMaestra()
        self.Sala_Espera = []

    def Pacientes_sin_Clasificar(self,paciente):
        self.Sala_Espera.append(paciente)


    def NoMasDe3Mins(self,paciente):
        fecha=dt.timedelta(0,0,0,0,paciente.getTiempoLLegada().minute,paciente.getTiempoLLegada().hour,0)
        hora=dt.datetime.now()
        ahora= dt.timedelta(0,0,0,0,hora.minute,hora.hour,0)
        diferencia = (fecha - ahora).total_seconds() / 60
        if (paciente.getClasificado == 'false' and diferencia > 3):
            raise cErrorSalaEspera("El paciente lleva mas de 3 minutos en la sala de espera")

    def Pacientes_Clasificados(self):
        paciente = self.Sala_Espera.pop(0)
        paciente.setClasificado()
        if paciente.getGravedad == 0:
            self.Lista_pacientes.R.put_nowait(paciente)
        elif paciente.getGravedad == 1:
            self.Lista_pacientes.N.put_nowait(paciente)
        elif paciente.getGravedad == 2:
            self.Lista_pacientes.AM.put_nowait(paciente)
        elif paciente.getGravedad == 3:
            self.Lista_pacientes.V.put_nowait(paciente)
        elif paciente.getGravedad == 4:
            self.Lista_pacientes.AZ.put_nowait(paciente)
        else:
            raise cErrorSalaEspera("Error Ingresar Paciente")

    def Reorganizar_greedy(self):
        p = self.Lista_pacientes.ObtenerProximo_sinR()
        fecha = dt.timedelta(0, 0, 0, 0, p.getTiempoLLegada().minute, p.getTiempoLLegada().hour, 0)
        hora = dt.datetime.now()
        ahora = dt.timedelta(0, 0, 0, 0, hora.minute, hora.hour, 0)
        diferencia = (fecha - ahora).total_seconds() / 60
        if (diferencia > p.getGravedad__.getTiempoGravedadActual):
            p.getGravedad__.setGravedadMayor(p.getGravedad - 1)  # el paciente tiene un nuevo color
            self.Cambiar_Paciante(p)

    def Cambiar_Paciante(self, paciente):
        if paciente.getGravedad == 1:
            self.Lista_pacientes.N.put_nowait(paciente)
        elif paciente.getGravedad == 2:
            self.Lista_pacientes.AM.put_nowait(paciente)
        elif paciente.getGravedad == 3:
            self.Lista_pacientes.V.put_nowait(paciente)
        elif paciente.getGravedad == 4:
            self.Lista_pacientes.AZ.put_nowait(paciente)
        else:
            raise cErrorSalaEspera("Error Ingresar Paciente")

    def Ingresar_Pacientes_Greedy(self):
        paciente = self.Sala_Espera.pop(0)
        if paciente.getGravedad == 0:
            self.Lista_pacientes.R.put_nowait(paciente)
        elif paciente.getGravedad == 1:
            self.Lista_pacientes.N.put_nowait(paciente)
        elif paciente.getGravedad == 2:
            self.Lista_pacientes.AM.put_nowait(paciente)
        elif paciente.getGravedad == 3:
            self.Lista_pacientes.V.put_nowait(paciente)
        elif paciente.getGravedad == 4:
            self.Lista_pacientes.AZ.put_nowait(paciente)
        else:
            raise cErrorSalaEspera("Error Ingresar Paciente")



    def Atender(self,paciente,medico):
       #if medico.getDisponibilidad()=='true':

        #else :
            #raise cErrorSalaEspera("Error No hay medicos disponibles")

      return 0


