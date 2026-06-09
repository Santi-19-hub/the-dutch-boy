from fastapi import APIRouter, HTTPException, status
from typing import List
from pydantic import BaseModel
from app.schemas.schemas import ConversionRequest
from app.db.connection import insert_conversion

router = APIRouter(prefix="/reportes", tags=["Reportes"])

class ReporteResponse(BaseModel):
    id: int
    amount_cop: float
    exchange_rate: float
    total_usd: float
    target_currency: str
    user_id: int

    class Config:
        from_attributes = True

@router.get("", response_model=List[ReporteResponse], summary="Get Reportes")
def get_reportes():
    return []

@router.post("", status_code=status.HTTP_201_CREATED, summary="Create Reporte")
def create_reporte(data: ConversionRequest):
    if data.exchange_rate <= 0:
        raise HTTPException(status_code=400, detail="La tasa de cambio debe ser mayor a cero")
    insert_conversion(data.amount_cop, data.exchange_rate, 0, data.target_currency)
    return {"message": "Reporte de conversión creado y almacenado exitosamente"}

@router.get("/{id}", summary="Get Reporte")
def get_reporte(id: int):
    return {"message": f"Detalle del reporte {id}"}

@router.put("/{id}", summary="Update Reporte")
def update_reporte(id: int):
    return {"message": f"Reporte {id} actualizado"}

@router.delete("/{id}", summary="Delete Reporte")
def delete_reporte(id: int):
    return {"message": f"Reporte {id} eliminado"}

@router.get("/summary", summary="Obtener resumen estadístico global")
def get_global_summary():
    try:
        
        total_transacciones = 150  
        total_ahorros = 350.50     
        
        return {
            "status": "success",
            "total_transacciones": total_transacciones,
            "total_ahorros": total_ahorros,
            "reportes_generados": 12
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al calcular el resumen: {str(e)}"
        )