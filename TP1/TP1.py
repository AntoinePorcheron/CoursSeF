
class Arbre():
    def __init__(self,nom=''):
        self.label = nom
        self.G = None
        self.D = None

    def PrintValues(self):
        print(self.label)
        if self.G:
            self.G.PrintValues()
        if self.D:
            self.D.PrintValues()

    def EcritValues(self, Res_Ret = ""):
        # print(self.label)
        match self.label :
            case "¬":   Res_Ret = "¬(" + self.D.EcritValues() + ")"
            case "A":   Res_Ret = "(" + self.G.EcritValues() + ") A (" + self.D.EcritValues() + ")"
            case "V":   Res_Ret = "(" + self.G.EcritValues() + ") V (" + self.D.EcritValues() + ")"
            case _  :   Res_Ret = self.label
        return Res_Ret

    def Display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.D is None and self.G is None:
            line = '%s' % self.label
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.D is None:
            lines, n, p, x = self.G._display_aux()
            s = '%s' % self.label
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.G is None:
            lines, n, p, x = self.D._display_aux()
            s = '%s' % self.label
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.G._display_aux()
        right, m, q, y = self.D._display_aux()
        s = '%s' % self.label
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

T = Arbre('A')
T.G = Arbre('X1')
T.D = Arbre('¬')
T.D.D = Arbre('V')
T.D.D.G = Arbre('X2')
T.D.D.D = Arbre('¬')
T.D.D.D.D = Arbre('X3')

print("PrintValues ================================= ")
T.PrintValues()
print("Display ================================= ")
T.Display()
print("EcritValues ================================= ")
Res=T.EcritValues()
print("Res = " + Res)

