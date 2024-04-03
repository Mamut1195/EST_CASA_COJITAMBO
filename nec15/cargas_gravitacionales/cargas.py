"""
Módulo para almacenar cargas según la norma NEC-15.
"""

class CargasNEC15:
    """
    Clase para almacenar cargas según la norma NEC-15.
    
    Attributes:
        cargas (dict): Un diccionario que almacena diferentes tipos de cargas.
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

        Args:
            carga_muerta (int): El valor de la carga permanente.
        """
        self.create_dict_of_cargas()
        self.cargas['carga_permanente'] = carga_muerta

    def add_to_dict_sobrecarga(self, carga_viva: int) -> None:
        """
        Agrega la sobrecarga al diccionario de cargas.

        Args:
            carga_viva (int): El valor de la sobrecarga.
        """
        self.create_dict_of_cargas()
        self.cargas['sobrecarga'] = carga_viva

    def add_to_dict_sobrecarga_cubierta(self, carga_viva_cubierta: int) -> None:
        """
        Agrega la sobrecarga de cubierta al diccionario de cargas.

        Args:
            carga_viva_cubierta (int): El valor de la sobrecarga de cubierta.
        """
        self.create_dict_of_cargas()
        self.cargas['sobrecarga_cubierta'] = carga_viva_cubierta

    def add_to_dict_carga_de_granizo(self, carga_de_granizo: int) -> None:
        """
        Agrega la carga de granizo al diccionario de cargas.

        Args:
            carga_de_granizo (int): El valor de la carga de granizo.
        """
        self.create_dict_of_cargas()
        self.cargas['carga_de_granizo'] = carga_de_granizo

    def add_to_dict_carga_de_barlovento(self, barlovento: int) -> None:
        """
        Agrega la carga de barlovento al diccionario de cargas.

        Args:
            barlovento (int): El valor de la carga de barlovento.
        """
        self.create_dict_of_cargas()
        self.cargas['carga_de_barlovento'] = barlovento

    def add_to_dict_carga_de_sotavento(self, sotavento: int) -> None:
        """
        Agrega la carga de sotavento al diccionario de cargas.

        Args:
            sotavento (int): El valor de la carga de sotavento.
        """
        self.create_dict_of_cargas()
        self.cargas['carga_de_sotavento'] = sotavento
