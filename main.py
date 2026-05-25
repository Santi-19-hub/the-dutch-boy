from fastapi import FastAPI
from pydantic import BaseModel
from app.models.schemas import ConversionRequest
from app.db.connection import init_db, insert_conversion
from app.db.connection import insert_conversion

app = FastAPI(title="GlobalSettler API - MVP")

@app.on_event("startup")
def startup_event():
    try:
        init_db()
        print("\n🚀 [SUCCESS] ¡Base de datos MySQL inicializada y sincronizada con éxito! 🎉\n")
    except Exception as e:
        print(f"\n❌ [ERROR] Error crítico al inicializar la base de datos: {e} 🚨\n")



@app.get("/")
def read_root():
    return {"status": "GlobalSettler API Running", "location": "Manizales ->Washington D.C. Connection"}

@app.post("/convert/cop-to-usd")
def convert_currency(data: ConversionRequest):
    if data.exchange_rate <=0:
        insert_conversion(data.amount_cop, data.exchange_rate, 0, data.target_currency)
        
        return {"error": "la tasa de cambio debe ser mayor que cero"}   
    result_usd = data.amount_cop / data.exchange_rate
    
    insert_conversion(data.amount_cop, data.exchange_rate, result_usd, data.target_currency )
    
    return {
        "currency": data.target_currency,
        "original_cop": data.amount_cop,
        "exchange_rate_used": data.exchange_rate,
        "total_usd": round(result_usd, 2),
        "message": "Ahorro proyectado para el viaje a EE.UU."
    }
    
@app.get("/history")
def get_conversion_history():
    history = get_all_history()
    return {"conversion_history": history}
