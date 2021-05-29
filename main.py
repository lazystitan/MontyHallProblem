import random

REWARD = 1
NOTHING = 0
TOTALROUND = 100000


class Guess:

    def __init__(self):
        self.boxs = [NOTHING, NOTHING, NOTHING]
        self.nothing_box = -1
        self.guess_box = -1
        reward_position = random.randint(0, 2)
        self.boxs[reward_position] = REWARD

    def open_a_nothing(self):
        for i, box in enumerate(self.boxs):
            if box == NOTHING and i != self.guess_box:
                self.nothing_box = i
                break

    def first_guess(self):
        self.guess_box = random.randint(0, 2)

    def is_reward(self):
        return self.boxs[self.guess_box] == REWARD

    def change_box(self):
        for i, box in enumerate(self.boxs):
            if i != self.guess_box and i != self.nothing_box:
                self.guess_box = i
                break

    def re_guess(self):
        new_guess_box = random.randint(0, 1)
        for i, box in enumerate(self.boxs):
            if new_guess_box == 0 and i != self.nothing_box:
                self.guess_box = i
                break
            if self.nothing_box != i:
                new_guess_box = new_guess_box - 1

def sim():
    first_guess_group = [Guess() for _ in range(0, TOTALROUND)]
    change_box_group = [Guess() for _ in range(0, TOTALROUND)]
    re_guess_group = [Guess() for _ in range(0, TOTALROUND)]

    first_guess_group_reward_ct = 0
    change_box_group_reward_ct = 0
    re_guess_group_reward_ct = 0

    for g in first_guess_group:
        g.first_guess()
        if g.is_reward():
            first_guess_group_reward_ct = first_guess_group_reward_ct + 1

    print(first_guess_group_reward_ct / TOTALROUND)

    for g in change_box_group:
        g.first_guess()
        g.open_a_nothing()
        g.change_box()
        if g.is_reward():
            change_box_group_reward_ct = change_box_group_reward_ct + 1

    print(change_box_group_reward_ct / TOTALROUND)

    for g in re_guess_group:
        g.first_guess()
        g.open_a_nothing()
        g.re_guess()
        if g.is_reward():
            re_guess_group_reward_ct = re_guess_group_reward_ct + 1

    print(re_guess_group_reward_ct / TOTALROUND)

def test1():
    g = Guess()
    g.first_guess()
    g.open_a_nothing()
    g.change_box()
    print(g.is_reward())

if __name__ == '__main__':
    # test1()
    sim()
