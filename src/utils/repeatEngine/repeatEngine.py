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
    try:
      async def taskProcess(iteraction, process_time):
        try:
          await asyncio.sleep(process_time)
          if (type(param) == type([])):
            results["list"].append(iteraction(*param))
          else:
            results["list"].append(iteraction())
        except:
          raise TypeError('Erro em uma tarefa do motor de repetição')

      for i in range(const_iteraction):
          tasks.append(
              asyncio.create_task(
                  taskProcess(iteraction, process_time)
              )
          )
          process_time += const_time

      loopTask = asyncio.shield(asyncio.gather(*tasks))

      async def engine():
        results['inLoop'] = True
        try:
          await loopTask
        except:
          None
        finally:
          results['inLoop'] = False

      def cancel(): 
        loopTask.cancel()

      results['engine'] = engine
      results['cancel'] = cancel

      return results
    except:
      raise TypeError('Erro no motor de repetição') 