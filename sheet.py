class Sheet:
    def __init__(self, name):
        self.name = name
        self.content = []

        for i in range(3):
            self.content.append([0, 0, 0])
        
        self.access_rights = {} #Hash Map 存 user 的 right
    
    def change_value(self, row, col, value):
        if 0 <= row <= len(self.content) and 0 <= col <= len(self.content[0]):
            self.content[row][col] = value
        else:
            print("Invalid postion!")

    def set_access_right(self, user, right):
        self.access_rights[user] = right

    def __repr__(self):
        """自定義顯示表單內容"""
        return '\n'.join([', '.join(map(str, row)) for row in self.content])