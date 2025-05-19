class Board:
    """
    リバーシの盤面を表すクラス
    
    盤面の状態を保持し、石を置く、裏返すなどの基本操作を提供します。
    
    Attributes:
        size (int): 盤面のサイズ（通常は8x8）
        grid (list): 盤面の状態を格納する2次元リスト
            0: 空きマス
            1: 黒石
            2: 白石
    """

    def __init__(self, size=8):
        """
        盤面を初期化する
        
        Args:
            size (int, optional): 盤面のサイズ。デフォルトは8。
        """
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]
        self.reset()
        
    def reset(self):
        """
        盤面を初期状態にリセットする
        中央に黒白の石を2つずつ配置する
        """
        # 盤面をすべて空きマスにする
        for row in range(self.size):
            for col in range(self.size):
                self.grid[row][col] = 0
        # 中央に初期配置の石を置く
        center = self.size // 2
        self.grid[center-1][center-1] = 2  # 白
        self.grid[center-1][center] = 1    # 黒
        self.grid[center][center-1] = 1    # 黒
        self.grid[center][center] = 2      # 白
        
    def __str__(self):
        """
        盤面の文字列表現を返す（デバッグ用）
        
        Returns:
            str: 盤面の文字列表現
        """
        # 列のインデックスを表示
        top_index = " " + " ".join(str(_) for _ in range(1, self.size + 1)) + "\n"
        board_str = ""
        for i, row in enumerate(self.grid, 1):
            col_str = f"{i}"
            for col in row:
                if col == 0:
                    col_str += "・"
                elif col == 1:
                    col_str += "○ "  # 黒
                else:
                    col_str += "● "
            board_str += col_str + "\n"
        top_index += board_str
        return top_index

    def reverse(self, valid_moves, color: int):
        from models.player import HumanPlayer, ComputerPlayer
        if color == 1:
            human = HumanPlayer()
            row, col = human.get_move(valid_moves)
        else:
            com = ComputerPlayer()
            row, col = com.get_move(valid_moves)
        
        turn_list = valid_moves[(row, col)][1]
        self.grid[row - 1][col - 1] = color
        while turn_list:
            r, c = turn_list.pop(0)
            self.grid[r - 1][c - 1] = color
        print(self.__str__())

    def valid_moves(self, color: int):
        """
        有効な手を表示する
        Args:
            valid_moves (list): 有効な手の座標タプル(row, col)のリスト
        """
        opponent = 3 - color
        valid_moves_count = {}
        directions = [(0, 1), (0, -1), (1, -1), (1, 0), (1, 1), (-1, -1), (-1, 0), (-1, 1)]
        for row in range(8):
            for col in range(8):
                if self.grid[row][col] == 0:
                    count_turn = 0
                    turn_list = []
                    for d_row, d_col in directions:
                        r, c = row + d_row, col + d_col
                        count_turn_ = 0
                        turn_list_ = []
                        while 0 <= r < 8 and 0 <= c < 8 and self.grid[r][c] == opponent:
                            turn_list_.append((r + 1, c + 1))
                            count_turn_ += 1
                            r += d_row
                            c += d_col
                            if 0 <= r < 8 and 0 <= c < 8 and self.grid[r][c] == color:
                                turn_list.extend(turn_list_)
                                count_turn += count_turn_
                                break
                    if count_turn > 0:
                        valid_moves_count[(row + 1, col + 1)] = [[count_turn], turn_list]
        return valid_moves_count