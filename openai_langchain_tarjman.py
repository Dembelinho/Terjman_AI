from os import environ
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from tarjman_models import *
from openai import OpenAI


# Create Template 
def create_propmt(prompt_ansewer):
    our_prompt = """Question: {question} Answer: """+prompt_ansewer
    prompt = PromptTemplate.from_template(our_prompt)
    return prompt
# Generate Answer From Question+[Template]
def generate_openai_answer(question,context,key_openai):
    prompt=create_propmt(context)
    llm = ChatOpenAI(openai_api_key=key_openai, model='gpt-4-turbo', temperature=0.0)
    llm_chain = prompt | llm
    response= llm_chain.invoke(question)
    return response.content

dr_en_tarjman=load_tarjman("dr_en")   
en_dr_tarjman=load_tarjman()
# darija Tarjman To LLm Model
def darija_to_llm(darija_query:str,openai_api_key):
    english_query=from_dr_en(darija_query,dr_en_tarjman)
    answer_english=generate_openai_answer(english_query,"Answer like you're a moroccan person. in very sample 20 words",openai_api_key)
    return answer_english

    
# final Darija Answer
def get_darija_answer(dr_query):
    load_dotenv()
    openai_api_key = environ.get('OPENAI_API_KEY')
    result=darija_to_llm(dr_query,openai_api_key)
    darija_result=from_en_dr(result,en_dr_tarjman)
    return darija_result
# Generate Image
def get_darija_image(dr_query):
    load_dotenv()
    openai_api_key = environ.get('OPENAI_API_KEY')
    client = OpenAI(api_key=openai_api_key)
    english_query=from_dr_en(dr_query,dr_en_tarjman)
    print(english_query)
    response = client.images.generate(
    model="dall-e-3",
    prompt=english_query,
    size="1024x1024",
    quality="hd",
    n=1,
    )
    image_url = response.data[0].url
    return image_url
#------------------------------
#       *****Test****** 
#------------------------------
"""
if __name__ == "__main__":
    #dr_query="شكوناهو المغرب، وباش معروف"
    #get_darija_answer(dr_query)
    dr_query="اتاي مغربي"
    print(get_darija_image(dr_query))
"""
    