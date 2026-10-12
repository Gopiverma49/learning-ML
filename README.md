# Learning ML

A repository for machine learning practice and data preprocessing scripts.

## Project Structure

- `data_fliter.py`: Python script demonstrating data cleaning and handling missing values with pandas.
- `requirements.txt`: Python package dependencies.
- `.gitignore`: Configured to ignore virtual environments, cache files, and editor settings.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd "learning ML"
   ```

2. **Create a virtual environment:**
   ```powershell
   python -m venv .venv
   ```

3. **Activate the virtual environment:**
   - **Windows (PowerShell):**
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - **Windows (CMD):**
     ```cmd
     .venv\Scripts\activate.bat
     ```
   - **macOS / Linux:**
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the script:**
   ```bash
   python data_fliter.py
   ```
