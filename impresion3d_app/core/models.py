from dataclasses import dataclass

@dataclass
class Filamento:
    material: str
    tipo: str
    color_nombre: str
    color_hex: str
    marca: str
    gramos: float
    costo_total: float
    costo_por_gramo: float

@dataclass
class ColorBase:
    nombre: str
    hex: str
