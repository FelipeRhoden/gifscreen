import asyncio
import time
import unittest
from .repeatEngine import repeat_engine

class TestRepeat_engine(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        loop = asyncio.get_event_loop()
        loop.close()

    #deveria retornar um dicinionário com os seguintes atributos {inLoop, list, engine, cancel}
    def test_repeat_engine_dic(self):
        soma = lambda : 1 + 1
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(repeat_engine(soma))
        resultType = type(result)
        dicType = type({}) 
        self.assertEqual(resultType, dicType)
        keys = [*result.keys()]
        expectKeys = ['inLoop', 'list', 'engine', 'cancel']
        self.assertEqual(keys, expectKeys)

    #deveria retornar uma lista de resultados de um ação qualquer
    def test_repeat_engine_list(self):
        soma = lambda : 1 + 1
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(repeat_engine(soma))
        resultType = type(result['list'])
        arrayType = type([]) 

        self.assertEqual(resultType, arrayType)

    # deveria retornar uma lista de resultados com um resultado igual a 2
    def test_repeat_engine_return2(self):
        def soma(value):
            return 1 + value
        
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(repeat_engine(soma,[1]))
        loop.run_until_complete(result['engine']())
        resultSoma = result['list'][0]
        self.assertEqual(resultSoma, 2)
    
    # deveria deveria executar duas repetições em menos de 1 segundo
    def test_repeat_engine_down_1s(self):
        soma = lambda value: 1 + value
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(repeat_engine(soma,[2], 2, 1))
        begin = time.time()
        loop.run_until_complete(result['engine']())
        end = time.time()
        timeLoop = end - begin
        resultList = result['list']
        resultSoma = resultList[0] + resultList[1]
        self.assertEqual(resultSoma, 6)
        self.assertTrue(timeLoop < 1)

    # deveria executar quatros repetições em menos de 2 segundos e mais do que 1
    def test_repeat_engine_down_2s_up_1s(self):
        soma = lambda value: 1 + value
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(repeat_engine(soma,[2], 2, 2))
        begin = time.time()
        loop.run_until_complete(result['engine']())
        end = time.time()
        timeLoop = end - begin
        resultList = result['list']
        listLength = len(resultList) 
        self.assertEqual(listLength, 4)
        self.assertTrue(timeLoop > 1 and timeLoop < 2)

    # deveria dizer se uma loop esta em execução
    def test_repeat_engine_inLoop(self):
        soma = lambda value: 1 + value
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(repeat_engine(soma,[2], 2, 2))
        async def inLoop():
            await asyncio.sleep(0.01)
            self.assertTrue(result['inLoop'])
            
        async def test():
            tasks = []
            tasks.append(asyncio.create_task(result['engine']()))
            tasks.append(asyncio.create_task(inLoop()))
            await asyncio.gather(*tasks)
            
        loop.run_until_complete(test())

    # deveria cancelar um loop
    def test_repeat_engine_cancel(self):
        soma = lambda value: 1 + value
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(repeat_engine(soma,[2], 2, 2))
        async def inLoop():
            await asyncio.sleep(0.9)
            result['cancel']()
            
        async def test():
            tasks = []
            tasks.append(asyncio.create_task(result['engine']()))
            tasks.append(asyncio.create_task(inLoop()))
            await asyncio.gather(*tasks)
            
        try:
          loop.run_until_complete(test())
        except:
          None
        finally:
          resultList = result['list']
          listLength = len(resultList)
          self.assertEqual(listLength, 2)
          resultSoma = resultList[0] + resultList[1]
          self.assertEqual(resultSoma, 6)


if __name__ == '__main__':
    unittest.main()