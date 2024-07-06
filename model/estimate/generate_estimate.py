def generate_estimate(count_dict, prices):
    estimate = {}
    for item, count in count_dict.items():
        estimate[item] = count * prices.get(item, 0)
    return estimate


if __name__ == "__main__":
    count_dict = {1: 3, 2: 2}
    prices = {1: 100, 2: 150}
    estimate = generate_estimate(count_dict, prices)
    print(estimate)
