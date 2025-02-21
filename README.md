# KPI Advisor

## 📌 Project Overview
This project is a **FastAPI-based backend** that connects to a client's **MySQL database**, extracts its structure (tables & columns), and suggests **prebuilt KPIs** based on available data. The system also highlights missing columns required to track meaningful KPIs.

### ✅ Features:
- **Connects to MySQL databases** securely.
- **Extracts database schema** (tables & columns).
- **Maps existing structure to prebuilt KPIs**.
- **Identifies missing columns** required for meaningful KPI tracking.
- **Provides an API to return schema & KPI readiness**.

---

## 🛠 Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/kpi-schema-extractor.git
cd kpi-schema-extractor
```

### **2️⃣ Create and Activate a Virtual Environment**
```bash
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # Activate on Mac/Linux
venv\Scripts\activate  # Activate on Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Configure Environment Variables**
Create a **`.env`** file in the project root and add your **MySQL database credentials**:
```ini
DATABASE_URL=mysql+pymysql://your_user:your_password@your_host:3306/your_database
```

> **Note:** If your password contains special characters (`@`, `!`, etc.), URL-encode them using `urllib.parse.quote()`.

### **5️⃣ Run the FastAPI Server**
```bash
uvicorn main:app --reload
```

Your API will be available at:
- **Swagger Docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc UI:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔥 API Endpoints

| Endpoint          | Method | Description |
|------------------|--------|-------------|
| `/`              | `GET`  | Root endpoint to check API status. |
| `/schema`        | `GET`  | Fetches the MySQL database schema (tables & columns). |
| `/check-kpis`    | `GET`  | Returns missing columns for KPI calculations. |

---

## 📂 Project Structure
```
kpi-schema-extractor/
│── .env                # Environment variables (not committed to Git)
│── .gitignore          # Ignore venv, pycache, logs, etc.
│── requirements.txt    # List of dependencies
│── main.py             # FastAPI app entry point
│── database.py         # Database connection logic
│── schema_extractor.py # Schema extraction & KPI mapping
│── README.md           # Project documentation
```

---

## 🔄 Updating Dependencies
If new packages are installed, update **`requirements.txt`**:
```bash
pip freeze > requirements.txt
```
Then push the update to Git.

---

## 🤝 Contributing
Feel free to submit issues or open a pull request. Feedback is always welcome!

---

## 📜 License
This project is licensed under the **MIT License**.

