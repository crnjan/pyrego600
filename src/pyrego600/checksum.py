from functools import reduce


def checksum(buffer: bytes) -> int:
    return reduce(lambda i, j: i ^ j, buffer)
