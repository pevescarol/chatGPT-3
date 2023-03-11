# Doc: https://platform.openai.com/docs/guides/chat/introduction
import openai
import config
import typer
from rich import print
from rich.table import Table


def main():
    openai.api_key = config.api_key

    print("[bold yellow]ChatGPT API con Python[/bold yellow]")

    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir de la aplicación")
    table.add_row("new", "Crear nueva conversación")

    print(table)

    # contexto del asistente
    context = [
        {"role": "system", "content": "Eres un asistente muy útil."}]

    messages = [context]

    while True:
        content = __prompt()

        if content == "new":
            print("Nueva conversación")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # solo quiero imprimir el messsage, osea la respuesta
        response_content = response.choices[0].message.content

        # le damos contexto al chat para que entienda de que estabamos hablando
        messages.append({"role": "assistant", "content": response})

        print(f"[bold yellow]> [/bold yellow] [green]{response_content}[/green]")


def __prompt():
    prompt = typer.prompt("\n> Escribe acá tu pregunta...")

    if prompt == "exit":
        exit = typer.confirm("¿Estas segurx?")
        if exit:
            print("Hasta luego!")
            raise typer.Abort()  # se detiene la app de tyoer
        return  __prompt()
    return prompt


if __name__ == "__main__":
    typer.run(main)