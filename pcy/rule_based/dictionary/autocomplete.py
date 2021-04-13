"""Make a Autocomplete class to autocomplete incomplete_words.

   It suggests word based on the provided dictionary.

Raises:
    ValueError: When the dictionary is not valid
    ValueError: When incomplete_word is not valid string
    ValueError: When the incomplete_word is empty
    ValueError: When no_of_suggestions is less than zero

Returns:
    str[]: Array of string containing suggestions
"""

from .node import Node


class Autocomplete:
    """Make a Autocomplete class to autocomplete incomplete_words.

    It suggests word based on the provided dictionary.
    """

    def __init__(self, dictionary):
        """Make a Autocomplete class to autocomplete incomplete_words.

        This Autocomplete class uses Dictionary to suggest words.

        Args:
            dictionary (node): Instance of the node class. It can be created using
                                the DictionaryGenerator class.

        Raises:
            ValueError: When the provided dictionary is not valid
        """
        if not isinstance(dictionary, Node):
            raise ValueError("Please provide a valid dictionary")

        self.__dictionary = dictionary

    def autocomplete(self, incomplete_word, no_of_suggestions):
        """Return an array of suggestions.

        It returns the suggestions based on incomplete_word and no_of_suggestions.

        Args:
            incomplete_word (str): Incomplete word to autocomplete
            no_of_suggestions (int): Number of suggestions to provide

        Raises:
            ValueError: When the incomplete_word is not valid
            ValueError: When incomplete_word is empty
            ValueError: When the no_of_suggestions is less than zero

        Returns:
            str[]: Array of string containing suggestions
        """
        if not isinstance(incomplete_word, str):
            raise ValueError("Please provide a valid incomplete_word")

        if not incomplete_word:
            raise ValueError(
                "Invalid incomplete_word, please provide at least once character"
            )

        if no_of_suggestions < 1:
            raise ValueError("Please provide a valid no_of_suggestions")

        return self.__dictionary.autocomplete_incomplete_word(
            incomplete_word, no_of_suggestions
        )
