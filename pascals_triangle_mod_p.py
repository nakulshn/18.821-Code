import itertools
def cstr(s):
    return "\033[38;5;4m" + s + "\u001b[0m"

def num_unique_strings_of_length_n_in_pascals_triangle_mod_p(n, p, num_rows_in_triangle_to_check=1000, print_triangle=False, print_disallowed_strings=False):
    triangle_texts = [" "*(num_rows_in_triangle_to_check + 1) + cstr("1")]
    strings = []
    previous_row = [1]
    for i in range(num_rows_in_triangle_to_check):
        current_row = [1] + [(previous_row[element_index - 1] + previous_row[element_index])%p for element_index in range(1, len(previous_row))] + [1]
        new_strings_indices = set()
        for j in range(len(current_row) - n + 1):
            if tuple(current_row[j:j + n]) not in strings:
                strings.append(tuple(current_row[j:j + n]))
                new_strings_indices.add(j)
        if print_triangle:
          triangle_texts.append((num_rows_in_triangle_to_check - i)*" " + ",".join([cstr(str(num)) if j in new_strings_indices else str(num) for j, num in enumerate(current_row)]))
        previous_row = current_row
    if print_triangle:
      print("\n".join(triangle_texts))

    if print_disallowed_strings:
      all_strings = {i for i in itertools.product([0, 1], repeat=n)}
      print(all_strings - set(strings))
    else:
      print(strings)
    return len(strings)
