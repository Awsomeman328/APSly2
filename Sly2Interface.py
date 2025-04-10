import json
from enum import Enum, IntEnum
from logging import Logger
from typing import Optional

from .pcsx2_interface.pine import Pine

_ADDRESSES = {
    "SCUS-97316": {
        "loading": 0x3D3980,
        "world id": 0x3D4A60,
        "coins": 0x3D4B00,
        "jobs": {
            "e1": [[],],
            "e4": [[0xb2ec90,0xb34d30,],],
        },
        "bottle flags": {
            "e4": 0x3D5020
        },
        "bottle count": 0x3E1BF4,
    },
}

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

class PCSX2Interface():
    pcsx2_interface: Pine = Pine()
    logger: Logger
    game_id_error: Optional[str] = None
    current_game: Optional[str] = None

    def __init__(self, logger) -> None:
        self.logger = logger

    def _read32(self, address: int):
        return self.pcsx2_interface.read_int32(address)

    def _write32(self, address: int, value: int):
        self.pcsx2_interface.write_int32(address, value)

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
            if game_id in _ADDRESSES.keys():
                self.current_game = game_id
                self.addresses = _ADDRESSES[game_id]
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

    def is_loading(self) -> bool:
        return self._read32(self.addresses["loading"]) == 2

    def get_current_episode(self) -> Sly2Episode:
        episode_num = self._read32(self.addresses["world id"])
        return Sly2Episode(episode_num)

    def add_coins(self, to_add: int):
        current_amount = self._read32(self.addresses["coins"])
        new_amount = current_amount + to_add
        if new_amount < 0:
            new_amount = 0
        self._write32(self.addresses["coins"],new_amount)
