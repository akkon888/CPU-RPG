from cpurpg import *

class Dominic(unit):
    charge
    def __init__(self):
        #self, name, level, xp, VIT, STR, INT, DEF, STAM, SPD, VITup, STRup, INTup, DEFup
        super(Dominic, self).__init__(self, "Dominic", 1, 0, 90, 5, 5, 5, 10, 4, 10, 2, 2, 2)
        self.charge = 1
    def focus(self):
        charge += 1
        super(Dominic, self).useSTAM(6)
    def gattle(enemyParty, pos):
        if (pos == 1):
             enemyParty[0].HP -= 50*charge
             enemyParty[1].HP -= 30*charge
             enemyParty[2].HP -= 30*charge
             enemyParty[3].HP -= 30*charge
        else if (pos == 2):
             enemyParty[1].HP -= 50*charge
             enemyParty[2].HP -= 30*charge
             enemyParty[3].HP -= 30*charge
        else
             print "How did this happen to me???? Dom gattle"
        charge = 1
        super(Dominic, self).useSTAM(8)
    def chen(self, userParty):
        for p in userParty:
            p.HP += (50 + self.STR + self.INT)
            if (p.HP > p.VIT):
                p.HP = p.VIT
        self.drainD = 3
        super(Dominic, self).useSTAM(10)
        

class Yong(unit):
    def __init__(self):
        #self, name,  level, xp,VIT,STR,INT,DEF,STAM,SPD,VITup, STRup, INTup, DEFup
        super(Yong, self).__init__(self, "Yongwoon", 1, 0, 150, 10, 6, 0, 10, 5, 30, 3, 1, 0)
    def graniteKick(target):
        target.HP -= (5*self.STR - target.def)
        super(Yong, self).useSTAM(10)
    def bloodTrans(partyList):
        for p in partyList:
            p.STAM += 3
        super(Yong, self).useSTAM(13)
    def bodyTrans(target)
        self.HP -= 50
        target.HP += 5*self.STR
        if(target.HP > target.VIT):
            target.HP = target.VIT


        

    