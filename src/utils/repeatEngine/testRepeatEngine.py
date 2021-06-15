import asyncio
import unittest
from .repeatEngine import repeat_engine

class TestRepeat_engine(unittest.TestCase):

  #deveria retornar uma lista de resultados de um ação qualquer
  def test_repeat_engine_return1(self):
      
      def soma():
          return 1 + 1
      
      loop = asyncio.get_event_loop()
      result = loop.run_until_complete(repeat_engine(soma))
      loop.close()
      resultType = type(result['list'])
      arrayType = type([]) 

      self.assertEqual(resultType, arrayType)

  # deveria retornar uma lista de resultados com somas
  def test_repeat_engine_return2(self):
    def soma(value):
        return 1 + value
    
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(repeat_engine(soma,[1]))
    loop.close()
    resultSoma = result['list'][0]
    self.assertEqual(resultSoma, 2)

if __name__ == '__main__':
    unittest.main()