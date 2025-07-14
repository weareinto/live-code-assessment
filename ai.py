from config import settings

WORD = "INTO AI "

KEYS = {
    "1": WORD,
    "2": WORD * 2,
    "3": WORD * 3,
    "4": WORD * 4,
    "5": WORD * 5,
}

class LLM:
    def __init__(self):
        print("Initializing LLM...")
        self.api_key = settings.OPENAI_API_KEY
        self.model_name = settings.OPENAI_MODEL_NAME

    
    def vaildate(self) -> bool:
        # Simulate API key validation
        if not self.api_key or not isinstance(self.api_key, str) or self.api_key != "FAKE_OPENAI_KEY":
            raise ValueError("Invalid API key")
        

    # TODO: Replace the {number} with the mapped KEYS
    # Exp: "Hi, {1}, We r {2}" -> "Hi, INTO AI, We r INTO AI INTO AI"
    async def generate_response(self, prompt: str) -> str:
        self.vaildate()
        
        # Simulate response generation
        response = f"Generated response for prompt: {prompt}"

        # TODO: Store the message in the database
        return response