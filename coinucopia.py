loop:
    flag = self.findFlag()
    if flag:
        self.pickUpFlag(flag)
    else:
        self.say("Placez un drapeau pour que je m'y rende.")