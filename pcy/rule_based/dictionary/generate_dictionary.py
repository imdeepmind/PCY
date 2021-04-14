"""Generate a dictionary tree based on words.

Raises:
    ValueError: If the path is not valid
    ValueError: If the provided words list is not valid
    ValueError: If the words list is empty
    ValueError: If the path is not valid

Returns:
    node: Dictionary tree node
"""
import pickle

from py_progress import progressbar
from ._node import _Node as Node


class DictionaryGenerator:
    """Generate a tree based on words list.

    Raises:
        ValueError: If the path is not valid
        ValueError: If the provided words list is not valid
        ValueError: If the words list is empty
        ValueError: If the path is not valid

    Returns:
        node: Dictionary tree node
    """

    @staticmethod
    def __generate_tree(word, index=0, node=None):
        """Generate a tree based on the word.

        Args:
            word (str): Word for adding to the tree
            index (int, optional): Index to track the recursive loop.
                                   Defaults to 0.
            node (node, optional): Current node in the dictionary tree.
                                   Defaults to None.
        """
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
        """Load a dictionary from filesystem.

        Args:
            path (str): Path to the saved dictionary

        Raises:
            ValueError: If the path is not valid

        Returns:
            node: Returns a dictionary tree
        """
        if not isinstance(path, str) and not path:
            raise ValueError("Please provide a valid path to load the data")

        with open(path, "rb") as f:
            return pickle.load(f)

    def __init__(self, words):
        """Generate dictionary tree based on words list.

        Args:
            words (str[]): List of words

        Raises:
            ValueError: If the words list is not a valid list
            ValueError: If the words list is empty
        """
        if not isinstance(words, list):
            raise ValueError("Please provide a valid list of words")

        if len(words) < 1:
            raise ValueError("There is no words in the list")

        self.__words = words

    def generate_dictionary(self):
        """Generate a dictionary tree.

        Returns:
            node: Returns a dictionary tree.
        """
        tree = Node("ROOT")

        for index, word in enumerate(self.__words):
            progressbar(
                index,
                len(self.__words),
                f"{index+1}/{len(self.__words)}",
                f"Current Char: {word[0]}",
            )
            DictionaryGenerator.__generate_tree(word.lower(), node=tree)

        print("")

        self.__tree = tree

        return self.__tree

    def add_word_to_dictionary(self, word):
        """Add word to the dictionary.

        Args:
            word (str): Word to add.

        Raises:
            ValueError: If the word is not valid string.
            ValueError: If the word is not a valid word.
            ValueError: If there is no dictionary.
        """
        if isinstance(word, str):
            raise ValueError("Please provide a valid word")

        if not word:
            raise ValueError("Please provide a word to add")

        if not self.__tree:
            raise ValueError("Please create a dictionary first")

        self.__generate_tree(word, node=self.__tree)

    def save_dictionary(self, path):
        """Save dictionary to file.

        Args:
            path (str): Path to store the dictionary.

        Raises:
            ValueError: If the path provided is not valid
        """
        if not isinstance(path, str) and not path:
            raise ValueError("Please provide a valid path to save the data")

        with open(path, "wb") as f:
            pickle.dump(self.__tree, f)
