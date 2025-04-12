import json
from enum import Enum, IntEnum
from logging import Logger
from typing import Optional, NamedTuple, Tuple
from time import sleep
from math import ceil
import struct

from .pcsx2_interface.pine import Pine
from .data.data import MENU_RETURN_DATA, ADDRESSES, POWERUP_TEXT

class ConnectionState(Enum):
    DISCONNECTED = 0
    IN_GAME = 1
    IN_MENU = 2

class Sly2Episode(IntEnum):
    Title_Screen = 0
    The_Black_Chateau = 1
    A_Starry_Eyed_Encounter = 2
    The_Predator_Awakens = 3
    Jailbreak = 4
    A_Tangled_Web = 5
    He_Who_Tames_the_Iron_Horse = 6
    Menace_from_the_North_Eh = 7
    Anatomy_for_Disaster = 8

class PowerUps(NamedTuple):
    trigger_bomb: bool = False
    size_destabilizer: bool = False
    snooze_bomb: bool = False
    adrenaline_burst: bool = False
    health_extractor: bool = False
    hover_pack: bool = False
    reduction_bomb: bool = False
    temporal_lock: bool = False

    fists_of_flame: bool = False
    turnbuckle_launch: bool = False
    juggernaut_throw: bool = False
    atlas_strength: bool = False
    diablo_fire_slam: bool = False
    berserker_charge: bool = False
    guttural_roar: bool = False
    raging_inferno_flop: bool = False

    smoke_bomb: bool = False
    combat_dodge: bool = False
    stealth_slide: bool = False
    alarm_clock: bool = False
    paraglide: bool = False
    silent_obliteration: bool = False
    thief_reflexes: bool = False
    feral_pounce: bool = False

    mega_jump: bool = False
    tornado_strike: bool = False

    knockout_dive: bool = False
    insanity_strike: bool = False
    voltage_attack: bool = False
    long_toss: bool = False
    rage_bomb: bool = False
    music_box: bool = False
    lightning_spin: bool = False
    shadow_power: bool = False
    tom: bool = False
    time_rush: bool = False

class PCSX2Interface():
    pcsx2_interface: Pine = Pine()
    logger: Logger
    game_id_error: Optional[str] = None
    current_game: Optional[str] = None

    def __init__(self, logger) -> None:
        self.logger = logger

    def _read8(self, address: int):
        return self.pcsx2_interface.read_int8(address)

    def _read16(self, address: int):
        return self.pcsx2_interface.read_int16(address)

    def _read32(self, address: int):
        return self.pcsx2_interface.read_int32(address)

    def _read_bytes(self, address: int, n: int):
        return self.pcsx2_interface.read_bytes(address, n)

    def _read_float(self, address: int):
        return struct.unpack("f",self.pcsx2_interface.read_bytes(address, 4))[0]

    def _write8(self, address: int, value: int):
        self.pcsx2_interface.write_int8(address, value)

    def _write16(self, address: int, value: int):
        self.pcsx2_interface.write_int16(address, value)

    def _write32(self, address: int, value: int):
        self.pcsx2_interface.write_int32(address, value)

    def _write_bytes(self, address: int, value: bytes):
        self.pcsx2_interface.write_bytes(address, value)

    def _collect_all_bottles(self, bottle_flags_address: int):
        self._write32(bottle_flags_address,2**30-1)
        self._write32(0x3E1BF4,30)

    def connect_to_game(self):
        """Initializes the connection to PCSX2 and verifies it is connected to Sly 2"""
        if not self.pcsx2_interface.is_connected():
            self.pcsx2_interface.connect()
            if not self.pcsx2_interface.is_connected():
                return
            self.logger.info("Connected to PCSX2 Emulator")
        try:
            game_id = self.pcsx2_interface.get_game_id()
            # The first read of the address will be null if the client is faster than the emulator
            self.current_game = None
            if game_id in ADDRESSES.keys():
                self.current_game = game_id
                self.addresses = ADDRESSES[game_id]
            if self.current_game is None and self.game_id_error != game_id and game_id != b'\x00\x00\x00\x00\x00\x00':
                self.logger.warning(
                    f"Connected to the wrong game ({game_id})")
                self.game_id_error = game_id
        except RuntimeError:
            pass
        except ConnectionError:
            pass

    def disconnect_from_game(self):
        self.pcsx2_interface.disconnect()
        self.current_game = None
        self.logger.info("Disconnected from PCSX2 Emulator")

    def get_connection_state(self) -> bool:
        try:
            connected = self.pcsx2_interface.is_connected()
            if not connected or self.current_game is None:
                return False
            else:
                return True
        except RuntimeError:
            return False

class Sly2Interface(PCSX2Interface):
    def _read_job_status(self, address: int):
        return self._read32(address+0x54)

    def _write_job_status(self, address: int, status: int):
        self._write32(address+0x54, status)

    def set_items_received(self, n:int) -> None:
        self._write32(self.addresses["items received"], n)

    def read_items_received(self) -> int:
        return self._read32(self.addresses["items received"])

    def is_loading(self) -> bool:
        return self._read32(self.addresses["loading"]) == 2

    def get_current_episode(self) -> Sly2Episode:
        episode_num = self._read32(self.addresses["world id"])
        return Sly2Episode(episode_num)

    def get_current_job(self) -> int:
        return self._read32(self.addresses["job id"])

    def in_safehouse(self) -> bool:
        return (
            self.get_current_episode() != 0 and
            self._read32(self.addresses["camera focus"]) == 0
        )

    def skip_cutscene(self) -> None:
        frame_counter = self._read16(self.addresses["frame counter"])
        pressing_x = self._read8(self.addresses["pressing x"]) == 255

        if frame_counter > 20 and pressing_x:
            self._write32(self.addresses["skip cutscene"],0)

    def to_episode_menu(self) -> None:
        self.logger.info("Skipping to episode menu")
        self._write_bytes(
            self.addresses["reload values"],
            bytes.fromhex(MENU_RETURN_DATA)
        )
        self._write32(self.addresses["reload"], 1)

    def unlock_episodes(self) -> None:
        self._write8(self.addresses["episode unlocks"], 8)

    def set_text(self, text: str|int, replacement: str) -> None:
        if isinstance(text,str):
            text = self.addresses["text"][text][self.get_current_episode()]

        if not isinstance(text,int):
            return

        replacement_string = replacement.encode()+bytes([0])
        self._write_bytes(text,replacement_string)

    def set_thiefnet(self, powerup: int, replacements: Tuple[str,str]) -> None:
        def adjust_length(text: str, target_length: int) -> str:
            if len(text) > target_length:
                if target_length%16 == 0:
                    new_length = target_length+15
                else:
                    new_length = ceil(target_length/16)*16-1
            else:
                new_length = len(text)

            if len(text) > new_length:
                return text[:new_length-2]+".."
            else:
                return text

        powerups = self.addresses["text"]["powerups"][self.get_current_episode()-1]
        addresses = list(powerups.values())[powerup]

        new_gadget_name = adjust_length(
            replacements[0],
            len(list(POWERUP_TEXT.keys())[powerup])
        )
        new_gadget_description = adjust_length(
            replacements[1],
            len(list(POWERUP_TEXT.values())[powerup])
        )

        self.set_text(addresses[0],new_gadget_name)
        self.set_text(addresses[1],new_gadget_description)

    def set_thiefnet_cost(self, powerup: int, cost: int) -> None:
        address = self.addresses["thiefnet costs"][powerup]
        self._write32(address, cost)

    def set_thiefnet_unlock(self) -> None:
        for i in range(24):
            address = self.addresses["thiefnet unlock"][i]
            self._write32(address,1)

    def reset_thiefnet(self) -> None:
        powerups = self.addresses["text"]["powerups"][self.get_current_episode()-1]
        for powerup, addresses in powerups.items():
            self.set_text(addresses[0],powerup)
            self.set_text(addresses[1],POWERUP_TEXT[powerup])

    def set_bottles(self, amount: int) -> None:
        self._write32(self.addresses["bottle count"], amount)

    def add_coins(self, to_add: int):
        current_amount = self._read32(self.addresses["coins"])
        new_amount = current_amount + to_add
        if new_amount < 0:
            new_amount = 0
        self._write32(self.addresses["coins"],new_amount)

    def load_powerups(self, powerups: PowerUps):
        booleans = list(powerups)
        byte_list = [
            [False]*7+[booleans[0]],
            booleans[1:9],
            booleans[9:17],
            booleans[17:25],
            booleans[25:33],
            booleans[33:36]+[False]*5
        ]
        data = b''.join(
            int(''.join(str(int(i)) for i in byte[::-1]),2).to_bytes()
            for byte in byte_list
        )

        self._write_bytes(self.addresses["gadgets"], data)

    def is_infobox(self) -> bool:
        infobox_pointer = self._read32(self.addresses["infobox"])
        return self._read32(infobox_pointer+0x64) == 2

    def set_infobox(self, text: str):
        ep = self.get_current_episode()
        if ep == 0 or self.in_safehouse():
            return

        infobox_pointer = self._read32(self.addresses["infobox"])
        text = " "*10+text
        bytes_string = text.encode()+bytes([0])
        self._write_bytes(self.addresses["infobox text"][ep-1],bytes_string)
        self._write32(self.addresses["infobox string"],1)
        self._write32(infobox_pointer+0x64,2)
        self._write32(self.addresses["infobox scrolling"],2)
        self._write32(self.addresses["infobox duration"],0xffffffff)

    def disable_infobox(self):
        self._write32(self.addresses["infobox"]+0x64,1)

    def kill_player(self):
        if self.in_safehouse() or self.get_current_episode() == 0:
            return

        # Death
        active_character_pointer = self._read32(self.addresses["active character pointer"])
        self._write32(active_character_pointer+0xdf4,8)

def find_text(interface: Sly2Interface, text: str) -> int:
    search_text = text[:12].encode()
    string_table_pointer = interface._read32(interface.addresses["string table"])
    start = interface._read32(string_table_pointer+0x4)
    pointer = start

    for _ in range(5000):
        text_at_pointer = interface._read_bytes(pointer,len(search_text))
        if text_at_pointer == search_text:

            break
        pointer += 0x10

    if pointer == start+0x10*5000:
        print(hex(pointer))
        pointer = 0

    return pointer

if __name__ == "__main__":
    interface = Sly2Interface(Logger("logger"))
    interface.connect_to_game()
    p = PowerUps(*[False for _ in range(35)])

    interface.load_powerups(p)
    interface.set_infobox("Penis "*20)
    # interface.kill_player()

    # for i in range(24):
    #     interface.set_thiefnet(i,(f"Check #{i+1}",f"This is check number {i+1} for thiefnet"))
    #     interface.set_thiefnet_cost(i,(i+1)**3)

    # print(" "*16+"{")
    # for i, (gadget, description) in enumerate(POWERUP_TEXT.items()):
    #     gadget_pointer = find_text(interface, gadget)
    #     description_pointer = find_text(interface, description)
    #     print(" "*20+f"\"{gadget}\": ({hex(gadget_pointer)},{hex(description_pointer)}),")
    # print(" "*16+"},")
