from sheet import Sheet
class User:
    def __init__(self, name):
        """初始化用戶資料"""
        self.name = name
        self.sheets = []       #user創建的表單
        self.shared_sheet = [] #user可以訪問的表單
    
    def add_sheet(self, sheet):
        """將表單加入用戶擁有的表單"""
        self.sheets.append(sheet)

    def add_shared_sheet(self, sheet):
        """將表單加入用戶共享的表單"""
        self.sheets.append(sheet)

    def create_sheet(self, sheet_name):
        sheet = Sheet(sheet_name)  # 使用 sheet_name 參數，而不是 sheet__name
        self.sheets.append(sheet)  # 把新創建的表單添加到 user 的 sheets 中
        return sheet



    

                
