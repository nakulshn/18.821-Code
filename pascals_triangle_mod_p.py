import colorama
from colorama import Fore
from colorama import Style

colorama.init()

def a(n, p):
    triangle_texts = ["1"]
    strings = set()
    previous_row = [1]
    for i in range(1000):
        current_row = [1] + [(previous_row[element_index - 1] + previous_row[element_index])%p for element_index in range(1, len(previous_row))] + [1]
        new_strings_indices = set()
        for j in range(len(current_row) - n + 1):
            if tuple(current_row[j:j + n]) not in strings:
                strings.add(tuple(current_row[j:j + n]))
                new_strings_indices.add(j)
        triangle_texts.append("".join([str(num) if num_index not in new_strings_indices else f"{Fore.GREEN}{num}{Style.RESET_ALL}" for num_index, num in enumerate(current_row)]))
        previous_row = current_row
    print("\n".join(triangle_texts))
    return len(strings)

print(a(2, 7))
