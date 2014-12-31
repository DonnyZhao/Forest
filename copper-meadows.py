# Ramassez toutes les pièces dans chaque prairie.
# Utilisez les drapeaux pour vous déplacer entre les prairies.
# Appuyez sur Envoyer quand vous êtes prêt à placer les drapeaux.

loop:
    flag = self.findFlag()
    if flag:
        # Pick up the flag.
        greenFlag = self.findFlag("green")
        self.pickUpFlag(greenFlag)
    else:
        # Automatically move to the nearest item you see.
        item = self.findNearestItem()
        if item:
            position = item.pos
            x = position.x
            y = position.y
            self.moveXY(x, y)