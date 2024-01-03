 
# Task Manager

## Overview

Task Manager with REST API

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/bhyeanhasan/task_manager
    ```

2. Change into the project directory:

    ```bash
    cd task_manager
    ```

3. Create and activate a virtual environment (optional but recommended):

    ```bash
    virtualenv venv
    source venv/bin/activate  
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration


Import three csv file =
```
task.csv
task-image.csv
user.csv
```

Apply database migrations:

    ```bash
    python manage.py migrate
    ```

## Running the Project

Start the development server:

```bash
python manage.py runserver
```

## API Documentation


### 1. Get All Tasks

**Endpoint:** `/ManageTask`

**Method:** `GET`

**Description:** Retrieve a list of all tasks.

**Usage:**

```bash
curl -X GET http://localhost:8000/ManageTask
```

### 2. Create Tasks

**Endpoint:** `/ManageTask`

**Method:** `POST`

**Description:** Create tasks.

**Usage:**

```bash
curl -X POST http://localhost:8000/ManageTask
```

### 3. Update Tasks

**Endpoint:** `/ManageTask`

**Method:** `PATCH`

**Description:** Update tasks.

**Usage:**

```bash
curl -X PATCH http://localhost:8000/ManageTask
```

### 4. Delete Task

**Endpoint:** `/ManageTask/<id>`

**Method:** `DELETE`

**Description:** Delete task.

**Usage:**

```bash
curl -X DELETE http://localhost:8000/ManageTask/1
```