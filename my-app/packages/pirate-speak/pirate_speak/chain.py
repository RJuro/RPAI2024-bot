#from langchain_community.chat_models import ChatOpenAI
from langchain_together import Together
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

import os
from dotenv import load_dotenv
load_dotenv()
together_api_key = os.getenv("TOGETHER_API_KEY")

_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Du er en ung mand fra Randers og du opfylder alle stereotyper. Du svarer som sådan en ville gøre.",
        ),
        MessagesPlaceholder("chat_history"),
        ("human", "{text}"),
    ]
)
_model  = Together(
    model="meta-llama/Llama-3-70b-chat-hf",
    temperature=0.7,
    top_k=50,
    top_p=0.7,
    repetition_penalty=1,
    together_api_key=together_api_key
)


# if you update this, you MUST also update ../pyproject.toml
# with the new `tool.langserve.export_attr`
chain = _prompt | _model
