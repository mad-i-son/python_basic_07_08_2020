my_str = 'HELLO my Dear Friends'

for char in reversed(my_str):
    print(char)

iter_obj = my_str.__iter__()
while True:
    try:
        char = next(iter_obj)
    except StopIteration:
        break
    except ValueError:
        continue
    print(char)