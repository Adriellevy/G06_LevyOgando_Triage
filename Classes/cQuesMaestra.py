import queue
#from cEnfermero import cEnfermero
from .cPaciente import cPaciente
from .Errores.cErrorTamanio import cErrorTamanio
from .Errores.cErrorGravedad import cErrorGravedad

class cQuesMaestra:
    def __init__(self):
        self.R = queue.Queue(maxsize=0)
        self.N = queue.Queue(maxsize=0)
        self.AM = queue.Queue(maxsize=0)
        self.V = queue.Queue(maxsize=0)
        self.AZ = queue.Queue(maxsize=0)
        self.Lista_de_colas = []
        #enermero_def = cEnfermero()
        #L_enfermeros = []
        self.Lista_de_colas.append(self.R)
        self.Lista_de_colas.append(self.N)
        self.Lista_de_colas.append(self.AM)
        self.Lista_de_colas.append(self.V)
        self.Lista_de_colas.append(self.AZ)

    def Reorganizar(self, indice_lista=4):
        obj_act = cPaciente()
        if indice_lista == 0:
            return 1
        try:
            obj_act = self.Lista_de_colas[indice_lista].queue[0]
            if obj_act.getTiempoRestante() > obj_act.getTiempoRestanteMayorGravedad():
                return self.Reorganizar(indice_lista - 1)
            else:
                num = obj_act.getPrioridadNueva()
                obj_act = self.Lista_de_colas[indice_lista].get_nowait()
                self.Lista_de_colas[num].put_nowait(obj_act)
                return self.Reorganizar(indice_lista)
        except:
            raise cErrorTamanio("Reorganizar")

    def insert(self, _paciente):
        try:
            num = -1
            try:
                num = _paciente.getGravedad()
            except cErrorGravedad("En el insert") as err:
                num = _paciente.getPrioridadNueva()
            self.Lista_de_colas[num].put_nowait(_paciente)
        except cErrorTamanio("Error en el insert") as errorTam:
            print(cErrorTamanio)