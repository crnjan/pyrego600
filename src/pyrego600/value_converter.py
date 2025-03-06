def int16_to_seven_bit_format(value: int) -> bytes:
    return bytes([(value & 0xC000) >> 14, (value & 0x3F80) >> 7, value & 0x007F])


def seven_bit_format_to_int16(buffer: bytes, offset: int) -> int:
    value = buffer[offset] << 14 | buffer[offset + 1] << 7 | buffer[offset + 2]
    return value if value & 0x8000 == 0 else -(1 + (~value & 0x7FFF))


def array_to_byte(buffer: bytes, offset: int) -> int:
    return (buffer[offset] << 4 | buffer[offset + 1]) & 0xFF


def string_from_bytes(buffer: bytes, offset: int, charCount: int) -> str:
    return "".join(
        map(
            lambda i: chr(array_to_byte(buffer, i)),
            range(offset, offset + charCount * 2, 2),
        ),
    )
