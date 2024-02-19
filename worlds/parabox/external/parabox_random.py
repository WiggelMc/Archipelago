BITMASK_32 = (1 << 32) - 1


class ParaboxRandom:
    x: int
    y: int
    z: int
    w: int

    @staticmethod
    def _gen_init_num(seed: int):
        state = seed & BITMASK_32

        def gen():
            nonlocal state
            result = state = (state + 0x9971f3DC) & BITMASK_32
            result = ((result ^ (result >> 14)) * 0xD7185219) & BITMASK_32
            result = ((result ^ (result >> 10)) * 0xCF4bED29) & BITMASK_32
            return (result ^ (result >> 15)) & BITMASK_32

        return gen

    def __init__(self, seed: int):
        g = ParaboxRandom._gen_init_num(seed)
        self.x = g()
        self.y = g()
        self.z = g()
        self.w = g()

    def next(self, start: int = 0, end: int = BITMASK_32) -> int:
        t = self.x ^ ((self.x << 13) & BITMASK_32)
        self.x, self.y, self.z = self.y, self.z, self.w
        result = self.w = (self.w ^ (self.w >> 7)) ^ (t ^ (t >> 6))

        start = max(0, min(start, BITMASK_32))
        end = max(start, min(end, BITMASK_32))
        return start + result % (end + 1 - start)


def main():
    r = ParaboxRandom(0xFFFFFAEE)
    x = ""
    for i in range(10000):
        v = r.next()
        print(format(v, '#034b'))
        x += format(v, '#034b')[2:]
    print(x)


if __name__ == '__main__':
    main()
