# AI Hospital Assistant Agent
 
An AI-powered hospital workflow assistant built for the OpenClaw Atlas assessment.
 
This project demonstrates:

- AI agent orchestration

- Tool usage

- Multi-step workflows

- AI reasoning

- Evaluation rubrics

- Frontend + Backend integration

- Free LLM integration using Groq
 
---
 
# Project Overview
 
The AI Hospital Assistant Agent simulates a hospital support workflow where an AI agent:

- fetches patient data

- processes medical information

- performs reasoning

- generates recommendations

- evaluates output quality
 
The system is designed to showcase practical AI agent architecture and evaluation pipelines.
 
---
 
# Features
 
## AI Agent Workflow

- Multi-step orchestration

- Planner-based execution
 
## Tool Usage

- Patient Tool

- Appointment Tool

- AI Reasoning Tool
 
## AI Reasoning

- Uses Groq LLM APIs

- Patient urgency analysis

- Recommendation generation
 
## Chat-Based Frontend

- Interactive AI chat interface

- Real-time API communication
 
## Evaluation Engine

- Rubric-based scoring

- Reasoning evaluation

- Safety evaluation
 
## Full Stack Architecture

- React frontend

- FastAPI backend
 
---
 
# Tech Stack
 
| Layer | Technology |

|---|---|

| Frontend | React + Vite |

| Backend | FastAPI |

| AI API | GroqCloud |

| Model | llama3-70b-8192 |

| Deployment | Render + Vercel |

| Database | SQLite (optional) |

| Version Control | GitHub |
 
---
 
# Project Structure
 
```text

ai-hospital-agent/

│

├── backend/

│   ├── agents/

│   ├── tools/

│   ├── evaluations/

│   ├── reports/

│   ├── models/

│   ├── main.py

│   ├── requirements.txt

│   └── .env

│

├── frontend/

│   ├── src/

│   ├── public/

│   └── package.json

│

├── docs/

│   ├── architecture.png

│   ├── screenshots/

│   └── rubric.md

│

├── README.md

└── .gitignore
 