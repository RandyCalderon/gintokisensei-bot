from charguana import get_charset
import csv
import re

hiragana = list(get_charset('hiragana'))
katakana = list(get_charset('katakana'))

reader_result = []

with open("./words/test.csv", "r", encoding="utf8") as word_file:
    csv_reader = csv.reader(word_file, delimiter=',')
    for row in csv_reader:
        temp_dict = {}
        for value in row:
            # (fkaokfaok
            match = re.findall("[/(*[a-zA-Z]+[;/)\s]*", value)
            alphabet_list = [c for word in match for c in word]

            for char in value:
                # print([char], end='')
                if char not in hiragana and char not in katakana and char not in alphabet_list:
                    temp_dict["kanji"] = value
                elif char in katakana:
                    temp_dict["katakana"] = value
                    # print(f"Katakana Value, {temp_dict}")
                elif char in hiragana:
                    temp_dict["hiragana"] = value
                else:
                    temp_dict["meaning"] = value
        reader_result.append(temp_dict)

print("Result List", reader_result)
