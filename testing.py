from pcsx2_interface.pine import Pine
from time import sleep

hex_string = (
    "8F1B8DAE"+
    "A19F156B"+
    "C9553493"+
    "EA 14 1C B0 9D FA DC 0B D9 67 91 21 2C AA B3 DF F9 A5 0A D0 82 D3 41 35 EC BF 73 F2 38 D1 7C BA C1 06 77 96 BD 97 7E 22 AF 50 88 AE F0 55 34 93 9E 5F 08 6B 89 01 00 00 FF FF FF FF 8F 1B 8D AE A1 9F 15 6B C9 55 34 93 EA 14 1C B0 9D FA DC 0B D9 67 91 21 2C AA B3 DF F9 A5 0A D0 82 D3 41 35 EC BF 73 F2 38 D1 7C BA C1 06 77 96 BD 97 7E 22 AF 50 88 AE F0 55 34 93 9E 5F 08 6B"
)

full_bytes = bytes.fromhex(hex_string)

p = Pine()
p.connect()
if not p.is_connected:
    print("Not connected")
    exit()

# while True:
#     world_id = p.read_int32(0x3D4A60)
#     job_id = p.read_int32(0x2DEB44)

#     if world_id == 0 and job_id == 1583:
#         p.write_bytes(0x3E1088, full_bytes)
#         p.write_int32(0x3E1080, 1)
#         sleep(1)
#         print("Skipped intro!")
#         sleep(5)
#         p.write_int8(0x5975E8, 8)
#         break

#     sleep(0.1)

replacement = b"Jonathan's Right Mothwing Cloak"+bytes([0])
old_text = p.read_bytes(0x4CB9B0,len(replacement))

p.write_bytes(0x4cdcbd,b"check."+bytes([0]))

while True:
    frame_counter = p.read_int16(0x2F67D0)
    pressing_x = p.read_int8(0x2DFC0E) == 255

    if frame_counter > 20 and pressing_x:
        p.write_int32(0x2F6810,0)

    shopping = p.read_int32(0x2DE258) == 0


    if shopping:
        p.write_bytes(0x3D4AF8,bytes.fromhex("000000000000"))
        p.write_bytes(0x4Cb960,b"Check No. 1 ")
        p.write_bytes(0x4CB9B0,replacement)
    else:
        p.write_bytes(0x3D4AF8,bytes.fromhex("FFFFFFFFFFFF"))
        p.write_bytes(0x4Cb960,b"Trigger Bomb")
        p.write_bytes(0x4CB9B0,old_text)

    sleep(0.1)