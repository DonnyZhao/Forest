# Utilisez votre nouvelle capacité "cleave" (fendre) aussi souvent que possible.

self.moveXY(23, 23)
loop:
    enemy = self.findNearestEnemy()
    if self.isReady("cleave"):
        # Fendez l'ennemi!
        self.cleave(enemy)
    else:
        # Sinon (si fendre n'est pas prêt), faites une attaques normale.
        self.attack(enemy)
        self.attack(enemy)
