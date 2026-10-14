## Topic 3: Project Setup and Environment Configuration

### 3.1 Prerequisites
Before setting up the project locally, ensure you have the following installed:

- **Python:** Version 3.10 or higher.
- **Git:** Installed and configured with your user credentials.
- **IDE / Editor:** Visual Studio Code, Cursor, or your preferred IDE.

### 3.2 Step-by-Step Initial Setup

1. **Clone the Repository:**
   ```bash
   git clone <REPOSITORY_URL>
   cd my-project
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   # Windows PowerShell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

   # Linux / macOS / Git Bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Copy `.env.example` to `.env` and fill in the values according to your development environment.
