# FastAPI & Postman Exercises

## Description

A collection of exercises to practice building RESTful web services using **FastAPI** and testing API endpoints with **Postman**.

---

## Prerequisites

- **Python** 3.7 or higher
- **FastAPI** library
- **Uvicorn** (ASGI server for running FastAPI)
- **Postman** (for testing API endpoints)

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/andriniainanekena/fastapi-exercises.git
   cd fastapi-exercises
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # Linux/MacOS
   source venv/bin/activate
   # Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install fastapi uvicorn
   ```

4. **Run the server**:
   ```bash
   uvicorn main:app --reload
   ```

   The server will be accessible at:  
   `http://localhost:8000`

---

## Testing with Postman

1. **Import the Postman collection**:
   - Find the collection file.
   - Import it into Postman.

2. **Test the endpoints**:
   - Use the imported collection to execute the **GET**, **POST**, ... requests.
