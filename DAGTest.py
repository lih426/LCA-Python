from DAG import DAG
import unittest


class TestDAG(unittest.TestCase):
    
    def test_addNode(self):
        DAG1 = DAG()
        self.assertFalse(DAG1.addNode('A'))
        self.assertFalse(DAG1.addNode('a'))
        self.assertFalse(DAG1.addNode('B'))
        self.assertFalse(DAG1.addNode('1'))
        self.assertFalse(DAG1.addNode('2'))

    def test_add1Node(self):
        DAG2 = DAG()
        DAG2.addNode('A')
        DAG2.printDAG(DAG2.graph)
        self.assertTrue(DAG2.graph == {'A': []})

    def test_addNodeAfterInit(self):
        DAG3 = DAG()
        self.assertFalse(DAG3.addNode('A'))

    def test_cyclesInDAG1(self):
        DAG4 = DAG()
        DAG4.addNode('2')
        DAG4.addNode('3')
        DAG4.addEdge('2', '3')
        self.assertTrue(DAG4)
        self.assertTrue(DAG4.Wrapper_DFS(DAG4.graph))

    def test_cyclesInDAG2(self):
        DAG5 = DAG()
        DAG5.addNode('4')
        DAG5.addNode('2')
        DAG5.addNode('1')
        DAG5.addEdge('2', '4')
        self.assertTrue(DAG5)
        self.assertTrue(DAG5.Wrapper_DFS(DAG5.graph))

    def test_cyclesInDAG3(self):
        DAG6 = DAG()
        DAG6.addNode('2')
        DAG6.addNode('3')
        DAG6.addEdge('2', '3')
        DAG6.addNode('4')
        DAG6.addNode('5')
        DAG6.addEdge('3', '4')
        DAG6.addEdge('4', '2')
        self.assertFalse(DAG6.Wrapper_DFS(DAG6.graph))
        self.assertTrue(DAG6)

    def test_intLCA(self):
        DAG7 = DAG()
        DAG7.addNode(1)
        DAG7.addNode(2)
        DAG7.addNode(3)
        DAG7.addNode(4)
        DAG7.addNode(5)
        DAG7.addNode(6)
        DAG7.addNode(7)
        DAG7.addNode(8)
        DAG7.addEdge(1, 2)
        DAG7.addEdge(1, 3)
        DAG7.addEdge(1, 4)
        DAG7.addEdge(2, 3)
        DAG7.addEdge(3, 5)
        DAG7.addEdge(2, 6)
        DAG7.addEdge(5, 6)
        DAG7.addEdge(6, 8)
        DAG7.addEdge(4, 7)
        DAG7.Wrapper_LCA(DAG7.graph, 8, 5)
        self.assertTrue(DAG7.Wrapper_LCA(DAG7.graph, 8, 5) == 5)

    def test_stringLCA1(self):
        DAG8 = DAG()
        DAG8.addNode('A')
        DAG8.addNode('B')
        DAG8.addNode('C')
        DAG8.addNode('D')
        DAG8.addNode('E')
        DAG8.addNode('F')
        DAG8.addNode('G')
        DAG8.addNode('H')
        DAG8.addEdge('A', 'B')
        DAG8.addEdge('A', 'C')
        DAG8.addEdge('A', 'D')
        DAG8.addEdge('B', 'C')
        DAG8.addEdge('C', 'E')
        DAG8.addEdge('B', 'F')
        DAG8.addEdge('E', 'F')
        DAG8.addEdge('F', 'H')
        DAG8.addEdge('D', 'G')
        DAG8.Wrapper_LCA(DAG8.graph, 'H', 'E')
        self.assertTrue(DAG8.Wrapper_LCA(DAG8.graph, 'H', 'E') == 'E')

    def test_stringLCA2(self):
        DAG9 = DAG()
        DAG9.addNode('A')
        DAG9.addNode('B')
        DAG9.addNode('C')
        DAG9.addNode('D')
        DAG9.addNode('E')
        DAG9.addNode('F')
        DAG9.addNode('G')
        DAG9.addNode('H')
        DAG9.addEdge('A', 'B')
        DAG9.addEdge('A', 'C')
        DAG9.addEdge('A', 'D')
        DAG9.addEdge('B', 'C')
        DAG9.addEdge('B', 'F')
        DAG9.addEdge('C', 'E')
        DAG9.addEdge('D', 'G')
        DAG9.addEdge('E', 'F')
        DAG9.addEdge('F', 'H')
        self.assertTrue(DAG9.Wrapper_LCA(DAG9.graph, 'H', 'G') == 'A')
        self.assertTrue(DAG9.Wrapper_LCA(DAG9.graph, 'A', 'G') == 'A')
        self.assertTrue(DAG9.Wrapper_LCA(DAG9.graph, 'G', 'B') == 'A')
        self.assertFalse(DAG9.Wrapper_LCA(DAG9.graph, 'H', 'F') == 'A')

    def test_stringLCA3(self):
        DAG10 = DAG()
        DAG10.addNode('A')
        DAG10.addNode('B')
        DAG10.addNode('C')
        DAG10.addNode('D')
        DAG10.addNode('E')
        DAG10.addNode('F')
        DAG10.addNode('G')
        DAG10.addNode('H')
        DAG10.addEdge('A', 'B')
        DAG10.addEdge('A', 'C')
        DAG10.addEdge('A', 'D')
        DAG10.addEdge('B', 'C')
        DAG10.addEdge('B', 'F')
        DAG10.addEdge('C', 'E')
        DAG10.addEdge('D', 'G')
        DAG10.addEdge('E', 'F')
        DAG10.addEdge('F', 'H')
        self.assertTrue(DAG10.Wrapper_LCA(DAG10.graph, 'H', 'G') == 'A')
        self.assertTrue(DAG10.Wrapper_LCA(DAG10.graph, 'A', 'G') == 'A')
        self.assertTrue(DAG10.Wrapper_LCA(DAG10.graph, 'G', 'B') == 'A')
        self.assertFalse(DAG10.Wrapper_LCA(DAG10.graph, 'H', 'F') == 'A')

    def test_oneNoneNodeLCA(self):
        DAG11 = DAG()
        DAG11.addNode('A')
        DAG11.addNode('B')
        DAG11.addEdge('A', 'B')
        self.assertTrue(DAG11.Wrapper_LCA(DAG11.graph, 'A', 'G') == None)

    def test_emptyGraphLCA(self):
        DAG12 = DAG()
        self.assertTrue(DAG12.Wrapper_LCA(DAG12.graph, None, None) == None)


if __name__ == '__main__':
    unittest.main()