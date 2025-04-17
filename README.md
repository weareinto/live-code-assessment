# Live Code Assessment

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/weareinto/live-code-assessment.git
cd live-code-assessment
```

2. **Copy the `.env.sample` file to `.env`**

```bash
cp .env.sample .env
```

3. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate    # On Windows use: venv\Scripts\activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

5. **Run the FastAPI app**

```bash
uvicorn main:app --reload
```

6. **Access the app**

Open your browser and go to [http://localhost:8000](http://localhost:8000)  
API docs are at [http://localhost:8000/docs](http://localhost:8000/docs)
