# You'll need great equipment and strategy to win.

loop:
    enemy = self.findNearestEnemy()
    flag = self.findFlag()
    if flag:
        self.pickUpFlag(flag)
    elif enemy:
        if self.isReady("cleave"):
            self.cleave(enemy)
        else:
            self.shield()
            self.attack(enemy)
            self.attack(enemy)
        
