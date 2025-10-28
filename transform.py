from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering

def create_simple_llm():
    """
    Creates a simple LLM using GPT-2 model
    """
    model_name= "distilgpt2"
    
    generator = pipeline('text-generation', model=model_name,pad_token_id=50265)
    return generator

generator = create_simple_llm()
prompt = 'once upon a time'
generated_text = generator(prompt, max_length=1000,num_return_sequences=1,truncation=True)
print(generated_text[0]['generated_text'])