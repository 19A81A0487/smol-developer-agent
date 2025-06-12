import os
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

class SmolDeveloperAgent:
    def __init__(self, model_name='Salesforce/codegen-350M-mono'):
        """
        Initializes the Smol Developer Agent using a code-specialized model.

        Args:
            model_name (str): Hugging Face model name for code generation.
        """
        self.model_name = model_name
        # Load tokenizer and model from Hugging Face hub
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

        # Create a text generation pipeline using the loaded model and tokenizer
        # pad_token_id set to eos_token_id to avoid warnings/errors during generation
        self.generator = pipeline(
            'text-generation',
            model=self.model,
            tokenizer=self.tokenizer,
            pad_token_id=self.tokenizer.eos_token_id
        )

    def generate_code(self, prompt, max_length=128):
        """
        Generates Python code based on the provided prompt.

        Args:
            prompt (str): Instruction or task description.
            max_length (int): Max tokens in the generated output.

        Returns:
            str: Generated Python code.
        """
        try:
            response = self.generator(
                prompt,
                max_length=max_length,
                num_return_sequences=1,
                do_sample=True,        # Enable sampling for diversity
                temperature=0.7,       # Controls randomness (0.7 is moderately creative)
                top_k=50,              # Limits sampling to top 50 candidates
                top_p=0.95             # Nucleus sampling (top 95% probability mass)
            )
            return response[0]['generated_text']
        except OSError as e:
            print(f"Error: {e}")
            print("Ensure the model is accessible and you have required dependencies.")
            return None

if __name__ == "__main__":
    agent = SmolDeveloperAgent(model_name='Salesforce/codegen-350M-mono')

    # A Python prompt to generate code for a function that adds two numbers
    prompt = (
        "# Python 3\n"
        "# Function to add two numbers with docstring and type hints\n"
        "def add_numbers(a: int, b: int) -> int:\n"
    )

    generated_code = agent.generate_code(prompt)

    if generated_code:
        print("\n🧠 Generated Code:")
        print("-" * 40)
        print(generated_code.strip())
        print("-" * 40)

        # Save generated code to a file
        with open("generated_addition.py", "w") as f:
            f.write(generated_code.strip())
        print("📁 Code saved to 'generated_addition.py'")
    else:
        print("❌ Code generation failed.")
