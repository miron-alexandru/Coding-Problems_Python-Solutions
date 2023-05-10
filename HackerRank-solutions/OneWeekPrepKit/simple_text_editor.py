# Problem Link: https://www.hackerrank.com/challenges/one-week-preparation-kit-simple-text-editor/problem


# My Solution:


class TextEditor:
    def __init__(self):
        self.text = ""
        self.operations = []

    def append(self, s):
        self.text += s
        self.operations.append(("append", s))

    def delete(self, k):
        deleted = self.text[-k:]
        self.text = self.text[:-k]
        self.operations.append(("delete", deleted))

    def print_text(self, k):
        print(self.text[k - 1])

    def undo(self):
        op = self.operations.pop()
        if op[0] == "append":
            self.text = self.text[: -len(op[1])]
        elif op[0] == "delete":
            self.text += op[1]


if __name__ == "__main__":
    text_edi = TextEditor()
    n = int(input().strip())

    for i in range(n):
        test = input().strip().split()

        if test[0] == "1":
            text_edi.append(test[1])
        elif test[0] == "2":
            text_edi.delete(int(test[1]))
        elif test[0] == "3":
            text_edi.print_text(int(test[1]))
        else:
            text_edi.undo()
