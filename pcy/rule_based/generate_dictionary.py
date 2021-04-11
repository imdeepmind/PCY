import pickle

from py_progress import progressbar
from .node import Node


class DictionaryGenerator:
    @staticmethod
    def __generate_tree(word, index=0, node=None):
        current_chr = word[index]

        current_word = None
        if len(word) == index + 1:
            current_word = word

        is_child_node_exists = node.get_child_node(current_chr)

        if is_child_node_exists:
            child_node = is_child_node_exists

            if child_node.word is None:
                child_node.add_word(current_word)
        else:
            child_node = Node(current_chr, word=current_word, parent=node)
            node.add_child(child_node)

        if len(word) > index + 1:
            DictionaryGenerator.__generate_tree(word, index=index + 1, node=child_node)

    @classmethod
    def load_dictionary(cls, path):
        if not isinstance(path, str) and not path:
            raise ValueError("Please provide a valid path to load the data")

        with open(path, "rb") as f:
            return pickle.load(f)

    def __init__(self, words):
        if not isinstance(words, list):
            raise ValueError("Please provide a valid list of words")

        if len(words) < 1:
            raise ValueError("There is no words in the list")

        self.__words = words

    def generate_dictionary(self):
        tree = Node("ROOT")

        for index, word in enumerate(self.__words):
            progressbar(
                index,
                len(self.__words),
                f"{index+1}/{len(self.__words)}",
                f"Current Char: {word[0]}",
            )
            DictionaryGenerator.__generate_tree(word.lower(), node=tree)

        self.__tree = tree

        return self.__tree

    def save_dictionary(self, path):
        if not isinstance(path, str) and not path:
            raise ValueError("Please provide a valid path to save the data")

        with open(path, "wb") as f:
            pickle.dump(self.__tree, f)
