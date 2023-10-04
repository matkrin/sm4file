from io import BufferedReader
import struct


class Cursor:
    def __init__(self, buffer: BufferedReader):
        self._buffer = buffer

    def set_position(self, position):
        self._buffer.seek(position)

    def skip(self, bytes_to_skip):
        self.set_position(self._buffer.tell() + bytes_to_skip)

    def read(self, num_bytes) -> bytes:
        return self._buffer.read(num_bytes)

    def read_string(self, str_len: int) -> str:
        """Read bytes as string from _bytes with str_len"""
        return "".join([chr(i) for i in self._buffer.read(str_len)])

    def read_sm4_string(self) -> str:
        length = self.read_u16_le()
        return self.read_string(length)

    def read_u8_le(self) -> int:
        return struct.unpack("<B", self._buffer.read(1))[0]

    def read_u16_le(self) -> int:
        return struct.unpack("<H", self._buffer.read(2))[0]

    def read_i16_le(self) -> int:
        return struct.unpack("<h", self._buffer.read(2))[0]

    def read_u32_le(self) -> int:
        return struct.unpack("<I", self._buffer.read(4))[0]

    def read_i32_le(self) -> int:
        return struct.unpack("<i", self._buffer.read(4))[0]

    def read_u64_le(self) -> int:
        return struct.unpack("<q", self._buffer.read(8))[0]

    def read_f32_le(self) -> int:
        return struct.unpack("<f", self._buffer.read(4))[0]

    def read_f64_le(self) -> int:
        return struct.unpack("<d", self._buffer.read(8))[0]
