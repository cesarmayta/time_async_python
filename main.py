import asyncio
import time

async def mi_funcion_asincrona():
    await asyncio.sleep(0.3)  # Simulamos una tarea asincrona que toma 2 segundos

async def medir_tiempo():
    inicio = time.time()
    await mi_funcion_asincrona()
    fin = time.time()
    tiempo_transcurrido = fin - inicio
    print(inicio)
    print(fin)
    print(f"Tiempo transcurrido: {tiempo_transcurrido:.2f} segundos")

if __name__ == '__main__':
    asyncio.run(medir_tiempo())
