from pydantic import BaseModel

class ConversionRequest(BaseModel):
    amount_cop: float
    exchange_rate: float 
    target_currency: str = "USD"
    
    