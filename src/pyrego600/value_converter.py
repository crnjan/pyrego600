def int16ToSevenBitFormat(value: int) -> bytes:
    return bytes([(value & 0xC000) >> 14, (value & 0x3F80) >> 7, value & 0x007F])


def sevenBitFormatToInt16(buffer: bytes, offset: int) -> int:
    value = buffer[offset] << 14 | buffer[offset + 1] << 7 | buffer[offset + 2]
    return value if value & 0x8000 == 0 else -(1 + (~value & 0x7FFF))


def arrayToByte(buffer: bytes, offset: int) -> int:
    return (buffer[offset] << 4 | buffer[offset + 1]) & 0xFF


def stringFromBytes(buffer: bytes, offset: int, charCount: int) -> str:
    return "".join(
        map(
            lambda i: chr(arrayToByte(buffer, i)),
            range(offset, offset + charCount * 2, 2),
        ),
    )
