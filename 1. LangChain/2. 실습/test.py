import truststore
truststore.inject_into_ssl()

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model("claude-sonnet-5-5", model_provider="anthropic")
response = model.invoke("안녕! 너는 누구야?")
print(response.content)