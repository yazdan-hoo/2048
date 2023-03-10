import unittest
import main

class TestLeft(unittest.TestCase):
    def test_left(self):
        
        main.arr = [[2,2,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        main.move_left()
        expected = [[4,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.assertEqual(main.arr,expected )
    
    def test_left2(self):
        main.arr = [[2,0,2,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        main.move_left()
        expected = [[4,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.assertEqual(main.arr,expected )
    
    def test_left3(self):
        main.arr = [[2,0,0,0],[2,0,0,0],[0,0,0,0],[0,0,0,0]]
        main.move_left()
        expected = [[2,0,0,0],[2,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.assertEqual(main.arr,expected )

    def test_can(self):
        main.arr = [[2,0,0,0],[2,0,0,0],[0,0,0,0],[0,0,0,0]]
        result = main.can_move_left()
        expected = False
        self.assertEqual(result,expected )
        
    def test_can1(self):
        main.arr = [[0,0,0,0],[2,0,0,0],[0,0,0,0],[2,0,2,0]]
        result = main.can_move_left()
        expected = True
        self.assertEqual(result,expected )

    def test_can2(self):
        main.arr = [[0,0,0,0],[0,0,0,0],[0,0,0,2],[0,0,0,0]]
        result = main.can_move_left()
        expected = True
        self.assertEqual(result,expected )


unittest.main()





# main.move_left()

# if main.arr == [[4,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]:
#     print("test pass")
# else:
#     print("test failed")