class Subject:
    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        self.observadores.remove(obj)

    def notificar(self, *args):
        for observador in self.observadores:
            observador.update(*args)


class Observador:
    def update(self, *args):
        raise NotImplementedError("Delegación de actualización")


class ConcreteObserverA(Observador):
    def __init__(self, obj):
        self.observado_a = obj
        self.observado_a.agregar(self)

    def update(self, *args):
        print("Actualización de estado para observador A")
        print("Aquí están los parámetros: ", args)