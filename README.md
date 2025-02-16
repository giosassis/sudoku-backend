# Sudoku - Backend

This is the backend of the Sudoku game, developed with **FastAPI**. The API is responsible for generating Sudoku boards, validating users' answers and providing the correct solution.

## How to run the project locally

### Requirements 
- Python (version 3.8 or higher)
- pip (Python package manager)

### Step to step to run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/giosassis/sudoku-backend

2. **Access the project folder:**:
    ```bash 
    cd sudoku-backend

3. **Create and activate the virtual environment:**:
    ```bash 
    python -m venv venv
    venv\Scripts\activate # Windows
    source venv/bin/activate # Linux or macOS

4. **Install dependencies:**:
    ```bash 
    pip install -r requirements.txt

5. **Start the development server:**:
    ```bash
    uvicorn main:app --reload

6. **Access the aplication**:
    ```bash
    http://localhost:8000

## Structure of the project

`main.py:` Contains the main logic of the API.

`solver.py:` Contains the algorithm for solving Sudoku.

`generator.py:` Contains the algorithm to generate Sudoku boards.

`src/assets/:` List of project dependencies.


## Deploy
The project is configured to deploy to **Render**. To deploy:

- Connect the repository to Render.
- Configure environment variables if necessary.
- Render will deploy automatically after each push.

## Technologies Used
- **FastAPI**: Framework for building APIs in Python.
- **Uvicorn**: ASGI server to run the API.
- **Render**: Deployment and hosting platform.

## License
This project is under the MIT License. See the LICENSE file for more details.

## How to contribute

Contributions are welcome! Follow the steps below:

- Fork the project.
- Create a branch for your feature (git checkout -b feature/new-feature).
- Commit your changes (git commit -m 'Add new feature').
- Push to the branch (git push origin feature/nova-feature).
- Open a pull request.

## Contact
If you have questions or suggestions, please contact:

Name: Giovana Assis

Email: giovana.sant@hotmail.com

GitHub: giosassis

