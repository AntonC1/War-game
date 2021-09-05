from random import shuffle


class Karty:
    Typ_karty = ["pik", "kier",
                 "karo", "trefl"]

    Wartosc = [None, None, "2", "3",
               "4", "5", "6", "7",
               "8", "9", "10", "Jopek",
               "Dama", "Krol", "As"]

    def __init__(self, v, s):
        self.wartosc2 = v
        self.Typ = s

    def __lt__(self, c2):
        if self.wartosc2 \
                < c2.wartosc2 \
                :
            return True
        if self.wartosc2 \
                == c2.wartosc2 \
                :
            if self.Typ < c2.Typ:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.wartosc2 \
                > c2.wartosc2 \
                :
            return True
        if self.wartosc2 \
                == c2.wartosc2 \
                :
            if self.Typ > c2.Typ:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.Wartosc[self.wartosc2
            ] + \
            " " + \
            self.Typ_karty[self.Typ]
        return v


class talia:
    def __init__(self):
        self.Karty = []
        for i in range(2, 15):
            for j in range(4):
                self.Karty \
                    .append(Karty(i,
                                  j))
        shuffle(self.Karty)

    def pozostale_karty(self):
        if len(self.Karty) == 0:
            return
        return self.Karty.pop()


class Gracz:
    def __init__(self, imie):
        self.wygrane = 0
        self.Karty = None
        self.imie = imie


class Game:
    def __init__(self):
        imie1 = input("Gracz 1 imie :")
        imie2 = input("Gracz 2 imie :")
        self.talia = talia()
        self.gracz1 = Gracz(imie1)
        self.gracz2 = Gracz(imie2)

    def wygrane(self, zwyciezca):
        w = "{} wygrywa te runde"
        w = w.format(zwyciezca)
        print(w)

    def draw(self, gracz1n, gracz1c, gracz2n, gracz2c):
        d = "{} dobiera {} {} dobiera {}"
        d = d.format(gracz1n,
                     gracz1c,
                     gracz2n,
                     gracz2c)
        print(d)

    def play_game(self):
        Karty = self.talia.Karty
        print("Gra rozpoczeta")
        while len(Karty) >= 2:
            m = "x by zakonczyc. Jakikolwiek " + \
                "przycisk poza x by grac:"
            response = input(m)
            if response == 'x':
                break
            gracz1c = self.talia.pozostale_karty()
            gracz2c = self.talia.pozostale_karty()
            gracz1n = self.gracz1.imie
            gracz2n = self.gracz2.imie
            self.draw(gracz1n,
                      gracz1c,
                      gracz2n,
                      gracz2c)
            if gracz1c > gracz2c:
                self.gracz1.wygrane += 1
                self.wygrane(self.gracz1.imie)
            else:
                self.gracz2.wygrane += 1
                self.wygrane(self.gracz2.imie)

        wygrana = self.zwyciezca(self.gracz1,
                          self.gracz2)
        print("Gra zakonczona wygrywa {} "
              .format(wygrana))

    def zwyciezca(self, gracz1, gracz2):
        if gracz1.wygrane > gracz2.wygrane:
            return gracz1.imie
        elif gracz1.wygrane < gracz2.wygrane:
            return gracz2.imie
        elif gracz1.wygrane == gracz2.wygrane:
            return "Remis!"


game = Game()
game.play_game()
