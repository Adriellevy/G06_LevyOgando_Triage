from Classes.cGravedad import cGravedad
import datetime as dt
class cPaciente:

    def __int__(self,_nombre,color):
        self.gravedad = cGravedad(color)
        self.nombre=_nombre
        self.tiempoLlegada = dt.datetime.now()


    def Atender(self):
        """
        Esta funcion guarda al paciente en el archivo csv como si fuera una "base" de datos
        :return:
        null
        """
        return 0

    def getGravedad(self):
        """
        este metodo devuelve el color de la gravedad actual
        :return:
        """
        return self.gravedad

    def getTiempoRestante(self):
        """
        Este metodo devuelve el tiempo que le queda en esa gravedad asignada
        :return:
        """

        return (self.getGravedad().getTiempoGravedadActual() - (dt.datetime.now() - self.tiempoLlegada))
    def getTiempoRestanteMayorGravedad(self):

        """

        :return:

        """
        return (self.getGravedad().getTiempoGravedadMayor() - (dt.datetime.now() - self.tiempoLlegada))

    def getPrioridadNueva(self):
        self.gravedad.AsignarNuevaGravedad()
        return self.getGravedad()