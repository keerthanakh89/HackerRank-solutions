def mutate_string(string, position, character):
    return "".join([character if e == position else c for e,c in enumerate(string)])
  if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
