"""Extract the two expected files from Septabee's ABI-8 SBRT container."""

import pathlib
import struct
import sys
import zlib


def extract(source, destination):
    data = pathlib.Path(source).read_bytes()
    if data[:16] != b"SBRT0001" + struct.pack("<II", 8, 2):
        raise ValueError("Expected an ABI-8 SBRT container with two files")
    expected = {"runtime-release", "libseptabee-jit-runtime.so"}
    files = {}
    offset = 16
    for _ in range(2):
        flags, name_size, crc, size, packed_size = struct.unpack_from("<BHIQQ", data, offset)
        offset += 23
        name = data[offset:offset + name_size].decode("utf-8")
        offset += name_size
        if flags != 0 or name not in expected or name in files:
            raise ValueError("Unexpected runtime entry")
        if offset + packed_size > len(data) or size > 128 * 1024 * 1024:
            raise ValueError("Invalid runtime entry size")
        payload = zlib.decompress(data[offset:offset + packed_size])
        offset += packed_size
        if len(payload) != size or zlib.crc32(payload) != crc:
            raise ValueError("Runtime entry checksum or size mismatch")
        files[name] = payload
    if offset != len(data) or files.keys() != expected:
        raise ValueError("Unexpected runtime container contents")
    if not files["libseptabee-jit-runtime.so"].startswith(b"\x7fELF"):
        raise ValueError("Runtime library is not ELF")
    if files["runtime-release"] != b"2\n":
        raise ValueError("Expected runtime release 2")
    out = pathlib.Path(destination)
    out.mkdir(parents=True, exist_ok=True)
    for name, payload in files.items():
        (out / name).write_bytes(payload)


if __name__ == "__main__":
    extract(*sys.argv[1:])
