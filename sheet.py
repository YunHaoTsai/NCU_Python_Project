# sheet.py

class Sheet:
    def __init__(self, name):
        """初始化表單"""
        self.name = name
        self.content = [
            [0 for _ in range(3)] for _ in range(3)
        ]  # 初始化為 3x3 空表格
        self.access_rights = {}  # 用戶訪問權限 (key: username, value: 'ReadOnly' or 'Editable')

    def change_value(self, row, col, value, user):
        """更改表單的值 (需檢查權限)"""
        if self.access_rights.get(user, 'ReadOnly') == 'Editable':
            if 0 <= row < 3 and 0 <= col < 3:
                self.content[row][col] = self._evaluate_expression(value)
            else:
                raise ValueError("Row or column out of bounds")
        else:
            raise PermissionError("This sheet is not editable by this user")

    def share_with_user(self, username, access_type):
        """分享表單給其他用戶並設置權限"""
        if access_type in ['ReadOnly', 'Editable']:
            self.access_rights[username] = access_type
        else:
            raise ValueError("Invalid access type. Use 'ReadOnly' or 'Editable'.")

    @staticmethod
    def _evaluate_expression(expr):
        """計算簡單的數學表達式 (加減乘除)"""
        try:
            return eval(expr, {"__builtins__": None}, {})
        except Exception:
            raise ValueError("Invalid expression")

    def __repr__(self):
        """顯示表單內容"""
        return '\n'.join([', '.join(map(str, row)) for row in self.content])


class User:
    def __init__(self, name):
        """初始化用戶"""
        self.name = name
        self.sheets = []  # 該用戶創建的表單列表
        self.shared_sheets = []  # 該用戶可訪問的共享表單

    def create_sheet(self, sheet_name):
        """創建新表單"""
        sheet = Sheet(sheet_name)
        sheet.access_rights[self.name] = 'Editable'  # 預設擁有編輯權限
        self.sheets.append(sheet)
        return sheet

    def __repr__(self):
        """顯示用戶信息"""
        return f"User(name={self.name}, sheets={[sheet.name for sheet in self.sheets]})"
