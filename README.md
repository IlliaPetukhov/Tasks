# Django ToDo List Application

## Description

This is a ToDo List application built with Django. It allows users to create, edit, delete, and mark tasks as completed or not completed. Tasks can also be organized using tags.

## Models

### Task
The Task model represents a to-do item. Each task has the following fields:
- `content`: Describes what needs to be done.
- `created_at`: Datetime when the task was created.
- `deadline`: (Optional) Datetime by which the task should be completed.
- `is_done`: Boolean field indicating if the task is done or not.
- `tags`: Tags relevant to this task.

### Tag
The Tag model represents a theme or category for tasks. Each tag has:
- `name`: The name of the tag.

A task can have multiple tags and a tag can be associated with multiple tasks.

## Home Page

The home page can be accessed at `127.0.0.1:8000/`. It includes:

- A sidebar with links to:
  - Home page
  - Tag list page
- The sidebar should be present on all pages.
- A to-do list that displays a list of tasks.
  - Tasks should be ordered from not done to done and from newest to oldest.
  - All task information should be displayed.
  - A button to add a new task.
  - Links for updating and deleting each task.
  - A "Complete" button if the task is not done, and an "Undo" button if the task is done. This button changes the status of the task to the opposite and redirects back to the home page.

## Tag List Page

The tag list page can be accessed at `127.0.0.1:8000/tags/`. It includes:

- A table with tag names, links for updating, and deleting tags.
- A button to add a new tag.

Pages for adding tasks and tags must also be implemented.

## How to Run the Project

1. **Clone the repository:**

    ```bash
    git clone https://github.com/IlliaPetukhov/Tasks.git
    cd Tasks
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run database migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

6. **Open the application in your browser:**

    Visit `http://127.0.0.1:8000/` to see the home page.
