from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from datasets import load_dataset
import sacremoses
from sklearn.model_selection import train_test_split
from huggingface_hub import login


# Tarjmans From Eng To Darija With nllb 
def load_tarjman_dr_en():
    tarjman_dr_en_tokenizer = AutoTokenizer.from_pretrained(
    "facebook/nllb-200-3.3B", token=True, src_lang="ary_Arab"
    )
    tarjman_dr_en_model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-3.3B", token=True)
    return {"model":tarjman_dr_en_model,"tokenizer":tarjman_dr_en_tokenizer}

def from_dr_en(sentence,tarjman_dr_en):
    encod_example=tarjman_dr_en['tokenizer'](sentence, return_tensors="pt")
    translated_tokens = tarjman_dr_en['model'].generate(**encod_example, forced_bos_token_id=tarjman_dr_en['tokenizer'].lang_code_to_id["eng_Latn"], max_length=30)
    result=tarjman_dr_en['tokenizer'].batch_decode(translated_tokens, skip_special_tokens=True)[0]
    return result

# Tarjams From Darija To English With Atlasia 
def load_tarjman_en_dr():
    tarjman_en_dr_tokenizer = AutoTokenizer.from_pretrained("atlasia/Terjman-Large")
    tarjman_en_dr_model = AutoModelForSeq2SeqLM.from_pretrained("atlasia/Terjman-Large")
    return {"model":tarjman_en_dr_model,"tokenizer":tarjman_en_dr_tokenizer}
def from_en_dr(sentence,tarjman_en_dr):
    encod_example=tarjman_en_dr["tokenizer"]([sentence],return_tensors="pt")
    encod_res=tarjman_en_dr["model"].generate(**encod_example)
    result=tarjman_en_dr["tokenizer"].batch_decode(encod_res,skip_special_tokens=True)
    return result

# Load Models
def load_tarjman(tarjman_model="en_dr"):
    if tarjman_model=="en_dr":
        return load_tarjman_en_dr()
    return load_tarjman_dr_en()

#------------------------------
#       *****Test****** 
#------------------------------
""" if __name__ == "__main__":
    dr_en_tarjman=load_tarjman("dr_en")   
    en_dr_tarjman=load_tarjman() 
    result1=from_dr_en("عفاك إمتا غيجي الترام",dr_en_tarjman)
    print(result1)
    result2=from_en_dr(result1,en_dr_tarjman)
    print(result2)
"""
