# Farmers Market API

A FastAPI-base POC backend for managing users, vendors, and organizations in a farmers market context.

---

## Features

- User authentication and management
- Vendor and organization CRUD operations
- PostgreSQL database integration

---

## Requirements

- Python 3.10+
- PostgreSQL

---

## Setup

### 1. Clone the repository

```sh
git clone <your-repo-url>
cd mt-poc
```

### 2. Create and activate a virtual environment

```sh
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the project root with the following variables:

```env
DATABASE_URL=postgresql://<user>:<password>@localhost/<database>
SECRET_KEY=your-secret-key


DB_HOST=<>
DB_PORT=<>
DB_USER=<>
DB_PASSWORD=<>
DB_NAME=<>
SECRET_KEY="<>"
API_PREFIX="/api"
```

- `DATABASE_URL`: PostgreSQL connection string (e.g., `postgresql://postgres:password@localhost/farmersmarket`)
- `SECRET_KEY`: Secret key for JWT or session management

### 5. Prepare the database

- Ensure PostgreSQL is running and the database exists.
- Run the database initialization script:


### 6. Running Tests
```

- pytest

```

---

## Running the API

Start the FastAPI server with:

```sh
uvicorn main:app --reload
```

The API will be available at [http://localhost:8000](http://localhost:8000).

---

## Directory Structure

```
mt-poc/
├── api/
├── core/
├── db/
├── models/
├── router/
├── schemas/
├── services/
├── tests/
├── main.py
├── requirements.txt
└── README.md
```

## Notes

- Ensure all required tables will be created by running the DB init script.
- Adjust import paths if you move files or rename directories.
- To run the server just python main.py

---

## License

MIT