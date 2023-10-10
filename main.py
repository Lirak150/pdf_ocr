from tempfile import NamedTemporaryFile

from src.levenshtein_distance_counter import LevenshteinDistanceCounter
from src.ocr_reader import OCRReader

MAX_LEVENSHTEIN_DISTANCE = 4
MIN_WORD_LENGTH = 5

if __name__ == "__main__":
    aim_word = input("Enter word to find: ")
    file_name = input("Enter filename (file should be in directory ocr_files): ")
    with NamedTemporaryFile() as temp_file:
        ocr_reader = OCRReader(f"/ocr_files/{file_name}", temp_file.name)
        return_code, error = ocr_reader.ocr_file()
        if return_code:
            raise Exception(error)
        levenshtein_distance_counter = LevenshteinDistanceCounter(aim_word, temp_file.name)
        found_words = set()
        for dist, word in levenshtein_distance_counter.count_levenshtein_distance():
            if len(word) > MIN_WORD_LENGTH and dist < MAX_LEVENSHTEIN_DISTANCE:
                found_words.add(word)
        if found_words:
            print(f"Found similar words in pdf - {', '.join(found_words)}.")
        else:
            print(f"Didn't find similar words in pdf.")
