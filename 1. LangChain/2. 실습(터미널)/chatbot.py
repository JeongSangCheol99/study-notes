import truststore
truststore.inject_into_ssl()

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

model = init_chat_model("claude-sonnet-5-5", model_provider="anthropic")

# 대화 기록 리스트 (SystemMessage는 챗봇의 성격과 규칙을 정하는 지시문)
messages = [
    SystemMessage("너는 친절한 한국어 도우미야. 짧고 명확하게 답해줘.")
]

print("챗봇을 시작합니다! (종료하려면 'quit' 입력)")
print("-" * 40)

while True:
    user_input = input("나: ")

    if user_input.strip().lower() in ("quit", "exit", "종료"):
        print("챗봇을 종료합니다. 안녕히 가세요!")
        break

    if not user_input.strip():
        continue

    messages.append(HumanMessage(user_input))   # 1) 내 말을 기록에 추가
    response = model.invoke(messages)            # 2) 기록 전체를 보내 답변 받기
    messages.append(response)                    # 3) AI 답변도 기록에 추가

    # print("챗봇:", response.content)
    print("챗봇:", response.text)
    print()
