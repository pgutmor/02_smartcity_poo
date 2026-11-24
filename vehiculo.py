
class Vehiculo:
    """Molde que representa un vehículo eléctrico."""

    def __init__(self, matricula: str, modelo: str, capacidad_kwh: float):
        self.matricula: str = matricula
        self.modelo: str = modelo
        self.capacidad_kwh: float = capacidad_kwh
        self._nivel_bateria: float = 100.0
        self._kilometros_totales: float = 0.0

    @property
    def nivel_bateria(self) -> float:
        """Getter: Devuelve el porcentaje de batería actual."""
        return self._nivel_bateria

    @nivel_bateria.setter
    def nivel_bateria(self, nuevo_nivel: float) -> None:
        """Setter: Valida que la batería esté entre 0 y 100."""
        if nuevo_nivel < 0.0 or nuevo_nivel > 100.0:
            raise ValueError(
                f"Nivel de batería inválido: {nuevo_nivel}%. "
                "Debe estar entre 0 y 100."
            )
        self._nivel_bateria = nuevo_nivel

    @property
    def kilometros_totales(self) -> float:
        """Getter: Devuelve los kilómetros acumulados."""
        return self._kilometros_totales

    @kilometros_totales.setter
    def kilometros_totales(self, nuevos_km: float) -> None:
        """Setter: Impide reducir los kilómetros del vehículo."""
        if nuevos_km < self._kilometros_totales:
            raise ValueError(
                "Los kilómetros no pueden disminuir (fraude de odómetro)."
            )
        self._kilometros_totales = nuevos_km

    def conducir(self, distancia_km: float) -> bool:
        """Simula un trayecto urbano."""

        energia_necesaria = distancia_km * 0.15
        porcentaje_consumido = (
            energia_necesaria / self.capacidad_kwh
        ) * 100.0

        if self.nivel_bateria >= porcentaje_consumido:
            self.nivel_bateria -= porcentaje_consumido
            self.kilometros_totales += distancia_km
            return True
        else:
            return False

    def obtener_estado(self) -> str:
        """Devuelve el estado actual del vehículo."""

        return (
            f"[{self.matricula}] {self.modelo} | "
            f"Batería: {self.nivel_bateria:.1f}% | "
            f"Total: {self.kilometros_totales} km"
        )

    def recargar(self, energia_kwh: float) -> float:
        """Recarga la batería sin superar el 100%."""

        porcentaje_recarga = (
            energia_kwh / self.capacidad_kwh
        ) * 100.0

        nuevo_nivel = self.nivel_bateria + porcentaje_recarga

        if nuevo_nivel > 100.0:
            nuevo_nivel = 100.0

        self.nivel_bateria = nuevo_nivel

        return self.nivel_bateria