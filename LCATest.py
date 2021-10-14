import unittest
import LCA

class TestLCA(unittest.TestCase):

    def setUp(self):
        self.node1 = self.root = LCA.root = LCA.Node("A")
        self.node2 = self.root.left = LCA.Node("B")
        self.node3 = self.root.right = LCA.Node("C")

        self.node4 = self.node2.left = LCA.Node("D")
        self.node5 = self.node2.right = LCA.Node("E")
        self.node6 = self.node3.left = LCA.Node("F")
        self.node7 = self.node3.right = LCA.Node("G")

        self.node8 = self.node4.left = LCA.Node("H")
        self.node9 = self.node4.right = LCA.Node("I")
        self.node10 = self.node5.right = LCA.Node("J")
        self.node11 = self.node6.right = LCA.Node("K")

        #        A
        #     /     \
        #    B       C
        #   / \     / \
        #  D   E   F   G
        # / \   \   \
        #H   I   J   K

    def test_base1(self):
        self.assertEqual(LCA.getLCA(self.root,"B", "C"), "A")
        self.assertEqual(LCA.getLCA(self.root,"D", "E"), "B")
        self.assertEqual(LCA.getLCA(self.root,"F", "G"), "C")
        self.assertEqual(LCA.getLCA(self.root,"H", "I"), "D")

    def test_base2(self):
        self.assertEqual(LCA.getLCA(self.root,"H", "K"), "A")
        self.assertEqual(LCA.getLCA(self.root,"D", "F"), "A")
        self.assertEqual(LCA.getLCA(self.root,"H", "J"), "B")

    def test_complex(self):
        self.assertEqual(LCA.getLCA(self.root,"B", "G"), "A")
        self.assertEqual(LCA.getLCA(self.root,"C", "H"), "A")
        self.assertEqual(LCA.getLCA(self.root,"H", "E"), "B")
        self.assertEqual(LCA.getLCA(self.root,"D", "J"), "B")
        self.assertEqual(LCA.getLCA(self.root,"G", "K"), "C")

    def test_is_LCA_itself(self):
        self.assertEqual(LCA.getLCA(self.root,"A", "B"), "A")
        self.assertEqual(LCA.getLCA(self.root,"A", "C"), "A")
        self.assertEqual(LCA.getLCA(self.root,"A", "D"), "A")
        self.assertEqual(LCA.getLCA(self.root,"A", "K"), "A")

        self.assertEqual(LCA.getLCA(self.root,"B", "D"), "B")
        self.assertEqual(LCA.getLCA(self.root,"B", "E"), "B")
        self.assertEqual(LCA.getLCA(self.root,"B", "H"), "B")

        self.assertEqual(LCA.getLCA(self.root,"C", "F"), "C")
        self.assertEqual(LCA.getLCA(self.root,"C", "G"), "C")
        self.assertEqual(LCA.getLCA(self.root,"C", "K"), "C")

    def test_same_node(self):
        self.assertEqual(LCA.getLCA(self.root,"A", "A"), "A")
        self.assertEqual(LCA.getLCA(self.root,"B", "B"), "B")
        self.assertEqual(LCA.getLCA(self.root,"C", "C"), "C")
        self.assertEqual(LCA.getLCA(self.root,"D", "D"), "D")
        self.assertEqual(LCA.getLCA(self.root,"F", "F"), "F")
        self.assertEqual(LCA.getLCA(self.root,"H", "H"), "H")
        self.assertEqual(LCA.getLCA(self.root,"K", "K"), "K")

    def test_invalid(self):
        self.assertEqual(LCA.getLCA(self.root,"L", "D"), -1)
        self.assertEqual(LCA.getLCA(self.root,"M", "N"), -1)

    def test_empty(self):
        self.assertEqual(LCA.getLCA(self.root," ", "A"), -1)
        self.assertEqual(LCA.getLCA(self.root," ", " "), -1)
        self.assertEqual(LCA.getLCA(self.root,"", ""), -1)

if __name__ == '__main__':
    unittest.main()