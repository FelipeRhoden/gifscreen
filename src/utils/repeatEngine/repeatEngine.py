import asyncio

async def repeat_engine(iteraction, param = None, rps = 1, sec = 1):
    tasks = []
    const_time = 1/rps
    const_iteraction = rps*sec
    process_time = 0
    results = {
      "inLoop": False,
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

    loopTask = asyncio.gather(*tasks)

    async def engine():
      results['inLoop'] = True
      await asyncio.gather(loopTask)
      results['inLoop'] = False

    def cancel(): 
      loopTask.cancel()

    results['engine'] = engine
    results['cancel'] = cancel

    return results 