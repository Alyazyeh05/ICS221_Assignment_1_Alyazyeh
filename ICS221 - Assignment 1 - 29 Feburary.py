import time
import matplotlib.pyplot as plt
import numpy as np


# Time Complexity Functions
def linear(n):
    return n


def nlogn(n):
    return n * np.log(n)


# Chocolate Distribution Algorithm
def distribute_chocolates_iter(chocolates, students):
    if len(chocolates) < len(students):
        return "Not enough chocolates for each student."

    distribution = {}
    for i, student in enumerate(students):
        distribution[student] = chocolates[i]

    return distribution, linear(len(chocolates))


def distribute_chocolates_rec(chocolates, students, distribution=None, index=0):
    if len(chocolates) < len(students):
        return "Not enough chocolates for each student."

    if distribution is None:
        distribution = {}

    if index == len(students):
        return distribution, linear(len(chocolates))

    distribution[students[index]] = chocolates[index]
    return distribute_chocolates_rec(chocolates, students, distribution, index + 1)


# Sorting Functions
def sort_by_weight(chocolates):
    return sorted(chocolates, key=lambda x: x['weight']), nlogn(len(chocolates))


def sort_by_price(chocolates):
    return sorted(chocolates, key=lambda x: x['price']), nlogn(len(chocolates))


# Searching Function
def search_chocolate(chocolates, target, key='price'):
    chocolates, sorting_time = sort_by_weight(chocolates)
    left, right = 0, len(chocolates) - 1
    while left <= right:
        mid = (left + right) // 2
        if chocolates[mid][key] == target:
            return chocolates[mid], sorting_time + nlogn(len(chocolates))
        elif chocolates[mid][key] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None, sorting_time + nlogn(len(chocolates))


# Timing and Plotting
def plot_times_complexity(x_values, y_values, xlabel, ylabel, title):
    plt.plot(x_values, y_values)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    chocolates_range = np.arange(1, 100, 5)
    chocolates_list = [{'weight': i, 'price': i, 'type': 'dark'} for i in chocolates_range]
    students = ['Alice', 'Bob', 'Charlie']

    # Task 1: Chocolate Distribution
    distribution_iter_complexities = [linear(n) for n in chocolates_range]
    distribution_rec_complexities = [linear(n) for n in chocolates_range]
    plot_times_complexity(chocolates_range, distribution_iter_complexities, 'Number of Chocolates', 'Time Complexity',
                          'Iterative Distribution Complexity')
    plot_times_complexity(chocolates_range, distribution_rec_complexities, 'Number of Chocolates', 'Time Complexity',
                          'Recursive Distribution Complexity')

    # Task 2: Sorting
    sorting_weight_complexities = [nlogn(n) for n in chocolates_range]
    sorting_price_complexities = [nlogn(n) for n in chocolates_range]
    plot_times_complexity(chocolates_range, sorting_weight_complexities, 'Number of Chocolates', 'Time Complexity',
                          'Sorting by Weight Complexity')
    plot_times_complexity(chocolates_range, sorting_price_complexities, 'Number of Chocolates', 'Time Complexity',
                          'Sorting by Price Complexity')

    # Task 3: Searching
    searching_complexities = [nlogn(n) for n in chocolates_range]
    plot_times_complexity(chocolates_range, searching_complexities, 'Number of Chocolates', 'Time Complexity',
                          'Binary Search Complexity')