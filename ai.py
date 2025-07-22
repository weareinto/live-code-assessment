from config import settings



KEYS = {
    "name": "INTO AI",
    "country": "Canada",
    "industry": "AI",
}

class LLM:
    def __init__(self):
        print("Initializing LLM...")
        self.model_name = settings.MODEL_NAME


    # TODO: Replace the {number} with the mapped KEYS
    # Exp: "Hi, {name}, We r in {country}" -> "Hi, INTO AI, We r in Canada"
    # TODO: Bonus if u used the retriever to get the top 1 tweet
    async def generate_response(self, prompt: str) -> str:

        response = f"Generated response for prompt: {prompt}"
 
        return response