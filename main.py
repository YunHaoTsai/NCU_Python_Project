from sheet import Sheet
from user import User
# 創建用戶
kevin = User("Kevin")

# 用戶創建表單
sheetA = kevin.create_sheet("SheetA")
print(kevin.sheets)  # 應該顯示包含 SheetA 的列表
