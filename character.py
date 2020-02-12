from proficiencies import Score

class Character:
    """
    A class for building a D&D character
    """
    def __init__(self, str, dex, con, int, wis, char, race, class):
        """
        creates the base character incorporating class and race
        Args:
            str (integer): The characters strength score
            dex (integer): The characters dexterity score
            con (integer): The characters constitution score
            int (integer): The characters intelligence score
            wis (integer): The characters wisdom score
            char (integer): The characters charisma score
            race (string): The characters race
            class (string): The charaters class
        """
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.char = char
        self.race = race
        self.class = class
        self.dragon_type = None
        self.lvl = 1
        self.prof_bonus = 0
        self.speed = 0
        self.age = 0
        self.height = 0
        self.weight = 0
        self.hp_mod = 0
        self.traits = []
        self.languages = []
        self.set_age()
        self.set_height()
        self.set_weight()
        self.set_race()

        # intialize saves amd skills
        self.str_save = Score(self.str, self.prof_bonus)
        self.dex_save = Score(self.dex, self.prof_bonus)
        self.con_save = Score(self.con, self.prof_bonus)
        self.int_save = Score(self.int, self.prof_bonus)
        self.wis_save = Score(self.wis, self.prof_bonus)
        self.char_save = Score(self.char, self.prof_bonus)
        self.acrobatics = Score(self.dex, self.prof_bonus)
        self.animal_handling = Score(self.wis, self.prof_bonus)
        self.arcana = Score(self.int, self.prof_bonus)
        self.athletics = Score(self.str, self.prof_bonus)
        self.deception = Score(self.char, self.prof_bonus)
        self.history = Score(self.int, self.prof_bonus)
        self.insight = Score(self.wis, self.prof_bonus)
        self.intimidation = Score(self.char, self.prof_bonus)
        self.investigation = Score(self.int, self.prof_bonus)
        self.medicine = Score(self.wis, self.prof_bonus)
        self.nature = Score(self.int, self.prof_bonus)
        self.perception = Score(self.wis, self.prof_bonus)
        self.performance = Score(self.char, self.prof_bonus)
        self.persuasion = Score(self.char, self.prof_bonus)
        self.religion = Score(self.int, self.prof_bonus)
        self.sleight_of_hand = Score(self.dex, self.prof_bonus)
        self.stealth = Score(self.dex, self.prof_bonus)
        self.Survival = Score(self.wis, self.prof_bonus)

        self.passive_perc = 10 + (self.wis//2)-5 + self.prof_bonus



    def set_race(self):
        if self.race.lower() == "hill dwarf":
            self.con += 2
            self.wis += 1
            self.hp_mod = 1
            self.speed = 25
            self.teraites.append("Dwarven Resilience: You have advantage on saving throws against poison, and you have resistance against poison damage")
            self.traits.append("Darkvision: You can see in dim light within 60 feet (cannot discern color in darkness, only shades of gray)")
            self.traits.append("Proficient in history checks on the origin of stonework add double proficiency bonus")
            self.languages.append("Common")
            self.languages.append("Dwarvish")
            print("You gain proficiency with the artisan's tools of your choice: smith's tools (0), brewer's supplies (1), or mason's tools (2). Which one would you like?")
            tool_prof = input()
            if tool_prof == 0:
                self.traits.append("Proficient in smith's tools")
            elif tool_prof == 1:
                self.traits.append("Proficient in brewer's supplies")
            else:
                self.traits.append("Proficient in mason's tools")
        elif self.race.lower() == "mountain dwarf":
            self.con += 2
            self.str += 2
            self.speed = 25
            self.traits.append("Advantage on poison saving throws")
            self.traits.append("Resistant to poison damage")
            self.traits.append("Darkvision: You can see in dim light within 60 feet (cannot discern color in darkness, only shades of gray)")
            self.traits.append("Proficient in history checks on the origin of stonework add double proficiency bonus")
            self.languages.append("Common")
            self.languages.append("Dwarvish")
            print("You gain proficiency with the artisan's tools of your choice: smith's tools (0), brewer's supplies (1), or mason's tools (2). Which one would you like?")
            tool_prof = input()
            if tool_prof == 0:
                self.traits.append("Proficient in smith's tools")
            elif tool_prof == 1:
                self.traits.append("Proficient in brewer's supplies")
            else:
                self.traits.append("Proficient in mason's tools")
        elif self.race.lower() == "high elf":
            self.dex += 2
            self.int += 1
            self.speed = 30
            self.perception.update_proficiency(True)
            self.traits.append("Advantage on saving throws against being charmed")
            self.traits.append("Magic can't put you to sleep")
            self.traits.append("Darkvision: You can see in dim light within 60 feet (cannot discern color in darkness, only shades of gray)")
            self.languages.append("common")
            self.languages.append("Elvish")
            ### ADD CANTRIP ABILITIES ###
            ### ADD LANGUAGE LIST TO CHOOSE FROM ####
        elif self.race.lower() == "wood elf":
            self.dex += 2
            self.wis += 1
            self.speed = 35
            self.perception.update_proficiency(True)
            self.traits.append("Advantage on saving throws against being charmed")
            self.traits.append("Magic can't put you to sleep")
            self.traits.append("Darkvision: You can see in dim light within 60 feet (cannot discern color in darkness, only shades of gray)")
            self.traits.append("You can attempt to hid even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena")
            self.languages.append("common")
            self.languages.append("Elvish")

        elif self.race.lower() == "drow":
            self.dex += 2
            self.char += 1
            self.speed = 30
            self.perception.update_proficiency(True)
            self.traits.append("Advantage on saving throws against being charmed")
            self.traits.append("Magic can't put you to sleep")
            self.traits.append("Darkvision: You can see in dim light within 120 feet (cannot discern color in darkness, only shades of gray)")
            self.traits.append("Sunlight Sensativity: You have disadvantage on attack rolls and on Wisdom checks that rely on sight when you, the target of your attack, or whatever you are trying to percieve is in direct sunlight")
            self.languages.append("common")
            self.languages.append("Elvish")
            ### ADD CANTRIB ABILITIES ###

        elif self.race.lower() == "lightfoot halfling":
            self.dex += 2
            self.char += 1
            self.speed = 25
            self.traits.apepnd("Lucky: When you roll a 1 on an attack roll, ability check, or saving throw you can reroll the die and must use the new roll")
            self.traits.append("Brave: You have advantage on saving throws against being frightened")
            self.traits.append("Halfling Nimbleness: You can move through the space of any creatue that is of a size larger than yours")
            self.traits.append("Naturally Stealthy: You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you")
            self.languages.append("Common")
            self.languages.append("Halfling")

        elif self.race.lower() == "stout halfling":
            self.dex += 2
            self.con += 1
            self.speed = 25
            self.traits.apepnd("Lucky: When you roll a 1 on an attack roll, ability check, or saving throw you can reroll the die and must use the new roll")
            self.traits.append("Brave: You have advantage on saving throws against being frightened")
            self.traits.append("Halfling Nimbleness: You can move through the space of any creatue that is of a size larger than yours")
            self.traits.append("Stout Resiliance: You have advantage on saving throws against poision, and you have resistance against poison damage")
            self.languages.append("Common")
            self.languages.append("Halfling")

        elif self.race.lower() == "human":
            self.str += 1
            self.dex += 1
            self.con += 1
            self.int += 1
            self.wis += 1
            self.char += 1
            self.speed = 30
            self.languages.append("Common")
            ### ADD LANGUAGE LIST TO CHOOSE FROM ####

        elif self.race.lower() == "dragonborn":
            self.str += 2
            self.char += 1
            self.speed = 30
            print("You have draconic acenstry. Choose one type of dragon. Your breath weapon and resistance are determined by the dragon type")
            print("Black, Blue, Brass, Bronze, Copper, Gold, Green, Red, Silver, White")
            self.dragon_type = input()
            if self.dragon_type == "Back" or "Copper":
                self.traits.append("Breath Weapon: Acid. 5 by 30 ft line (Dex. save)")
                self.traits.append("Damage Resistance: Acid")
            elif self.dragon_type == "Blue" or "Bronze":
                self.traits.append("Breath Weapon. Lighting. 5 by 30 ft. line (Dex. save)")
                self.traits.append("Damage Resistance: Lighting")
            elif self.dragon_type == "Brass":
                self.traits.append("Breath Weapon: Fire. 5 by 30 ft. line (Dex. save)")
                self.traits.append("Damage Resistance: Fire")
            elif self.dragon_type == "Gold" or "Red":
                self.traits.append("Breath Weapon: Fire. 15 ft. cone (Dex. save)")
                self.traits.append("Damage Resistance: Fire")
            elif self.dragon_type == "Poison":
                self.traits.append("Breath Weapon: Poison. 15 ft. cone (Con. save)")
                self.traits.append("Damage Resistance: Poison")
            elif self.dragon_type == "Silver" or "White":
                self.traits.append("Breath Weapon: Cold. 15 ft. cone (Con. save)")
                self.traits.append("Damage Resistance: Cold")
            self.languages.append("Common")
            self.languages.append("Draconic")

        elif self.race.lower() == "forest gnome":
            self.int += 2
            self.dex += 1
            self.speed = 25
            self.traits.append("Darkvision: You can see dim light within 50 ft as if it were bright light and darkness as if it were dim light. You can't discern color in darkness, only shades of gray")
            self.traits.append("Gnome Cunning: You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic")
            self.languages.append("Common")
            self.languages.append("Gnomish")
            ### ADD CANTRIP ABILITIES ###
            self.traits.append("Speak with Small Beasts: Through sounds and gestures, you can communicate simple ideas with Small or smaller beasts.")
        elif self.race.lower() == "rock gnome":
            self.int += 2
            self.con += 1
            self.speed = 25
            self.traits.append("Darkvision: You can see dim light within 50 ft as if it were bright light and darkness as if it were dim light. You can't discern color in darkness, only shades of gray")
            self.traits.append("Gnome Cunning: You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic")
            self.languages.append("Common")
            self.languages.append("Gnomish")
            self.traits.append("Artificer's Lore: Whenever you make an Intelligence (History) check related to magic items, alchemical objects, or technological devices, you can add twice your proficiency bonus.")
            self.traits.append("Tinker: You have proficiency with artisan's tools (tinker's tool). Using those tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clockword device (AC 5, 1 hp). \
            The device ceases to functiona fter 24 hours (unless you spend 1 hour repairing it to keep the device functioning), or when you use your action to dismantle it; at that time, you can reclaim the materials used \
            to create it. You can have up to three such devices active at a time")

        elif self.race.lower() == "half-elf":
            self.char += 2
            valid_choice = False
            while not valid_choice:
                print("what ability score would you like to increase by 1? str, dex, con, int, wis, char")
                stat_inc = input()
                if stat_inc == "str":
                    self.str += 1
                    valid_choice = True
                elif stat_inc == "dex":
                    self.dex += 1
                    valid_choice = True
                elif stat_inc == "con":
                    self.con += 1
                    valid_choice = True
                elif stat_inc == "int":
                    self.int += 1
                    valid_choice = True
                elif stat_inc == "wis":
                    self.wis += 1
                    valid_choice = True
                elif stat_inc == "char":
                    self.char += 1
                    valid_choice = True
                else:
                    valid_choice = False
            self.speed = 30
            self.traits.append("Darkvision: Thanks to your elf blood, you have superior vision in dark and dim comditions. You can see in dim light within 60 feet of you as if it were bright light. You can't discern color in darkness, only shades of gray.")
            self.traits.append("Fey Ancestry: You have advantage on saving throws against being charmed, and magic can't put you to sleep")
            ### GAIN PROFICIENCY IN TWO SKILLS SET UP DROP DOWN FOR THIS ####
            self.languages.append("Common")
            self.languages.append("Elvish")
            ### ADD LANGUAGES TABLE ###

        elif self.race.lower() == "half-orc":
            self.str += 2
            self.con += 1
            self.speed = 30
            self.traits.append("Darkvision: Thanks to your orc blood, you have superior vision in dark and dim comditions. You can see in dim light within 60 feet of you as if it were bright light. You can't discern color in darkness, only shades of gray.")
            self.intimidation.update_proficiency(True)
            self.traits.append("Relentless Endurance: When you are reduced to 0 hit pooints but not killed outright, you can drop to 1 hit point instead. You can't use this feature again utnil you finish a a long rest.")
            self.traits.append("Savage Attacks: When you score a critical hit with a melee weapon attack, you can roll one of the weapon's damage dice one additional time and add it to the extra damage of the critical hit.")
            self.languages.append("Common")
            self.languages.append("Orc")

        elif self.race.lower() == "tiefling":
            self.int += 1
            self.char += 2
            self.speed = 30
            self.traits.append("Darkvision: Thanks to your infernal heritage, you have superior vision in dark and dim comditions. You can see in dim light within 60 feet of you as if it were bright light. You can't discern color in darkness, only shades of gray.")
            self.traits.append("Hellish Resistance: You have resistance to fire damage")
            ### ADD CANTRIP ABILITIES###
            self.languages.append("Common")
            self.languages.append("Infernal")

    def set_age(self):
        if self.race.lower() == "hill dwarf" or "mountain dwarf":
            print("Dwarves mature at the same rate as humans, but they're considered young until they reach the age of 50. On Average, they live about 350 years. What is your age?")
        elif self.race.lower() == "high elf" or "wood elf" or "drow":
            print("A typical elf claims adulthood and an adult name around the age of 100 and can live to be 750 years old. What is your age?")
        elif self.race.lower() == "lightfoot halfling" or "stout halfling":
            print("A halfling reaches adulthood at age of 20 and generally lives into the middle of his or her second century. What is your age?")
        elif self.race.lower() == "human":
            print("Humans reach adulthood in their late teens and live less than a century. What is your age?")
        elif self.race.lower() == "dragonborn":
            print("Dragonborn reach adulthood by 15. They live to be around 80. What is your age?")
        elif self.race.lower() == "rock gnome" or "forest gnome":
            print("Gnomes reach adulthood by about 40 and can live 350 to almost 500 years. What is your age?")
        elif self.race.lower() == "half-elf":
            print("Half-Elves mature at the same rate as humans do and reach adulthood around the age of 20. They live much longer than humans, however, often exceeding 180 years. What is your age?")
        elif self.race.lower() == "half-orc":
            print("Half-orcs mature a little faster than humans, reaching adulthood around age 14. They age noticeably faster and rarely live longer than 75 years. What is your age?")
        elif self.race.lower() == "tiefling":
            print("Tieflings mature at the same rate as humans, reaching adulthood around the age of 20. They live a little longer than humans. What is your age?")

    def set_height(self):
        if self.race.lower() == "hill dwarf" or "mountain dwarf":
            print("Dwarves stand between 4 and 5 feet tall. Your size is Medium. What is your height?")
        elif self.race.lower() == "high elf" or "wood elf" or "drow":
            print("Elves range from under 5 to over 6 feet tall. Your size is Medium. What is your height?")
        elif self.race.lower() == "lightfoot halfling" or "stout halfling":
            print("Halfling average about 3 feet tall. Your size is Small. What is your height?")
        elif self.race.lower() == "human":
            print("Humans vary widely in height from barely 5 feet to well over 6 feet. Your size is Medium. What is your height?")
        elif self.race.lower() == "dragonborn":
            print("Dragonborn stand well over 6 feet tall. Your size is Medium. What is your height?")
        elif self.race.lower() == "rock gnome" or "forest gnome":
            print("Gnomes are between 3 and 4 feet tall. Your size is Small. What is your height?")
        elif self.race.lower() == "half-elf":
            print("Half-Elves are about the same size as humans ranging from 5 to 6 feet tall. Your size is Medium. What is your height?")
        elif self.race.lower() == "half-orc":
            print("Half-orcs are somewhat larger and bulkier than humans, and they range from 5 to well over 6 feet tall. Your size is medium. What is your height?")
        elif self.race.lower() == "tiefling":
            print("Tieflings are about the same size and build as humans standing barely 5 feet to well over 6 feet. Your size is Medium. What is your height?")

    def set_weight(self):
        if self.race.lower() == "hill dwarf" or "mountain dwarf":
            print("Dwarves weigh on average about 150 pounds. What is your weight?")
        elif self.race.lower() == "high elf" or "wood elf" or "drow":
            print("Elves weigh on average just over 100 pounds. What is your weight?")
        elif self.race.lower() == "lightfoot halfling" or "stout halfling":
            print("Halfings weight around 40 pounds on average. What is your weight?")
        elif self.race.lower() == "human":
            print("Humans vary widely in build but average about 110 pounds. What is your weight?")
        elif self.race.lower() == "dragonborn":
            print("Dragonborn average almost 250 pounds. What is your weight?")
        elif self.race.lower() == "rock gnome" or "forest gnome":
            print("Gnomes average about 40 pounds. What is your weight?")
        elif self.race.lower() == "half-elf":
            print("Half-Elves vary in build but average about 110 pounds. What is your weight?")
        elif self.race.lower() == "half-orc":
            print("Half-Orcs vary in build but average about 175 pounds. What is your weight?")
        elif self.race.lower() == "tiefling":
            print("Tieflings vary widely in build but average about 110 pounds. What is your weight?")
