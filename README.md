JustifAi – AI-Based Lawyer

An AI-powered legal assistant combining a React (Vite + TypeScript + Tailwind) frontend with a Flask-based backend for PDF case summarization and predictive analysis (custody and compensation). The backend can also serve a prebuilt frontend for simple single-container deployments.

## Features
- PDF upload and automatic case summarization (NLTK + TF‑IDF)
- Predictive analysis for custody and compensation (scikit‑learn)
- Authentication and theming scaffolded on the frontend (Firebase ready)
- Docker support for one-command deployment (Gunicorn + Flask)

## Tech Stack
- Backend: Flask, scikit‑learn, pandas, NLTK, Gunicorn
- Frontend: React, Vite, TypeScript, TailwindCSS, Firebase (optional)
- Packaging: Docker (Python 3.10 slim)

## Repository Structure
```
JustifAi-AI-Based-Lawyer-main/
  backened/                 # Flask app (note the folder name)
    check.py                # Main app entry
    requirements.txt        # Python dependencies
    static/                 # Prebuilt frontend (served by Flask)
    models/                 # Trained model artifacts (.pkl)
    uploads/                # Temp uploads
    data/                   # Training/feature data (xlsx)
  frontened/                # React + Vite + TypeScript app (note the folder name)
    src/                    # Components, context, Firebase config
    package.json            # Frontend dependencies & scripts
  data/                     # Dataset copy
  Dockerfile                # One-container deploy
```

## Prerequisites
- Python 3.10+ (for backend)
- Node.js 18+ and npm (for frontend dev/build)
- Git (to version and push)
- Docker (optional, for containerized run)

## Backend – Local Setup (Flask)
On Windows PowerShell:
```powershell
cd backened
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
# (Optional) Ensure NLTK data is available
python -m nltk.downloader punkt

# Run the server (development)
python check.py
```
Default dev URL: `http://localhost:5000`

Environment variables:
- `PORT` (optional): Flask will use this if set; default is 5000 in `check.py`. Docker uses 10000 (see Docker section).

### Backend API Endpoints
- `POST /upload` – multipart form-data with `file` (PDF). Returns JSON `{ summary, filename }`.
- `POST /predict` – JSON body:
  ```json
  {
    "father_salary": 50000,
    "mother_salary": 25000,
    "divorce_status": "Divorced",
    "reason_for_divorce": "Incompatibility",
    "child_age": 7
  }
  ```
  Response:
  ```json
  { "custody": "Mother", "compensation": 12345.67 }
  ```

### Sample cURL
```bash
# Summarization
curl -X POST http://localhost:5000/upload \
  -F "file=@/path/to/document.pdf"

# Prediction
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "father_salary": 50000,
    "mother_salary": 25000,
    "divorce_status": "Divorced",
    "reason_for_divorce": "Incompatibility",
    "child_age": 7
  }'
```

## Frontend – Local Setup (React + Vite + TS)
```powershell
cd frontened
npm install

# Start dev server (usually http://localhost:5173)
npm run dev

# Build for production (outputs dist/)
npm run build
```

Environment configuration:
- If you use a custom backend URL, create `frontened/.env` with e.g.:
  ```
  VITE_API_BASE_URL=http://localhost:5000
  ```
- Firebase credentials live in `frontened/src/config/firebase.ts`. Prefer using envs and do not commit secrets.

Serving the frontend:
- Option A (separate): run frontend dev on port 5173 and backend on 5000 (CORS is enabled on Flask).
- Option B (single container): build the frontend and copy its build into `backened/static/` so Flask serves it.

## Docker – One-Container Build & Run
The Dockerfile is set to serve the Flask app via Gunicorn on port 10000 and expects prebuilt or existing static files in `backened/static/`.

```bash
# From repository root
docker build -t justifai .
docker run -p 10000:10000 --name justifai --rm justifai
```

Then open `http://localhost:10000`.

Notes:
- Docker installs Python dependencies, downloads NLTK `punkt`, and starts Gunicorn: `backened.check:app`.
- If you want the latest frontend in the container, build the frontend locally and ensure the build output is present in `backened/static/` before building the image, or extend the Dockerfile to build the frontend.

## Model Artifacts & Data
- Trained models are saved under `backened/models/` (`custody_model.pkl`, `comp_model.pkl`).
- The backend can train them automatically if missing, using `backened/data/Modified_Final_Database.xlsx`.
- Consider using Git LFS for large `.pkl` and `.xlsx` files.

## Recommended .gitignore
Create a `.gitignore` at the repository root with:
```
# Python
.venv/
__pycache__/
*.py[cod]

# Node
frontened/node_modules/
frontened/.vite/
frontened/dist/

# App artifacts
backened/uploads/
backened/models/*.pkl
*.xlsx

# Env & secrets
.env
*.env.local
```

## GitHub – Upload Steps
1. Initialize and commit locally
   ```powershell
   git init
   git add .
   git commit -m "chore: initial commit for JustifAi"
   ```
2. Create a new GitHub repository (via GitHub UI). Copy the remote URL.
3. Add remote and push
   ```powershell
   git remote add origin https://github.com/<your-user>/<your-repo>.git
   git branch -M main
   git push -u origin main
   ```
4. (Optional) Configure Git LFS for large files
   ```powershell
   git lfs install
   git lfs track "backened/models/*.pkl"
   git lfs track "*.xlsx"
   git add .gitattributes
   git add backened/models/*.pkl data/*.xlsx || echo Skipping if not present
   git commit -m "chore: track model and data with LFS"
   git push
   ```
5. Add a license (MIT or your choice) and description/badges on GitHub.
6. Protect your secrets: never commit API keys; use `.env` and GitHub Actions secrets.

## Deployment Options
- Docker on any VM or container platform
- Railway, Render, Fly.io, Heroku‑like (use Dockerfile or Procfile equivalents)
- GitHub Actions for CI/CD (build Docker image, push to registry, deploy)

## Troubleshooting
- Port conflicts: change `PORT` or container port mapping.
- NLTK `punkt` not found: run `python -m nltk.downloader punkt`.
- CORS issues: backend already enables CORS via `flask-cors`.
- Missing models/data: ensure `backened/data/Modified_Final_Database.xlsx` exists so training can run.

## License
Add your preferred license (e.g., MIT) as `LICENSE` in the repository root.


