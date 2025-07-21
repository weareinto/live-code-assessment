from config import settings


WORD = "INTO AI"

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
        self.model_name = settings.MODEL_NAME


    # TODO: Replace the {number} with the mapped KEYS
    # Exp: "Hi, {1}, We r {2}" -> "Hi, INTO AI, We r INTO AI INTO AI"
    async def generate_response(self, prompt: str) -> str:

        response = f"Generated response for prompt: {prompt}"
 
        return response