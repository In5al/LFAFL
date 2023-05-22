class ChomskyNormalForm:
    def __init__(self, VN, VT, P, S):
        self.VN = VN
        self.VT = VT
        self.P = P
        self.S = S

    def eliminate_epsilon(self):
        P = self.P.copy()
        eps_productions = [sym for sym in P if '' in P[sym]]
        new_productions = {}
        for sym in P:
            new_productions[sym] = [p for p in P[sym] if p != 'epsilon']
            for i, p in enumerate(new_productions[sym]):
                for j in range(len(p)):
                    if p[j] in eps_productions:
                        for eps_prod in self.combine_epsilon(P[p[j]]):
                            new_productions.setdefault(sym, []).append(p[:j] + eps_prod + p[j + 1:])
        self.P = new_productions
        print(self.P)

    def combine_epsilon(self, productions):
        if not productions:
            return ['']
        combined = []
        for p in self.combine_epsilon(productions[1:]):
            combined.append(productions[0] + p)
        return combined



    def eliminate_unit(self):
        for production in self.P:
            for symbol in self.P[production]:
                if symbol in self.VN:
                    self.P[production].remove(symbol)
                    self.P[production].extend(self.P[symbol])
                    print(self.P)

    def eliminate_nonproductive_inaccessible(self):
        reached = set()
        unreached = self.VN.copy()
        reached.add(self.S)
        while True:
            changed = False
            for sym in self.P:
                if sym in unreached:
                    for prod in self.P[sym]:
                        if all(s in reached or s in self.VT for s in prod):
                            unreached.remove(sym)
                            reached.add(sym)
                            changed = True
                            break
                if changed:
                    break
            if not changed:
                break

        nused = unreached
        for sym in nused:
            del self.P[sym]
            self.VN.remove(sym)
            if sym == self.S:
                self.S = None
        self.VT = set(t for prod in self.P.values() for s in prod for t in s if t not in self.VN)
        print(self.P)

    def Chomsky(self):
        self.VN.append('S0')
        dict = {'S0': ['S']}
        self.P = {**dict, **self.P}

        final = {}
        dict = {}
        flag = 0
        for production in self.P:
            for symbol in self.P[production]:
                if len(symbol) > 1:
                    for char in symbol:
                        if char in self.VT and char not in final.values():
                            final[chr(70 + flag)] = char
                            dict[char] = chr(70 + flag)
                            flag += 1

        for item in dict.keys():
            for production in self.P:
                for i in range(len(self.P[production])):
                    if len(self.P[production][i]) > 1:
                        self.P[production][i] = self.P[production][i].replace(item, dict[item])

        self.P = {**self.P, **final}
        flag = 1
        final = {}
        for production in self.P:
            for symbol in self.P[production]:
                if len(symbol) > 2:
                    final[production] = 'Y'

        production = list(self.P.keys())[1]
        for symbol in self.P[production]:
            if len(symbol) > 2:
                while len(symbol) > 2:
                    final[('X' + str(flag))] = symbol[:2]
                    print(('X' + str(flag)), '->', symbol[:2])
                    flag += 1
                    if len(symbol[2:]) > 2:
                        final[('X' + str(flag))] = ('X' + str(flag + 1)) + symbol[-1]
                        print(('X' + str(flag)), '->', ('X' + str(flag + 1)) + symbol[-1])
                        flag += 1
                    symbol = symbol[2:]

        for production in self.P:
            for symbol in self.P[production]:
                if len(symbol) > 2:
                    self.P[production].remove(symbol)

        for production in final:
            if production in self.P:
                self.P[production].append(final[production])
            else:
                self.P[production] = final[production]

        print("P =", self.P)