from dino_runner.components.powerup.powerup import PowerUp
from dino_runner.utils.constants import SHIELD, SHIELD_TYPE

class Shield(PowerUp):
    def __init__(self):
        self.image = SHIELD
        self.type = SHIELD_TYPE
        super(Shield, self).__init__(self.image, self.type)
        