# See https://huggingface.co/smangrul/falcon-40B-int4-peft-lora-sfttrainer
# import os
# os.environ["CUDA_VISIBLE_DEVICES"]="0"
import os.path

from dataclasses import dataclass, field
from typing import Optional

import torch
from datasets import load_dataset
from peft import LoraConfig
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    HfArgumentParser,
    AutoTokenizer,
    TrainingArguments,
)

from trl import SFTTrainer

from peft import (
    prepare_model_for_kbit_training,
    LoraConfig,
    get_peft_model,
    PeftModel
)

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype="bfloat16",
    bnb_4bit_use_double_quant=False,
)

device_map = {"": 0}
tokenizer = AutoTokenizer.from_pretrained("tiiuae/falcon-7b")
model = AutoModelForCausalLM.from_pretrained(
    "tiiuae/falcon-7b", quantization_config=bnb_config, device_map=device_map, trust_remote_code=True
)
model = prepare_model_for_kbit_training(model, use_gradient_checkpointing=False)
model_id = os.path.join("./results/checkpoint-9990")
model = PeftModel.from_pretrained(model, model_id)

text = '### Human: Write a tweet celebrating the Apache-2 release of Falcon models which are generative Large Language Models (LLMs) on which you have been finetuned. Previously, it was under a bit of a restrictive license. Make the tweet punchy, energetic, exciting and marketable.### Assitant:'
outputs = model.generate(input_ids=tokenizer(text, return_tensors="pt").input_ids, 
                         max_new_tokens=256, 
                         temperature=0.7, 
                         top_p=0.9,
                         do_sample=True)

print(tokenizer.batch_decode(outputs))

