if __name__ == "__main__":
    country = []
    for _ in range(int(input())):
        country.append(input())
    s = set(country)
    print(len(s))