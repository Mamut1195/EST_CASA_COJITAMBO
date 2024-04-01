"""
Módulo para almacenar cargas según la norma NEC-15.
"""

class CargasNEC15:
    """
    Clase para almacenar cargas según la norma NEC-15.
    """
    def __init__(self) -> None:
        """
        Inicializa el diccionario de cargas.
        """
        self.cargas = {}

    def create_dict_of_cargas(self) -> None:
        """
        Crea un diccionario vacío para las cargas.
        """
        self.cargas = {}

    def add_to_dict_carga_permanente(self, carga_muerta: int) -> None:
        """
        Agrega la carga permanente al diccionario de cargas.
        """
        self.create_dict_of_cargas()
        self.cargas['carga_permanente'] = carga_muerta

    def add_to_dict_sobrecarga(self, carga_viva: int) -> None:
        """
        Agrega la sobrecarga al diccionario de cargas.
        """
        self.create_dict_of_cargas()
        self.cargas['sobrecarga'] = carga_viva

    def add_to_dict_sobrecarga_cubierta(self, carga_viva_cubierta: int) -> None:
        """
        Agrega la sobrecarga de cubierta al diccionario de cargas.
        """
        self.create_dict_of_cargas()
        self.cargas['sobrecarga_cubierta'] = carga_viva_cubierta

    def add_to_dict_carga_de_granizo(self, carga_de_granizo: int) -> None:
        """
        Agrega la carga de granizo al diccionario de cargas.
        """
        self.create_dict_of_cargas()
        self.cargas['carga_de_granizo'] = carga_de_granizo

    def add_to_dict_carga_de_viento(self, carga_de_viento: int) -> None:
        """
        Agrega la carga de viento al diccionario de cargas.
        """
        self.create_dict_of_cargas()
        self.cargas['carga_de_viento'] = carga_de_viento
