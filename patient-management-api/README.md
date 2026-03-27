# 🏥 Patient Management System API

A simple and efficient **Patient Management System API** built using **FastAPI**.
This project allows you to manage patient records with automatic BMI calculation and health classification.

---

## 🚀 Features

* ✅ Create, Read, Update, Delete (CRUD) patient records
* ✅ Automatic **BMI calculation**
* ✅ Health classification:

  * Underweight
  * Normal
  * Overweight
  * Obese
* ✅ Input validation using **Pydantic**
* ✅ Lightweight **JSON-based storage**
* ✅ Clean and structured API design

---

## 🛠️ Tech Stack

* **FastAPI** 🚀
* **Python 3.10+**
* **Pydantic**
* **JSON (File Storage)**

---

## 📂 Project Structure

```
.
├── main.py          # FastAPI application
├── patients.json    # Data storage
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/patient-management-api.git
cd patient-management-api
```

### 2. Create virtual environment

```
python -m venv venv
```

### 3. Activate virtual environment

* Windows:

```
venv\Scripts\activate
```

* Mac/Linux:

```
source venv/bin/activate
```

### 4. Install dependencies

```
pip install fastapi uvicorn
```

### 5. Run the server

```
uvicorn main:app --reload
```

---

## 🌐 API Endpoints

| Method | Endpoint         | Description        |
| ------ | ---------------- | ------------------ |
| GET    | `/`              | Welcome message    |
| GET    | `/patients`      | Get all patients   |
| GET    | `/patients/{id}` | Get single patient |
| POST   | `/patients`      | Create new patient |
| PUT    | `/edit/{id}`     | Update patient     |
| DELETE | `/delete/{id}`   | Delete patient     |

---

## 📊 Example Patient Data

```json
{
  "id": "P001",
  "name": "Sahil Patil",
  "city": "Mumbai",
  "age": 20,
  "gender": "Male",
  "height": 1.72,
  "weight": 70
}
```

---

## 📌 BMI Formula

BMI is calculated automatically using:

```
BMI = weight / (height * height)
```

---

## 🧪 API Testing

Once the server is running, open:

👉 http://127.0.0.1:8000/docs

FastAPI provides an interactive Swagger UI to test all endpoints.

---

## 🎯 Future Improvements

* 🔐 Add Authentication (JWT)
* 🗄️ Replace JSON with Database (SQLite/PostgreSQL)
* ☁️ Deploy API (Render / Railway)
* 📊 Add analytics & filtering

---

## 👨‍💻 Author

* Sahil Patil
* GitHub: https://github.com/SahilPatil-Dev

---

## ⭐ Show your support

If you like this project, give it a ⭐ on GitHub!
