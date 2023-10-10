from Levenshtein import distance


class LevenshteinDistanceCounter:
    def __init__(self, aim_word: str, filepath: str):
        self._aim_word = aim_word
        self._filepath = filepath

    def count_levenshtein_distance(self):
        with open(self._filepath, mode="r") as read_fd:
            for line in read_fd:
                words_in_line = [word.strip() for word in line.strip().split()]
                for word in words_in_line:
                    yield distance(self._aim_word, word), word
