# Restez au mileu et prot�ge!

loop:
    enemy = self.findNearestEnemy()
    if enemy:
        self.attack(enemy)
        self.attack(enemy)
    else:
        # ...soit reculez jusqu'� votre position de defense.
        self.moveXY(40, 33)