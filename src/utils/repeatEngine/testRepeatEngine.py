import unittest
from .repeatEngine import repeat_engine

class TestRepeat_engine(unittest.TestCase):

    #deveria retornar uma lista de resultados de um ação qualquer
    async def test_repeat_engine_return(self):
        
        def soma():
            return 1 + 1
        
        result = await repeat_egine(soma)
        resultType = type(result)
        arrayType = type([]) 
        self.assertEqual(resultType, arrayType)

if __name__ == '__main__':
    unittest.main()