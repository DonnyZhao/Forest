# Survivez aux deux vagues en vous protégeant et en fendant vos ennemis.
# Quand "cleave" n'est pas prêt, utilisez votre talent "shield".$
loop:
    enemy = self.findNearestEnemy()
    if self.isReady("cleave"):
        self.cleave(enemy)
    else:
        self.shield()