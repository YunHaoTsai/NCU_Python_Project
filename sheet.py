# sheet.py

class Sheet:
    def __init__(self, name):
        """Initialize the sheet."""
        self.name = name
        self.content = [[0 for _ in range(3)] for _ in range(3)]  # 3x3 empty grid initialized to 0
        self.access_rights = {}  # Access rights (key: username, value: 'ReadOnly' or 'Editable')

    def change_value(self, row, col, value, user):
        """Change a value in the sheet (requires appropriate permissions)."""
        if self.access_rights.get(user, 'ReadOnly') == 'Editable':
            if 0 <= row < len(self.content) and 0 <= col < len(self.content[0]):
                self.content[row][col] = self._evaluate_expression(value)
            else:
                raise ValueError("Row or column index out of bounds.")
        else:
            raise PermissionError("This sheet is not editable by the user.")

    def share_with_user(self, username, access_type):
        """Share the sheet with another user, setting their access rights."""
        if access_type in ['ReadOnly', 'Editable']:
            self.access_rights[username] = access_type
        else:
            raise ValueError("Invalid access type. Use 'ReadOnly' or 'Editable'.")

    @staticmethod
    def _evaluate_expression(expr):
        """Evaluate a basic mathematical expression (e.g., addition, subtraction)."""
        try:
            return eval(expr, {"__builtins__": None}, {})
        except Exception:
            raise ValueError("Invalid mathematical expression.")

    def __repr__(self):
        """Display the sheet content."""
        return '\n'.join([', '.join(map(str, row)) for row in self.content])


class User:
    def __init__(self, name):
        """Initialize the user."""
        self.name = name
        self.sheets = []  # Sheets created by the user
        self.shared_sheets = []  # Sheets shared with the user

    def create_sheet(self, sheet_name):
        """Create a new sheet."""
        if any(sheet.name == sheet_name for sheet in self.sheets):
            raise ValueError(f"Sheet with the name '{sheet_name}' already exists!")
        
        sheet = Sheet(sheet_name)
        sheet.access_rights[self.name] = 'Editable'  # Default to editable for the owner
        self.sheets.append(sheet)
        return sheet

    def __repr__(self):
        """Display user information."""
        return f"User(name={self.name}, sheets={[sheet.name for sheet in self.sheets]})"