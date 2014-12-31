# S'il y a un enemi, attaquez-le.
# Sinon, attaquez le coffre !

loop:
    # Utilisez if/else.
    enemy = self.findNearestEnemy()
    if not enemy:
        self.attack("Chest")
    else:
        self.attack(enemy)
        self.attack(enemy)