from pcsx2_interface.pine import Pine
from time import sleep

hex_string = "8F 1B 8D AE A1 9F 15 6B C9 55 34 93 EA 14 1C B0 9D FA DC 0B D9 67 91 21 2C AA B3 DF F9 A5 0A D0 82 D3 41 35 EC BF 73 F2 38 D1 7C BA C1 06 77 96 BD 97 7E 22 AF 50 88 AE F0 55 34 93 9E 5F 08 6B 89 01 00 00 FF FF FF FF 8F 1B 8D AE A1 9F 15 6B C9 55 34 93 EA 14 1C B0 9D FA DC 0B D9 67 91 21 2C AA B3 DF F9 A5 0A D0 82 D3 41 35 EC BF 73 F2 38 D1 7C BA C1 06 77 96 BD 97 7E 22 AF 50 88 AE F0 55 34 93 9E 5F 08 6B"

full_bytes = bytes.fromhex(hex_string)

p = Pine()
p.connect()
if not p.is_connected:
    print("Not connected")
    exit()

while True:
    world_id = p.read_int32(0x3D4A60)
    job_id = p.read_int32(0x2DEB44)

    if world_id == 0 and job_id == 1583:
        p.write_bytes(0x3E1088, full_bytes)
        p.write_int32(0x3E1080, 1)
        sleep(1)
        print("Skipped intro!")
        sleep(5)
        p.write_int8(0x5975E8, 8)
        break

    sleep(0.1)