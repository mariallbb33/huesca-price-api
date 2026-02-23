from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timezone

app = FastAPI()


class ExtractRequest(BaseModel):
    url: str


class CompareRequest(BaseModel):
    query: str
    city: str
    max_results: int = 20


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/extract")
def extract(req: ExtractRequest):
    return {
        "store": "demo",
        "name": "Producto de prueba",
        "price": 1.23,
        "currency": "EUR",
        "unit_size": "1 ud",
        "price_per_unit": 1.23,
        "unit": "€/ud",
        "availability": "in_stock",
        "url": req.url,
        "captured_at": datetime.now(timezone.utc).isoformat(),
    }


@app.post("/compare")
def compare(req: CompareRequest):
    return {
        "query": req.query,
        "currency": "EUR",
        "results": [
            {
                "store": "demo-mercadona",
                "name": f"{req.query} (ejemplo 1)",
                "price": 2.10,
                "unit_size": "1 kg",
                "price_per_unit": 2.10,
                "unit": "€/kg",
                "availability": "in_stock",
                "url": "https://example.com/producto1",
                "captured_at": datetime.now(timezone.utc).isoformat(),
            },
            {
                "store": "demo-carrefour",
                "name": f"{req.query} (ejemplo 2)",
                "price": 2.40,
                "unit_size": "1 kg",
                "price_per_unit": 2.40,
                "unit": "€/kg",
                "availability": "in_stock",
                "url": "https://example.com/producto2",
                "captured_at": datetime.now(timezone.utc).isoformat(),
            },
        ],
    }
