import asyncio

async def repeat_engine(iteraction, rps = 26, sec = 7):
    tasks = []
    const_time = 1/rps
    const_iteraction = sec*const_time
    process_time = 0
    results = []

    async def taskProcess(iteraction, process_time):
        asyncio.sleep(process_time)
        results.append(iteraction())

    for iteraction in range(const_iteraction):
        tasks.append(
            asyncio.create_task(
                taskProcess(iteraction, process_time)
            )
        )
        process_time += const_time
    
    await asyncio.gather(*tasks)

    return results 