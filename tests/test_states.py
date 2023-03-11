

import click

import __init__
from emulator import Emulator, PauseState, PartyState, PackState
from helpers import test_util
from helpers.log import get_logger, mod_fname
logger = get_logger(mod_fname(__file__))

from tests.__init__ import TEST_IMG_DIR

MODULE = "emulator.py"
EMULATOR = Emulator()

EMULATOR.launch_game()
EMULATOR.continue_pokemon_game()

def test_1_id_pause_state():
    logger.info("Test 1 - ID Pause Menu")
    logger.info(f"Start Menu is {EMULATOR.state.is_pause_menu_open()}")
    logger.info(f"Beginning Pause State: {EMULATOR.state.pause_menu}")
    EMULATOR.navigate_menu(PauseState.OPTION)
    logger.info(f"Current Pause State: {EMULATOR.state.pause_menu}")
    EMULATOR.navigate_menu(PauseState.PACK)
    logger.info(f"Current Pause State: {EMULATOR.state.pause_menu}")
    assert(EMULATOR.state.pause_menu == PauseState.PACK)
    EMULATOR.press_b()
    EMULATOR.state.pause_menu_off()
    EMULATOR.state.pause_menu = PauseState.POKEDEX
    logger.info(f"Test 1 - Success")

def test_2_id_pokemon():
    logger.info("Test 2 - ID Pokemon in Party")
    logger.info(f"Beginning Pause State: {EMULATOR.state.party_menu}")
    EMULATOR.navigate_party(PartyState.SLOT_4)
    logger.info(f"Current Pause State: {EMULATOR.state.party_menu}")
    assert(EMULATOR.state.party_menu == PartyState.SLOT_4)
    EMULATOR.press_b()
    EMULATOR.state.party_menu_off()
    logger.info("Test 2 - Success")

def test_3_id_pack():
    logger.info("Test 3 - ID Pack Pockets")
    logger.info(f"Beginning Pack Item: {EMULATOR.state.pack_menu}")
    EMULATOR.navigate_pack(PackState.KEY_ITEMS)
    logger.info(f"Current Pack Pocket: {EMULATOR.state.pack_menu}")
    assert(EMULATOR.state.pack_menu == PackState.KEY_ITEMS)
    EMULATOR.press_b()
    EMULATOR.state.pack_menu_off()
    logger.info("Test 3 - Success")

@click.command()
def run_tests():
    logger.info(f"----- Testing {MODULE} -----")
    


    # each test is dependent on controller presses from
    # previous test so required to always run all tests in this test
    test_util.run_tests(module_name=__name__)
    
    logger.info("----- All tests pass! -----")


if __name__ == "__main__":
    run_tests()