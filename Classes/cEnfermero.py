from .cPaciente import cPaciente
class cEnfermero:
    """
    Esta clase tiene como objetivo dar a conocer el/la enfermer@ de triage que se encargo de
    clasificar al pacientes que fue registrado y luego de esto se encuentra en la sala de espera para ser
    atendidos
    """
    def __init__(self):
        self.nombre = "def"
        self.Matricula="123012"

    def Clasificar(self,_nombre,_color,_casoClinico):
        """
        toda esta informacion viene de la interfaz del usario, y el usuario que agendo
        :param:
        :return:
        cPacienteClasificado
        """
        NuevoPaciente=cPaciente(_nombre,_color,_casoClinico,self)
        return NuevoPaciente