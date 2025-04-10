from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Sly2Client import Sly2Context

def update(ctx: 'Sly2Context', ap_connected: bool):
    """Called continuously"""
    pass

def init(ctx: 'Sly2Context'):
    """Called when the player connects to the AP server or enters a new episode"""
    pass