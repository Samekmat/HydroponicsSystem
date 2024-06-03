# Hydroponic System Development in Django

## Instructions to Run Locally:

* ### Using Poetry:
<details>
<summary>Expand instructions</summary>

1. Clone the repository:
   ```bash
   git clone https://github.com/Samekmat/HydroponicsSystem.git
    ```

2. Navigate to the project directory:

3. Create a .env file based on .env.dist in the core directory and fill in the necessary environment variables.

4. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

5. Apply migrations:
   ```bash
      poetry run python manage.py migrate
   ```

6. Run the development server:
   ```bash
      poetry run python manage.py runserver
   ```
</details>

* ### Using Requirements.txt:
<details>
<summary>Expand instructions</summary>

1. Clone the repository:
   ```bash
      git clone https://github.com/Samekmat/HydroponicsSystem.git
   ```

2. Navigate to the project directory:

3. Create a .env file based on .env.dist in the core directory and fill in the necessary environment variables.

4. Install dependencies using pip:
   ```bash
      pip install -r requirements.txt
   ```

5. Apply migrations:
   ```bash
      python manage.py migrate
   ```

6. Run the development server:
   ```bash
      python manage.py runserver
   ```
</details>

* ### Running with Docker/Docker Compose:
<details>
<summary>Expand instructions</summary>

1. Make sure Docker and Docker Compose are installed on your system.

2. Clone the repository:
   ```bash
      git clone https://github.com/Samekmat/HydroponicsSystem.git
   ```

3. Navigate to the project directory:

4. Create a .env file based on .env.dist in the core directory and fill in the necessary environment variables.

5. Build and run the Docker images:
   ```bash
      docker compose -f .docker/docker-compose.yml up -d --build
   ```

6. Access the application at http://localhost:8000.

</details>

## Additional Information:
<details>
<summary>Expand info</summary>

1. Typing and type annotations have been utilized for improved code clarity and maintainability. Django and Django REST Framework stubs have been included for better type checking with MyPy.
MyPy can be used to check the code for type errors.</br>
`Run MyPy with the following command:`
   ```bash
      poetry run mypy .
   ```

2. Pre-commit hooks have been set up using black, ruff, bandit, and a bunch of hooks for code formatting and security checks.

3. Continuous Integration (CI) for the project is managed through GitHub Actions workflow. It includes steps for running tests, code quality checks, and ensuring compliance with coding standards.

4. Django-filters are added, allowing for pagination, filtering, and sorting of responses by adding parameters in the request:
   - **Pagination:** `url/?page=page_num`
   - **Filter:** `url/?field=field_value`
   - **Sort:** `url/?ordering=field/-field`

   ### Available Filters

   #### Systems App Filter Fields
   - `name`
   - `created_at`
   - `updated_at`

   #### Measurements App Filter Fields
   - `system`
   - `measured_at`
   - `pH_data`
   - `water_temperature`
   - `TDS`

   ### Example `curl` Request
   ```bash
   curl -X GET "http://localhost/api/v1/systems/?page=1&name=example_system_name&ordering=-created_at"
   ```

</details>
