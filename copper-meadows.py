# Ramassez toutes les pi�ces dans chaque prairie.
# Utilisez les drapeaux pour vous d�placer entre les prairies.
# Appuyez sur Envoyer quand vous �tes pr�t � placer les drapeaux.

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