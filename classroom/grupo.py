from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            if self._asignaturas == None:
                self._asignaturas = [Asignatura(x)]
            else:
                self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista == None and self.listadoAlumnos == None:
            self.listadoAlumnos = [alumno]
        elif lista != None and self.listadoAlumnos == None:
            lista.append(alumno)
            self.listadoAlumnos = lista
        elif lista == None and self.listadoAlumnos != None:
            self.listadoAlumnos.append(alumno)
        elif lista != None and self.listadoAlumnos != None:
            lista.append(alumno)
            self.listadoAlumnos += lista

    def __str__(self):
        return "Grupo de estudiantes: " + self._grupo

    """@ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre"""

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    """@ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre"""


