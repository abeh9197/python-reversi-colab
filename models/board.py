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
        s = "this is board\n"
        return s
