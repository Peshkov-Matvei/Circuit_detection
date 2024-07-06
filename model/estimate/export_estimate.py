import csv


def export_estimate(estimate, output_path):
    with open(output_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Item ID", "Total Cost"])
        for item, cost in estimate.items():
            writer.writerow([item, cost])


if __name__ == "__main__":
    estimate = {1: 300, 2: 300}
    export_estimate(estimate, "../data/estimates/estimate.csv")
