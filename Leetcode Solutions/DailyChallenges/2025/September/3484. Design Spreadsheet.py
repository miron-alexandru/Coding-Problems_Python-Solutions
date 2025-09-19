# problem link: https://leetcode.com/problems/design-spreadsheet/


# Description:
"""
A spreadsheet is a grid with 26 columns (labeled from 'A' to 'Z') and a given number of rows. Each cell in the spreadsheet can hold an integer value between 0 and 105.

Implement the Spreadsheet class:

Spreadsheet(int rows) Initializes a spreadsheet with 26 columns (labeled 'A' to 'Z') and the specified number of rows. All cells are initially set to 0.
void setCell(String cell, int value) Sets the value of the specified cell. The cell reference is provided in the format "AX" (e.g., "A1", "B10"), where the letter represents the column (from 'A' to 'Z') and the number represents a 1-indexed row.
void resetCell(String cell) Resets the specified cell to 0.
int getValue(String formula) Evaluates a formula of the form "=X+Y", where X and Y are either cell references or non-negative integers, and returns the computed sum.
Note: If getValue references a cell that has not been explicitly set using setCell, its value is considered 0.

"""
# Solution:
class Spreadsheet:
    def __init__(self, rows: int):
        self.rows = rows
        self.cells = {}

    def _parse_cell(self, cell: str) -> tuple:
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:]) - 1
        if not (0 <= col < 26 and 0 <= row < self.rows):
            raise ValueError("Invalid cell reference")
        return (row, col)

    def setCell(self, cell: str, value: int) -> None:
        r, c = self._parse_cell(cell)
        self.cells[(r, c)] = value

    def resetCell(self, cell: str) -> None:
        r, c = self._parse_cell(cell)
        self.cells.pop((r, c), None)

    def _get_cell_value(self, cell: str) -> int:
        r, c = self._parse_cell(cell)
        return self.cells.get((r, c), 0)

    def _get_token_value(self, token: str) -> int:
        if token[0].isalpha():
            return self._get_cell_value(token)
        return int(token)

    def getValue(self, formula: str) -> int:
        if not formula.startswith("="):
            raise ValueError("Formula must start with '='")
        tokens = formula[1:].split("+")
        total = 0
        for token in tokens:
            token = token.strip()
            total += self._get_token_value(token)
        return total

        