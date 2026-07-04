
# Suproc AI Agent

## Overview

The Suproc AI Procurement Agent is a local AI-powered procurement assistant that interprets business procurement requests, searches a structured knowledge base, ranks suitable suppliers, validates recommendations, detects potential prompt injection, and generates procurement insights while ensuring that all consequential actions require human approval.

The project is implemented using Python and Ollama (Qwen3:1.7B) and runs entirely on a local machine without external APIs.

---

# Features

- Natural language procurement request parsing using LLM
- AI-generated execution planning
- Multi-dataset knowledge base
- Supplier search and filtering
- Transparent ranking and match scoring
- Validation against hard constraints
- Correction workflow
- Prompt injection detection
- AI-generated procurement analysis
- Draft outreach message generation
- Human approval before business actions

---

# Project Architecture

```
                        User
                          │
                          ▼
                Requirement Parser (LLM)
                          │
                          ▼
                Structured Requirement
                          │
                          ▼
                  AI Execution Planner
                          │
                          ▼
                  Knowledge Base
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
   Suppliers    Professionals    Projects
        │             │             │
        └─────────────┼─────────────┘
                      ▼
           Procurement History
                      │
                      ▼
           Business Opportunities
                      │
                      ▼
               Ranking Engine
                      │
                      ▼
             Validation Engine
                      │
                      ▼
             Correction Workflow
                      │
                      ▼
               AI Business Advisor
                      │
                      ▼
              Human Approval Gate
```

---

# Project Structure

```
suproc_agent/

agent/
tools/
models/
data/
tests/

main.py
README.md
requirements.txt
pytest.ini
```

---

# Technology Stack

- Python 3.10+
- Ollama
- Qwen3:1.7B
- Pandas
- Pydantic
- Pytest

---

# Installation

Clone the repository

```bash
git clone <repository-url>
cd suproc_agent
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install Ollama

https://ollama.com

Download model

```bash
ollama pull qwen3:1.7b
```

Run

```bash
python main.py
```

---

# Model Requirements

Model Used

Qwen3:1.7B (Ollama)

Minimum RAM

8 GB

Recommended

16 GB RAM

Python

3.10+

Operating System

Windows / Linux / macOS

---

# Sample Dataset

The project uses synthetic procurement datasets.

Included datasets:

- suppliers.csv (30+ records)
- professionals.csv
- projects.csv
- opportunities.csv
- procurement_requests.csv

Each dataset contains structured business information including:

- Company
- Category
- Capacity
- Delivery
- Certification
- Availability
- Rating
- Location
- Previous procurement requests
- Business opportunities

No real Suproc production data is used.

---

# Tool Definitions

### Requirement Parser

Converts natural language procurement requests into structured business requirements.

### Supplier Tool

Searches suppliers matching requested categories.

### Professional Tool

Returns relevant professionals.

### Project Tool

Finds related business projects.

### Procurement Tool

Searches previous procurement history.

### Opportunity Tool

Retrieves business opportunities.

### Ranking Tool

Ranks suppliers using transparent scoring.

### Validation Tool

Checks recommendations against business constraints.

### Correction Tool

Reports validation issues and prepares corrected recommendations.

### AI Advisor

Generates

- Execution plan
- Risks
- Missing information
- Outreach message

---

# Ranking Formula

| Factor | Weight |
|---------|---------|
| Product Relevance | 30% |
| Location Suitability | 20% |
| Hard Constraints | 25% |
| Capacity & Availability | 15% |
| Reputation | 10% |

Maximum Score = 100

---

# Validation Logic

The validator checks:

- Supplier exists
- Correct entity type
- Capacity requirements
- Delivery constraints
- Food-grade certification
- Availability
- Duplicate recommendations
- Requested number of results
- Prompt injection detection
- Match score validity
- Human approval requirement

---

# Correction Workflow

When validation issues are detected:

1. Recommendations are reviewed.
2. Validation failures are reported.
3. Correction report is generated.
4. Best available recommendations are returned.
5. Human approval is required before any action.

---

# Human Approval

The AI agent never automatically:

- Sends emails
- Approves suppliers
- Awards contracts
- Creates purchase orders
- Updates business databases
- Executes irreversible actions

The final output always ends with:

```
Status

Awaiting Human Approval
```

---

# Evaluation Tests

Implemented test cases include:

- Normal procurement request
- No matching suppliers
- Conflicting requirements
- Missing request information
- Missing dataset information
- Ambiguous location
- Duplicate records
- Invalid entity type
- Prompt injection
- Ignore validation request

Current Results

| Metric | Value |
|---------|--------|
| Total Tests | 10 |
| Passed | 8 |
| Failed | 2 |

---

# Example Output

The final agent output includes:

- Business Requirement
- Execution Plan
- Recommended Suppliers
- Match Score Breakdown
- Supporting Evidence
- Validation Report
- Missing Information
- Risks
- Recommended Next Action
- Draft Outreach Message
- Human Approval Status

---

# Known Limitations

- Uses synthetic datasets
- Limited supplier records
- Local CSV storage instead of SQL
- Local LLM may occasionally require prompt tuning
- Recommendation quality depends on dataset completeness
- Correction workflow can be further enhanced with iterative re-search

---

# Future Improvements

- SQLite/PostgreSQL integration
- FastAPI REST API
- Streamlit dashboard
- Multi-agent orchestration
- Web search integration
- Real supplier database
- Automatic report generation

---

# Repository

Repository URL:

https://github.com/hefaaa/suproc-ai-procurement-agent

---

# Submission Information

Repository URL

https://github.com/hefaaa/suproc-ai-procurement-agent

Demo Video URL

(Add your video link)

Model Used

Qwen3:1.7B via Ollama

Known Limitations

Refer to the Known Limitations section above.

---

