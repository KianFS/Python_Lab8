from abc import ABC, abstractmethod


# **********************part1****************
class FileClass(ABC):
    address = "weirdWords.txt"

    def __init__(self, address):
        self.address = address

    @abstractmethod
    def calculateFreqs(self):
        pass


# **********************part2,3****************
class ListCount(FileClass):

    def calculateFreqs(self):
        f = open(self.address, "r+")
        file_contents = f.read()

        letter_list = []
        frequencies = []

        for letter in file_contents:
            if letter.isalpha() and letter != '\n':
                if letter not in letter_list:
                    letter_list.append(letter)
                    frequencies.append(1)
                else:
                    index = letter_list.index(letter)
                    frequencies[index] += 1
        print("List:")
        print(letter_list)
        print("Resulting list:")
        for i in range(len(letter_list)):
            letter_list[i] += f"={frequencies[i]}"

        f.close()

        print(letter_list)


# **********************part4****************

class DictCount(FileClass):
    def calculateFreqs(self):
        f = open(self.address, "r+")
        file_content = f.read()

        letter_dict = {}
        for char in file_content:
            if char != " " and char != "\n":
                letter_dict.setdefault(char, 0)
        print("Dict:")
        print(letter_dict)
        for character in file_content:
            if character != " " and character != "\n":
                if character in letter_dict:
                    letter_dict[character] += 1
                else:
                    letter_dict[character] = 1

        f.close()
        print("Updated dict:")

        for key in sorted(letter_dict.keys()):
            print(f"'{key}'  {letter_dict[key]}")




# **********************part5**********************

print("**********************part1**********************")

list_count_instance = ListCount("weirdWords.txt")
list_count_instance.calculateFreqs()
print("**********************part2**********************")

dict_count_instance = DictCount("weirdWords.txt")
dict_count_instance.calculateFreqs()
