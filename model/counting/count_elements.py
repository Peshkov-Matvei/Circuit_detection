def count_elements(matches):
    count_dict = {}
    for match in matches:
        if match in count_dict:
            count_dict[match] += 1
        else:
            count_dict[match] = 1
    return count_dict


if __name__ == "__main__":
    matches = [1, 2, 1, 1, 2]
    counts = count_elements(matches)
    print(counts)
