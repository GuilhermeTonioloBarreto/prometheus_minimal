from fastapi import FastAPI, Response
import random

app = FastAPI()

@app.get("/metrics")

def metrics():
    body = f"""
# HELP temperatura Temperatura simulada
# TYPE temperatura gauge
temperatura {random.uniform(20, 30)}

# HELP tensao Tensao simulada
# TYPE tensao gauge
tensao {random.uniform(210, 230)}
"""
    return Response(content=body, media_type="text/plain")

