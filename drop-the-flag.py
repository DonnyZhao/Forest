# Put flags where you want to build traps.
# When you're not building traps, pick up coins!

loop:
    flag = self.findFlag()
    if flag:
        # How do we get fx and fy from the flag's pos?
        loc = flag.pos
        fx = loc.x
        fy = loc.y
        
        self.buildXY("fire-trap", fx, fy)
        self.pickUpFlag(flag)
    else:
        item = self.findNearestItem()
        if item:
            pos = item.pos
            itemX = pos.x
            itemY = pos.y
            self.moveXY(itemX, itemY)