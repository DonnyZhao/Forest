# Utilisez votre nouvelle capacit� "cleave" (fendre) aussi souvent que possible.

self.moveXY(23, 23)
loop:
    enemy = self.findNearestEnemy()
    if self.isReady("cleave"):
        # Fendez l'ennemi!
        self.cleave(enemy)
    else:
        # Sinon (si fendre n'est pas pr�t), faites une attaques normale.
        self.attack(enemy)
        self.attack(enemy)
