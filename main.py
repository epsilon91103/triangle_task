import math

LIMIT = 100_000_000


def incenter(limit):
    cnt = 0
    for m in range(1, math.ceil(limit**.5)):
        for n in range(m % 2 + 1, m, 2):
            if math.gcd(m, n) == 1:
                b, d = m*m-n*n, 2*m*n
                sum_ = b+d
                if sum_ >= limit:
                    break
                cnt += 2*int(limit/sum_)
    return cnt


def parallel(limit):
    cnt = 0
    for m in range(1, math.ceil((limit/2)**.5), 2):
        for n in range(1, limit):
            if math.gcd(m, n) == 1:
                g, a = 2*m*n, m*m+2*n*n
                sum_ = (g+a)*2
                if sum_ > limit:
                    break
                cnt += int((limit-1)/sum_)
    return cnt


def main():
    incenter_cnt = incenter(LIMIT)
    parallel_cnt = parallel(LIMIT)

    return incenter_cnt + parallel_cnt


if __name__ == '__main__':
    answer = main()
    print(answer)
