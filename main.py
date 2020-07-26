import Algorithm


def main():
    arr = [1, 2, 3, 3, 2, 1]
    print(Algorithm.find_end(arr, lambda x: x == 10))


if __name__ == "__main__":
    main()
