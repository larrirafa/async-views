import asyncio
import httpx
from django.http import HttpResponse


async def async_view(request):
    print("Iniciando contador e requisição")

    async def contador():
        for i in range(1, 6):
            await asyncio.sleep(1)
            print(f"Contador: {i}")

    async def requisicao():
        async with httpx.AsyncClient() as client:
            response = await client.get("https://jsonplaceholder.typicode.com/todos?_limit=5")
            data = response.json()
            print("\nDados recebidos da API:")
            for todo in data:
                print(f"- {todo['title']}")
            return data

    # Executa contador e requisição simultaneamente
    contador_task = asyncio.create_task(contador())
    requisicao_task = asyncio.create_task(requisicao())

    # Aguarda ambas terminarem
    await asyncio.gather(contador_task, requisicao_task)

    print("\nFinalizou tudo!")
    return HttpResponse("Contagem e requisição concluídas — veja o terminal para os detalhes.")
