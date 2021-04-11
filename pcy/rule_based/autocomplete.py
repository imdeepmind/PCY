from .node import Node


class Autocomplete:
    def __init__(self, dictionary):
        if not isinstance(dictionary, Node):
            raise ValueError("Please provide a valid dictionary")

        self.__dictionary = dictionary

    def autocomplete(self, incomplete_word, no_of_suggestions):
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
