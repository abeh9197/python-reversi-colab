#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
リバーシのゲームコントローラーを表すモジュール

このモジュールはリバーシゲームのMVCパターンのコントローラー部分を担当します。
"""
from views.console_view import ConsoleView
from models.board import Board


class GameController:
    """
    リバーシのゲームコントローラークラス
    
    モデル（Game）とビュー（ConsoleView）の橋渡しをします。
    ユーザー入力の処理と、ゲームの状態の更新、表示の管理を担当します。
    
    Attributes:
        game (Game): ゲームモデル
        view (ConsoleView): ビュー
    """
    
    def __init__(self):
        """
        ゲームコントローラーを初期化する
        """
        self.view = ConsoleView()
        self.board: Board = Board()
        
    def setup_game(self):
        """
        ゲームのセットアップを行う
        プレイヤーの種類（人間/コンピュータ）を選択する
        """
        first_player: int = input("先攻コンピュータにしたいなら2を入力")
        if first_player == "2":
            self.board.reverse(self.board.valid_moves(color=2), color=2)
        
    def run(self):
        """
        ゲームのメインループを実行する
        """
        while not self.is_finish():
            self.view.display_valid_moves(self.board.valid_moves(color=1))
            if self.is_can_put(self.board.valid_moves(color=1)):
                self.score()
                self.board.reverse(self.board.valid_moves(color=1), color=1)
            else:
                print("playerターンpass")
            self.view.display_valid_moves(self.board.valid_moves(color=2))
            if self.is_can_put(self.board.valid_moves(color=2)):
                self.board.reverse(self.board.valid_moves(color=2), color=2)
            else:
                print("comターンpass")
        
    def end_game(self):
        """
        ゲーム終了時の処理を行う
        """
        print("ゲーム終了")
        black_count, white_count = self.score()
        if black_count > white_count:
            print("勝者はplayer!")
        elif black_count < white_count:
            print("勝者はcomputer!")
        else:
            print("引き分け")
    
    def score(self) -> tuple[int, int]:
        black_count = 0
        white_count = 0
        for row in range(self.board.size):
            for col in range(self.board.size):
                if self.board.grid[row][col] == 1:
                    black_count += 1
                elif self.board.grid[row][col] == 2:
                    white_count += 1
        print(f"黒:{black_count}\n白:{white_count}")
        return (black_count, white_count)

    def is_finish(self) -> bool:
        pass1 = self.is_can_put(self.board.valid_moves(color=1))
        pass2 = self.is_can_put(self.board.valid_moves(color=2))
        if not pass1 and not pass2:
            return True
    
    def is_can_put(self, valid_moves) -> bool:
        return bool(valid_moves)