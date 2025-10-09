import asyncio
import httpx
from django.http import HttpResponse, JsonResponse


async def fetch_todos():
    print("Iniciando busca de dados...")
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/todos?_limit=5")
        data = response.json()
        print("Dados recebidos:")
        for todo in data:
            print(f"- {todo['title']}")
    print("Finalizou busca de dados!")


async def async_api_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(fetch_todos())
    return HttpResponse("Requisição iniciada — processamento em segundo plano.")
