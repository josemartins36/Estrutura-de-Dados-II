class Node:

    def __init__(self, value):
        self.height = 1
        self.value = value
        self.right = None
        self.left = None

class AVLTree:
    """
    Classe da árvore AVL
    """

    def __init__(self):
        self.root = None

    def _height(self, node: Node) -> int:
        """
        Retorna a altura do nó
        """
        if node is None:
            return 0
        return node.height

    def _imbalance_factor(self, node: Node) -> int:
        """
        Calcula o fator de balanço do nó
        """
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _rotate_left(self, node: Node) -> Node:
        """
        Faz uma rotação à esquerda no nó
        """
        a = node.right
        b = a.left
        a.left = node
        node.right = b

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        a.height = 1 + max(self._height(a.left), self._height(a.right))

        return a

    def _rotate_right(self, node: Node) -> Node:
        """
        Faz uma rotação à direita no nó
        """
        a = node.left
        b = a.right

        a.right = node
        node.left = b

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        a.height = 1 + max(self._height(a.left), self._height(a.right))

        return a

    def _balance(self, node: Node) -> Node:
        """
        Balanceia a partir do nó
        """
        if node is None:
            return node

        node.height = 1 + max(self._height(node.left), self._height(node.right))

        balance = self._imbalance_factor(node)

        if balance > 1:
            if self._imbalance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1:
            if self._imbalance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _search_word(self, node: Node, val: any) -> bool:
        """
        Procurar uma palavra na árvore AVL
        """
        if node is None:
            return False

        if node.value == val:
            return True
        elif val < node.value:
            return self._search_word(node.left, val)
        else:
            return self._search_word(node.right, val)

    def contains(self, val: any) -> bool:
        """
        Checar se a palavra está na árvore
        """
        return self._search_word(self.root, val)

    def _add(self, node: Node, val: any) -> Node:
        """
        Adicionar palavra à árvore
        """
        if node is None:
            return Node(val)
        elif val < node.value:
            node.left = self._add(node.left, val)
        else:
            node.right = self._add(node.right, val)

        return self._balance(node)

    def add(self, val: any):

        if self.contains(val):
            return
        self.root = self._add(self.root, val)

    def _search_prefix(self, node: Node, prefix: str, results: list):
        """
        Procurar palavra através do prefixo
        """
        if node is None:
            return

        if node.value.startswith(prefix):
            results.append(node.value)

        if node.value >= prefix:
            self._search_prefix(node.left, prefix, results)

        self._search_prefix(node.right, prefix, results)

    def words_found_prefix(self, prefix: str) -> list:
        """
        Listar palavras encontradas
        """
        results = []
        self._search_prefix(self.root, prefix, results)
        return results