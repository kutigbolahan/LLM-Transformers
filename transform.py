from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering

def create_simple_llm():
    """
    Creates a simple LLM using GPT-2 model
    """
    model_name= "distillgpt2"