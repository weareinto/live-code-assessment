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

* Open your browser and go to [http://localhost:8000](http://localhost:8000)
* API docs are at [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📋 Task Breakdown by File
To complete this assessment, you'll need to implement functionality across multiple files. Below is a detailed breakdown of what needs to be done in each file:

### 1. 📝 **config.py** - Settings Management
**What to implement:**
- Create a FastAPI-compatible settings class using `pydantic-settings`
- Load environment variables from `.env` file (`API_KEY`, `MODEL_NAME`)
- Replace the empty `get_settings()` function to return the settings instance

**Requirements:**
- Use `BaseSettings` from `pydantic_settings`
- Load `API_KEY` and `MODEL_NAME` from environment variables
- Make settings available throughout the app

---

### 2. 📊 **schemas.py** - Request/Response Models
**What to implement:**
- Create Pydantic models for API request and response validation
- Add model name validation to ensure only supported models are allowed

**Required schemas:**
- `MessageRequest`: Contains `message` (str) and `model_name` (str)
- `MessageResponse`: Contains the LLM response data
- `MessageHistory`: For retrieving stored messages
- Model name validator that checks against supported models in environment

---

### 3. 🚀 **main.py** - API Endpoints
**What to implement:**
- Create POST endpoint `/generate` for LLM message generation
- Create GET endpoint `/messages` to retrieve conversation history
- Add proper dependency injection for database sessions
- Implement API key authentication via headers

**Endpoint specifications:**
- **POST `/generate`**: 
  - Accepts `MessageRequest` body
  - Requires `API_KEY` in headers
  - Uses LLM class to generate response
  - Stores input/output in database
  - Returns generated response
- **GET `/messages`**: 
  - Returns all stored messages from database
  - Use proper Pydantic response models

---

### 4. 🤖 **ai.py** - LLM Response Generation
**What to implement:**
- Update `generate_response()` method to replace placeholder tokens
- Replace `{name}`, `{country}`, `{industry}` with values from KEYS dictionary
- **BONUS**: Integrate with retriever to get top relevant tweet

**Example transformation:**
```
Input: "Hi {name}, we're in {country}"
Output: "Hi INTO AI, we're in Canada"
```

---

### 5. 🗄️ **retriever.py** - Vector Search (BONUS)
**What to implement:**
- Load tweets from `data/tweets.json`
- Create FAISS vector store with tweet documents
- Set tweet text as page content and author info as metadata
- Provide retrieval functionality for relevant tweets

**Requirements:**
- Load JSON data and convert to LangChain Documents
- Use existing FAISS and FakeEmbeddings setup
- Make retriever available for LLM class integration

---

### 6. ⚡ **background.py** - Background Tasks (BONUS)
**What to implement:**
- Create FastAPI background task function
- Check if "INTO AI" exists in generated message output
- Delete message from database if "INTO AI" is not found
- Integrate with the main message generation endpoint

---

## 🎯 Core Requirements Summary

### **MUST HAVE (Required for completion):**
1. [ ] **Settings Management** (`config.py`)
   - FastAPI settings class with environment variable loading

2. [ ] **Request/Response Schemas** (`schemas.py`)
   - Pydantic models for API validation
   - Model name validation

3. [ ] **API Endpoints** (`main.py`)
   - POST `/generate` - Generate LLM responses with authentication
   - GET `/messages` - Retrieve conversation history
   - Database integration for storing messages

4. [ ] **LLM Token Replacement** (`ai.py`)
   - Replace `{key}` placeholders with actual values from KEYS dictionary

### **BONUS (Optional for extra credit):**
5. [ ] **Vector Retrieval** (`retriever.py`)
   - Load tweets and create searchable vector store
   - Integrate top tweet retrieval in LLM generation

6. [ ] **Background Tasks** (`background.py`)
   - Content validation and cleanup via background processing

---

## 🔧 Implementation Notes

- **Authentication**: Use API key from headers, validate against environment variable
- **Database**: Messages are automatically stored using the existing SQLAlchemy models
- **Error Handling**: Return appropriate HTTP status codes for authentication failures
- **Testing**: Use FastAPI's automatic documentation at `/docs` to test your endpoints
