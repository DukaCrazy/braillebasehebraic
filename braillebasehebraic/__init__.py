from braillebase import BrailleBase

class BrailleBaseHebraic(BrailleBase):
    def __init__(self):

        """
        """
        super().__init__()
        self.setting_braille_rules_uppercase("⠨", "⠐") 

        #Alphabet Hebraic
        self.append_braille_letter("א", ["⠁"], 3) 
        self.append_braille_letter("בּ", ["⠃"], 3) 
        self.append_braille_letter("ב", ["⠧"], 3) 
        self.append_braille_letter("ג", ["⠛"], 3) 
        self.append_braille_letter("ד", ["⠙"], 3) 
        self.append_braille_letter("ה", ["⠓"], 3) 
        self.append_braille_letter("ו", ["⠺"], 3) 
        self.append_braille_letter("וֹ", ["⠕"], 3) 
        self.append_braille_letter("וּ", ["⠥"], 3) 
        self.append_braille_letter("ז", ["⠵"], 3) 
        self.append_braille_letter("ח", ["⠭"], 3) 
        self.append_braille_letter("ט", ["⠞"], 3) 
        self.append_braille_letter("י", ["⠚"], 3) 
        self.append_braille_letter("ִי", ["⠊"], 3) 
        self.append_braille_letter("כּ", ["⠅"], 3) 
        self.append_braille_letter("כ", ["⠡"], 3) 
        self.append_braille_letter("ל", ["⠇"], 3) 
        self.append_braille_letter("מ", ["⠍"], 3) 
        self.append_braille_letter("נ", ["⠝"], 3) 
        self.append_braille_letter("ס", ["⠎"], 3) 
        self.append_braille_letter("ע", ["⠫"], 3) 
        self.append_braille_letter("פּ", ["⠏"], 3) 	
        self.append_braille_letter("פ", ["⠋"], 3) 
        self.append_braille_letter("צ", ["⠮"], 3) 
        self.append_braille_letter("ק", ["⠟"], 3) 
        self.append_braille_letter("ר", ["⠗"], 3) 
        self.append_braille_letter("שׂ", ["⠱"], 3) 
        self.append_braille_letter("שׁ", ["⠩"], 3)
        self.append_braille_letter("ת", ["⠹"], 3)
         

        self.append_braille_letter("...", ["⠄", "⠄", "⠄"])
        self.append_braille_letter("…", ["⠄", "⠄", "⠄"])
        self.append_braille_letter("———", ["⠤", "⠤", "⠤"])