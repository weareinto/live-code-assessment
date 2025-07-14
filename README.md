# Live Code Assessment

## Requirements

To complete this assessment, please implement the following:

1. [ ] **Environment Setup**
   You must be able to run the project successfully with environment variables defined in the `.env` file.

2. [ ] **Settings Management**
   Create a FastAPI-compatible settings class to load values from the `.env` file and use them throughout your app.

3. [ ] **API Endpoint**
   Create a new API endpoint with the following specs:

   * Accepts a request with a payload containing:
     * `message`: the user's input message.
     * `model_name`: name of the LLM model to use.
   * Validate `model_name` using Pydantic to allow only supported models that exists in the environment variables
   * Requires an `API_KEY` to be passed in the request headers.
     * If the key is missing or invalid, return an authentication error.
   * This endpoint should use the **LLM** class to generate a response and return it to the user.

4. [ ] **Modify LLM class**
   Update the `generate_response` function inside the `LLM` class:
   * Replace any keys/tokens in the prompt with the provided context before generating the final output.


---

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

* Open your browser and go to [http://localhost:8000](http://localhost:8000)
* API docs are at [http://localhost:8000/docs](http://localhost:8000/docs)