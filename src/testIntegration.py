import unittest
import asyncio
import time
from utils.repeatEngine.repeatEngine import repeat_engine
from utils.screenShot.screenShot import screen_shot

class TestIntegretion(unittest.TestCase):

  #deveria salvar 16 frames por segundo durante 2 segundos
  def test_integration_engine_repeat_print_scree_16fps_2sec(self):
    coordinates = [(0,0,500,500)]
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(repeat_engine(screen_shot, coordinates, 16, 2))
    begin = time.time()
    loop.run_until_complete(results['engine']())
    end = time.time()
    listLength = len(results['list'])
    timeLoop = end - begin
    self.assertEqual(listLength, 32)
    self.assertTrue(timeLoop > 1 and timeLoop <= 2.5)

  #deveria salvar 25 frames por segundo durante 7 segundos
  def test_integration_engine_repeat_print_scree_25fps_7sec(self):
    coordinates = [(0,0,500,500)]
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(repeat_engine(screen_shot, coordinates, 25, 7))
    begin = time.time()
    loop.run_until_complete(results['engine']())
    end = time.time()
    listLength = len(results['list'])
    timeLoop = end - begin
    self.assertEqual(listLength, 25*7)
    self.assertTrue(timeLoop > 6 and timeLoop < 7.5)

if __name__ == '__main__':
    unittest.main()
