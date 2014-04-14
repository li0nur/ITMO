# coding: utf-8

from random import choice


class Vertex(object):

    def __init__(self, key, l_edge=None, r_edge=None):
        self.left_edge = l_edge
        self.right_edge = r_edge
        self.key = key

    def __str__(self):
        return "(key: %s   lkey: %s   rkey: %s)" % (self.key, self.left_edge, self.right_edge)


class BTree(object):

    def build_tree(self, root_index):
        self.root = Vertex(self.nodes.pop(root_index))
        for val in self.nodes:
            self.add_vertex(self.root, Vertex(val))

    def add_vertex(self, root, vertex):
        if vertex.key >= root.key:
            if root.right_edge is not None:
                self.add_vertex(root.right_edge, vertex)
                return
            else:
                root.right_edge = vertex
        else:
            if root.left_edge is not None:
                self.add_vertex(root.left_edge, vertex)
                return
            else:
                root.left_edge = vertex
        #print "Node: ", root

    def print_tree(self, root):
        if root is not None:
            print "root -> %s \t lChild -> %s \t rChild -> %s" % \
                  (root.key, root.left_edge, root.right_edge)
        if root.left_edge is not None:
            if root.left_edge == self.root.left_edge:
                print "left leg ->"
            self.print_tree(root.left_edge)
        if root.right_edge is not None:
            if root.right_edge == self.root.right_edge:
                print "right leg ->"
            self.print_tree(root.right_edge)

    def in_order_tree_walk(self, node):
        if node is not None:
            self.in_order_tree_walk(node.left_edge)
            print node.key
            self.in_order_tree_walk(node.right_edge)

    def tree_search(self, root, key):
        if root is None or key == root.key:
            return root
        if key < root.key:
            return self.tree_search(root.left_edge, key)
        else:
            return self.tree_search(root.right_edge, key)

    @staticmethod
    def tree_min(x):
        while x.left_edge is not None:
            x = x.left_edge
        return x

    @staticmethod
    def tree_max(x):
        while x.right_edge is not None:
            x = x.right_edge
        return x

    def __str__(self):
        return str(self.root)

    def __init__(self, stack):
        self.nodes = stack  # [::-1]
        self.root = None  # Vertex(stack[-1])

if __name__ == '__main__':
    s = [8, 5, 2, 7, 3, 5, 27, 11, 4, 9, 13]
    t = BTree(s)
    r_ind = s.index(choice(s))
    t.build_tree(r_ind)
    print "-" * 100
    print "PRINT_TREE"
    t.print_tree(t.root)
    print "-" * 100
    print "BTREE.__STR__"
    print t
    print "-" * 100
    print "IN_ORDER_TREE_WALK"
    t.in_order_tree_walk(t.root)
    print "-" * 100
    print "TREE_SEARCH"
    print t.tree_search(t.root, 7), "\n", t.tree_search(t.root, 10)
    print "-" * 100
    print "TREE_MIN & TREE_MAX"
    print "tree minimum: %s \t tree_maximum: %s" % (BTree.tree_min(t.root), BTree.tree_max(t.root))