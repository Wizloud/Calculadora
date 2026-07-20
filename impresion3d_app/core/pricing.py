# core/pricing.py
from typing import List
from .models import ProductoItem

def factor_multitanda(tandas: int) -> float:
    if tandas <= 1:
        return 1.0
    return 0.6 * tandas

def calcular_costos_variables(
    productos: List[ProductoItem],
    tarifa_material_extra: float,
    tarifa_electricidad_h: float,
    tarifa_depreciacion_h: float,
) -> float:
    total_gramos = sum(p.gramos for p in productos)
    total_horas = sum(p.tiempo_impresion_h for p in productos)

    costo_material_extra = total_gramos * tarifa_material_extra
    costo_electricidad = total_horas * tarifa_electricidad_h
    costo_depreciacion = total_horas * tarifa_depreciacion_h

    return costo_material_extra + costo_electricidad + costo_depreciacion

def calcular_postproceso(productos: List[ProductoItem], tarifa_postproceso_h: float) -> float:
    total = 0.0
    for p in productos:
        total += p.tiempo_postproceso_h * tarifa_postproceso_h * p.tandas
    return total

def calcular_costos_fijos(base_costos_fijos: float, tandas_totales: int) -> float:
    return base_costos_fijos * factor_multitanda(tandas_totales)

def calcular_riesgo(productos: List[ProductoItem], tarifa_riesgo_h: float) -> float:
    if not productos:
        return 0.0
    horas_totales = sum(p.tiempo_impresion_h for p in productos)
    tandas_totales = sum(p.tandas for p in productos)
    horas_promedio_por_tanda = horas_totales / max(tandas_totales, 1)
    return horas_promedio_por_tanda * tarifa_riesgo_h

def aplicar_margen(costo_total: float, margen_pct: float) -> float:
    return costo_total * (1 + margen_pct / 100.0)

def aplicar_iva(monto: float, iva_pct: float, aplicar: bool) -> float:
    if not aplicar:
        return monto
    return monto * (1 + iva_pct / 100.0)
