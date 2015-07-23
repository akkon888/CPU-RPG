--BOOK--

1 - Statistics list
2 - Mechanics
	2.1 - Lingo Glossary
	2.2 - Game Mechanics

--1--

LEVEL - Level of the unit. For scalable units, each level increases VIT, STR, INT and DEF by amounts given
on the card. Levels are gained after the completion of an instance, and thus will not affect combat mid-instance.
After gaining a level, current VIT is increased by gained VIT. All status effects remain.

XP - Experience points of the unit. Killing a unit, in general, should give XP equal to 50 + 25*(LEVEL-1) (index 1).
Experience requirements to gain a level should be 100 + 40*(LEVEL-1) (index 1). XP is gained after the completion
of an instance.

HP - Analogous to current HP. This variable is changed when taking damage or being healed. After falling to 0,
the unit cannot continue to take turns (unless revived). HP is not passively regenerated unless the character
has a specific spell that denotes it.

STR - Primary attribute of physical abilities. All players have an innate attack action which deals STR.
Physical abilties (denoted on cards with RED) are prevented with Bind. Their damage is inherently reduced 
by STR + DEF.

INT - Primary attribute of spells. Spells (denoted on cards with DARK GREY) are prevented with Mute.
Their damage is inherently reduced by INT + DEF.

DEF - Main defensive attribute. Acts as a 1:1 reductant of most damage except pure damage (denoted in WHITE)
and other instances where DEF is specifically ignored.

STAM - Stamina, the cost of using abilities. Most units have a maximum stamina of 10. Stamina is subtracted
for abilities used, as denoted on the card. The amount of stamina gained per turn (with reference to the char)
is equal to the SPD of the character. Stamina cannot be passively or actively (with spells) gained while
afflicted with Drain. Reserve characters gain Stamina every half-cycle (rather than every turn). At the start
of the game, the stamina of all player-controlled characters is set to 5. In order to passively gain stamina
(unless stated otherwise), the character must perform no actions for his/her turn.

MAXSTAM?? - MAXSTAM??

SPD - Speed, The rate at which a character takes his/her turn in a cycle. The current cycle is 60 ticks long.
As an instance progresses, the tick count is increased. A character takes his/her turn when TICK % SPD == 0.
If multiple units take their turn on the same tick, the character with the higher speed goes first; if both have
the same speed, the character with the higher current stamina goes first.

STUN - One of the four main effects. STUN prevents the use of the character for the number of turns (with
reference to the afflicted character) given Stun. It does not prevent passive/active stamina gain, healing, or
buffing of any sort.

DRAIN - One of the four main effects. DRAIN prevents the passive and active (spells) recovery of Stamina. It does
not prevent the use of abilities per se.

BIND - One of the four main effects. BIND prevents the character from using any physical abilities (denoted in
RED). Deactivates channeling physical abilities.

MUTE - One of the four main effects. MUTE prevents the character from using any spells (denoted in DARK GREY).
Deactivates channeling spells.

	If a character is swapped out while affected by buffs/disables, the the remaining duration of all
	disables is doubled while the remaining duration of all buffs is left unchanged. While in reserve
	effect duration time expires at the same rate as that of fielded units.

--2--

2.1 GLOSSARY
	
	Intermediate - The non-combat portion of the game. Here, character statistics can be queried and parties
	can be reformatted. There might be some story or w/e but idk I can't write story that well.

	Instance - The combat portion of the game. Instances last until one side or the other is defeated. No
	retreating is possible. At the end of an instance, all effects are removed unless specifically stated.
	The only attributes that carry between instances are LEVEL, XP, HP, and STAM values.

	Cycle - A progression of 60 ticks within the in-game system. The cycle is used to determine the turn
	order of characters within the game.

	Turn - A tick during a cycle where a character may perform one action (Nicolas may perform 2). In general,
	characters take their turn when TICK % SPD == 0.

	Ally-inflicted - Abilities cast by an allied unit. These abilities typically do not interact with defense
	values. Self-inflicted abilities fall in this category.
	
	Enemy-inflicted - Abilities cast by an enemy unit. Unless otherwise stated these abilities typically
	interact with defense values.

		Healing - Abilities that increase current HP.

		Boosting - Abilities that increase current Stamina.

		Purging - Abilities that remove undesired effects.

		Buff - Ally-inflicted abilities that are not Healing, Purging, or Boosting.

		Damage - Typically Enemy-inflicted abilities that reduce current HP.

		Sapping - Abilities that reduce current Stamina.

		Disabling - Abilities that inflict harmful effects.
	
		Debuff - Typically Enemy-inflicted abilities that are not Damage, Sapping, or Disabling.

Gonna work on this more 7/14/15, if you need clarification on something let me know below this line.



Testy Edits for Testy Individuals












random lel

0,30						2
0,20,40						2
0,15,30,45					2
0,12,24,36,48					4
0,10,20,30,40,50				2
0,6,12,18,24,30,36,42,48,54			4
0,5,10,15,20,25,30,35,40,45,50,55		4
0,4,8,12,16,20,24,28,32,36,40,44,48,52,56	8 = 28

0,4,5,6,8,10,12,15,16,18,20,24,25,28,30,32,35,36,40,42,44,45,48,50,52,54,55,56

2	1,15
3	1,
4
5
6
10
12
15