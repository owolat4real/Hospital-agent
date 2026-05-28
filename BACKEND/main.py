from fastapi import FastAPI
from AGENTS.planner_agent import run_agent
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
def home():
    return {
        "message":"AI hospital agent is runing"
    }

@app.get("/analyze/{patient_id}")
def anaysis(patient_id:int):
    result = run_agent(patient_id)
    return result
