def validate_with_users(recognized_elements, ground_truth):
    correct = 0
    for element in recognized_elements:
        if element in ground_truth:
            correct += 1
    accuracy = correct / len(ground_truth)
    return accuracy

if __name__ == "__main__":
    recognized_elements = ["Авт. выкл. 3P 16А", "Авт. выкл. 3P 63А"]
    ground_truth = ["Авт. выкл. 3P 16А", "Авт. выкл. 3P 63А"]
    accuracy = validate_with_users(recognized_elements, ground_truth)
    print(f"Accuracy: {accuracy * 100}%")
