from random import SystemRandom

sec_rand = SystemRandom()
seed = sec_rand.randint(0, 19576)
mult = 10357
inc = 283
mod = 19577


def random_int(lim: int):
    global seed
    seed += inc
    seed = (seed * mult) % mod

    return seed % lim


def set_seed(new):
    global seed
    seed = hash(new) % mod


if __name__ == "__main__":
    set_seed(1)
    for i in range(23):
        print(random_int(10))
