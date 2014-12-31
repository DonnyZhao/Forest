# Si les ogres vous foncent dessus, fendez les!
# Si ils restent a 10 mètres d'écart, attaquez le coffre
loop:
    enemy = self.findNearestEnemy()
    dist = self.distanceTo(enemy)
    if dist >10:
        self.attack("Chest")
    else:
        if self.isReady("cleave"):
            self.cleave(enemy)
        else:
            self.shield()
            self.attack(enemy)