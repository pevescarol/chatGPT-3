# Doc: https://platform.openai.com/docs/guides/chat/introduction
import openai
import config

openai.api_key = config.api_key


# contexto del asistente
messages = [
        {"role": "system", "content": "Eres un asistente muy útil."}]

while True:
    content = input("> Escribe acá tu pregunta...")

    if content == "exit":
        break

    messages.append({"role": "user", "content": content})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # solo quiero imprimir el messsage, osea la respuesta
    response_content = response.choices[0].message.content

    # le damos contexto al chat para que entienda de que estabamos hablando
    messages.append({"role": "assistant", "content": response})

    print(response_content)