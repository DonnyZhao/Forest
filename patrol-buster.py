# Remember that enemies may not yet exist.
loop:
    enemy = self.findNearestEnemy()
    # If there is an enemy, attack it!
    if enemy:
        self.attack(enemy)
        self.attack(enemy)