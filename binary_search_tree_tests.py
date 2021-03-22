import unittest
from binary_search_tree import *
from queue_array import Queue

class TestLab4(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        self.assertFalse(bst.search(10))
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])

    def test_all(self):
        test = BinarySearchTree()
        self.assertTrue(test.is_empty())
        self.assertEqual(test.find_min(), None)
        self.assertEqual(test.find_max(), None)
        self.assertEqual(test.tree_height(), None)
        self.assertEqual(test.inorder_list(), [])
        self.assertEqual(test.preorder_list(), [])
        test.insert(25, '1000')
        self.assertFalse(test.is_empty())
        test.insert(21, '1001')
        test.insert(23, '1002')
        test.insert(24, '1003')
        test.insert(19, '1004')
        test.insert(20, '1005')
        test.insert(26, '1006')
        test.insert(28, '1007')
        test.insert(23, '1008')
        self.assertTrue(test.search(20))
        self.assertFalse(test.search(100))
        self.assertEqual(test.find_min(), (19, '1004'))
        self.assertEqual(test.find_max(), (28, '1007'))
        self.assertEqual(test.tree_height(), 3)
        self.assertEqual(test.inorder_list(), [19, 20, 21, 23, 24, 25, 26, 28])
        self.assertEqual(test.preorder_list(), [25, 21, 19, 20, 23, 24, 26, 28])
        self.assertEqual(test.level_order_list(),  [25, 21, 26, 19, 23, 28, 20, 24])
    
    def test_more(self):
        b = BinarySearchTree()
        self.assertEqual(b.level_order_list(), [])

    def test_queue_1(self):
        #testing the isEmpty and is full methods
        queue = Queue(0)
        self.assertTrue(queue.is_empty())
        
        queue = Queue(1)
        queue.enqueue('hey')
        self.assertTrue(queue.is_full())
        self.assertFalse(queue.is_empty())

    def test_queue_2(self):
        #checks the raise Index error Fucntions
        queue = Queue(None)
        with self.assertRaises(IndexError):
            queue.enqueue('a')
        with self.assertRaises(IndexError):
            queue.dequeue()

    def test_queue_3(self):
        #checks the dequeue and enqueue methods are working together well
        queue = Queue(2)
        queue.enqueue('first')
        queue.enqueue('second')
        self.assertEqual(queue.dequeue(), 'first')
        self.assertEqual(queue.dequeue(), 'second')

    def test_queue_4(self):
        q = Queue(2)
        self.assertEqual(q.size(), 0)
        q.enqueue(1)
        self.assertEqual(q.size(), 1)

    def test_queue_5(self):
        q = Queue(2)
        q.enqueue(3)
        q.enqueue(4)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)
        q.enqueue('a')
        q.enqueue('b')
        self.assertEqual(q.dequeue(), 'a')
        self.assertEqual(q.dequeue(), 'b')

    def test_queue_6(self):
        q = Queue(0)
        with self.assertRaises(IndexError):
            q.enqueue('hello')
        
    def test_queue_7(self):
        q = Queue(1)
        with self.assertRaises(IndexError):
            q.dequeue()


if __name__ == '__main__': 
    unittest.main()