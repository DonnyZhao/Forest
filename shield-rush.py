# Survivez aux deux vagues en vous prot�geant et en fendant vos ennemis.
# Quand "cleave" n'est pas pr�t, utilisez votre talent "shield".$
loop:
    enemy = self.findNearestEnemy()
    if self.isReady("cleave"):
        self.cleave(enemy)
    else:
        self.shield()