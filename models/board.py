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
        self._symbols = {
            0: "・",
            1: "⚫︎",
            2: "⚪︎"
        }

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
        self.grid[center - 1][center - 1] = 2  # 白
        self.grid[center - 1][center] = 1  # 黒
        self.grid[center][center - 1] = 1  # 黒
        self.grid[center][center] = 2  # 白

    def __str__(self):
        """
        盤面の文字列表現を返す（デバッグ用）

        Returns:
            str: 盤面の文字列表現
        """
        # 列のインデックスを表示
        grid_str_ = "  0  1  2  3  4  5  6  7  \n"
        for row_num, row in enumerate(self.grid):
            print_row = str(row_num)
            for col in row:
                sym = self._symbols[col]
                print_row += " " + sym
            grid_str_ += print_row + "\n"
        return grid_str_
