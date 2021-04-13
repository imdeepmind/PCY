class Node:
    @staticmethod
    def __find_key_in_level(node, key):
        for child in node.children:
            if child.key == key:
                return child

        return False

    @staticmethod
    def __search_tree(word, index=0, node=None):
        if index + 1 > len(word):
            return node

        current_key = word[index]

        child_node = Node.__find_key_in_level(node, current_key)

        if not child_node:
            return False

        return Node.__search_tree(word, index + 1, child_node)

    def __find_nth_words(self, node, no_of_words):
        if self.__found_words > no_of_words:
            return []

        words = []

        if node.word:
            words.append(node.word)
            self.__found_words += 1

        if len(node.children) > 0:
            for child in node.children:
                words += self.__find_nth_words(child, no_of_words)

        return words

    @staticmethod
    def __print_tree(node, level=0):
        level += 1
        message = ""

        dash = "--" * level
        message += f"{dash}{node.__key}({node.__word})"

        if len(node.children) < 1:
            return message

        for child in node.children:
            message += f"\n{Node.__print_tree(child, level)}"

        return message

    # Getters
    @property
    def key(self):
        return self.__key

    @property
    def word(self):
        return self.__word

    @property
    def parent(self):
        return self.__parent

    @property
    def children(self):
        return self.__children

    def __init__(self, key, word=None, parent=None):
        self.__key = key
        self.__word = word
        self.__parent = parent
        self.__children = []
        self.__found_words = 0

    def add_child(self, node):
        if isinstance(node, Node):
            self.__children.append(node)
        else:
            raise ValueError("Please provide a valid node to append")

    def is_child_exists(self, key):
        return True if Node.__find_key_in_level(self, key) else False

    def get_child_node(self, key):
        return Node.__find_key_in_level(self, key)

    def add_word(self, word):
        self.__word = word

    def autocomplete_incomplete_word(self, incomplete_word, no_of_words):
        root_node = Node.__search_tree(incomplete_word.lower(), node=self)

        if not root_node:
            return False

        return self.__find_nth_words(root_node, no_of_words)

    def print_tree(self):
        print(Node.__print_tree(self))
