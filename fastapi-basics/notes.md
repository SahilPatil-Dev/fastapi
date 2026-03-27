# FastAPI Basics + Query Handling

## What I built:
- API to read patient data from JSON
- Get all patients
- Get patient by ID
- Sort patients by height, weight, BMI

## Concepts Learned:

### 1. FastAPI App
- Creating app using FastAPI()

### 2. GET Routes
- @app.get("/") → return all data

### 3. Path Parameters
- /patient/{patient_id}
- Used Path() for validation

### 4. Query Parameters
- /sort?sort_by=bmi&order=desc
- Used Query()

### 5. Error Handling
- HTTPException (404, 400)

### 6. Data Handling
- Reading JSON file using json.load()

### 7. Sorting Logic
- sorted() with lambda
- reverse=True for descending

## Mistakes:
- Example parameter is deprecated (warning in terminal)

## Key Takeaway:
FastAPI makes building APIs simple and powerful with validation built-in.