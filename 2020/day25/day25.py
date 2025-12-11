
filename = "input"
card_pub, door_pub = [int(x) for x in open(filename).read().split("\n")]
print(card_pub, door_pub)
#card_pub, door_pub =5764801, 17807724

divider = 20201227


def get_key(loop, subject, key):
    value = 1
    for _ in range(loop):
        value = value*subject
        value = value % divider

    return value


def solve():

    subject = 7
    keys = []
    for key in [card_pub, door_pub]:
        loop_size = 0
        value = 1

        while True:
            loop_size += 1

            value = value * subject

            value = value % divider

            if value == key:
                keys.append((loop_size, value))
                break

    one = get_key(keys[1][0], keys[0][1], keys[1][1])
    two = get_key(keys[0][0], keys[1][1], keys[0][1])

    assert one == two

    print(f'A: {one}')


if __name__ == "__main__":
    solve()
