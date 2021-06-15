import asyncio

async def repeat_engine(iteraction, param = None, rps = 1, sec = 1):
    tasks = []
    const_time = 1//rps
    const_iteraction = sec*const_time
    process_time = 0
    results = {
      "inLoop": True,
      "list" : [],
    }

    async def taskProcess(iteraction, process_time):
        await asyncio.sleep(process_time)
        if (type(param) == type([])):
          results["list"].append(iteraction(*param))
        else:
          results["list"].append(iteraction())

    for i in range(const_iteraction):
        tasks.append(
            asyncio.create_task(
                taskProcess(iteraction, process_time)
            )
        )
        process_time += const_time
    
    await asyncio.gather(*tasks)

    return results 