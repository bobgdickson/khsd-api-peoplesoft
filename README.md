# KHSD PeopleSoft Info API

FastAPI service to expose Purchase Order information (PO header and line distribution) from the KHSD PeopleSoft Finance system over internal JSON APIs. 
Designed to replace legacy SOAP/WSDL interfaces with clean, lightweight JSON.

---

## 🚀 Features
- Fetch PO details by `PO_ID` and `BUSINESS_UNIT`
- Returns:
  - PO Date
  - Vendor ID
  - Line Items (Quantity, Amount, Fund Code)
- Built with:
  - FastAPI
  - SQLAlchemy
  - MS SQL Server backend (via pyodbc)

---

## 📦 Requirements

- Python 3.11+
- ODBC Driver 17+ for SQL Server
- `.env` file or environment variables for database credentials

---

## 🛠️ Setup (Local Development)

```bash
git clone https://github.com/your-org/khsd-api-peoplesoft.git
cd khsd-api-peoplesoft
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

**Environment Variables (local `.env` file):**
```dotenv
DATABASE_URL=mssql+pyodbc://username:password@your-sql-server/your-db?driver=ODBC+Driver+17+for+SQL+Server
```

**Run Locally:**
```bash
uvicorn main:app --reload
```

Then open Swagger Docs at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Dockerized Setup

**Build and Run:**
```bash
docker-compose up --build
```

---

## 🔥 API Usage

**Endpoint:**  
`GET /po-info`

**Query Parameters:**
| Parameter | Description |
|:---------|:------------|
| `po_id` | (required) Purchase Order ID |
| `business_unit` | (optional, default: `KERNH`) |

**Example:**
```bash
curl 'http://localhost:8000/po-info?po_id=0000212096&business_unit=KERNH'
```

**Sample Response:**
```json
{
  "po_id": "0000212096",
  "business_unit": "KERNH",
  "po_date": "2023-12-01",
  "vendor_id": "0000001478",
  "line_items": [
    {
      "line_number": 1,
      "quantity": 2,
      "amount": 21.58,
      "fund_code": "06"
    }
  ]
}
```

---

## 🧩 Project Structure

```
khsd-api-peoplesoft/
├── main.py          # FastAPI app
├── models.py        # Pydantic response models
├── database.py      # DB connection setup
├── orm.py           # SQLAlchemy ORM models
├── queries.py       # DB query logic
└── Dockerfile       # (optional) Docker support
└── docker-compose.yml
```

---

## ✨ Future Enhancements

- Add authentication (API Key or OAuth)
- Join Vendor Name info
- Add optional filter by Fund Code or Department
- Add caching for popular POs
- Centralized logging

---

### 🚀 TL;DR
Proved a "6-month project" could be done by one guy and an AI in **literally 30 minutes**.

---
