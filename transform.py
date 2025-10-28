from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering

def create_simple_llm():
    
    """
    Creates a simple LLM using a small GPT-2 model.
    GPT-2 (smallest version) is perfect for demonstrations as it's:
    - Relatively small (124M parameters)
    - Fast enough to run on CPU
    - Good for understanding basic concepts
    """
    model_name= "distilgpt2"
    
    generator = pipeline('text-generation', model=model_name,pad_token_id=50265)
    return generator

generator = create_simple_llm()
prompt = 'once upon a time'
generated_text = generator(prompt, max_length=1000,num_return_sequences=1,truncation=True)
print(generated_text[0]['generated_text'])

def generate_text(generator,prompt,max_length=1000):
    result = generator(prompt,max_length,num_return_sequences=1,do_sample=True,temperature=0.7)
    return result['0']['generate_text']

def run_llm_demo():
    
    print("🤖 Loading Simple LLM Model...")
    generator = create_simple_llm()
    
    print("\n✨ Simple LLM Demo ✨")
    print("This demo shows basic text generation using a small language model")
    
    prompts= [
        "The quick brown fox"
        "Once upon a time"
        "Pythin programming is"
    ]
    
    for prompt in prompts:
        print("\n Prompt:",prompt)
        print("\n Generated:", generate_text(generator,prompt)) 
        input("\nPress Enter to see next example...")
        
        
        
def interactive_demo():
    """
    Allows users to interact with the model
    """
    generator = create_simple_llm() 
    print("\n🤖 Interactive LLM Demo")
    print("Type your prompts (or 'quit' to exit)")    
    while True:
        prompt = input("\n Enter your prompt: ")
        if prompt.lower() == "quit":
            break
        response = generate_text(generator, prompt) 
        print("\n💭 Generated response:")
        print(response)


