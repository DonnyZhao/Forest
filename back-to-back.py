# Restez au mileu et protége!

loop:
    enemy = self.findNearestEnemy()
    if enemy:
        self.attack(enemy)
        self.attack(enemy)
    else:
        # ...soit reculez jusqu'à votre position de defense.
        self.moveXY(40, 33)