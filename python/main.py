from fastapi import FastAPI, Response
import random

app = FastAPI()

@app.get("/metrics")

def metrics():
    body = f"""
# HELP temperatura Temperatura ambiente
# TYPE temperatura gauge
temperatura{{sensor="sala"}} {random.uniform(20, 30)}
temperatura{{sensor="cozinha"}} {random.uniform(20, 30)}
"""
    return Response(content=body, media_type="text/plain")

