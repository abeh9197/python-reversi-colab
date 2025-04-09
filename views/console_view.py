#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
リバーシのコンソール表示を管理するモジュール

このモジュールはコンソール上でのリバーシゲームの表示を担当します。
"""


class ConsoleView:
    """
    コンソール上でのリバーシゲームの表示を管理するクラス
    
    Attributes:
        symbols (dict): 盤面表示に使用する記号
    """
    
    def __init__(self):
        """
        コンソールビューを初期化する
        """
        # TODO: コンソールビューを初期化するコードを書く
        pass
        
    def display_board(self, board):
        """
        盤面を表示する
        
        Args:
            board (Board): 表示する盤面
        """
        # TODO: 盤面を表示するコードを書く
        pass
        
    def display_score(self, black_count, white_count):
        """
        スコアを表示する
        
        Args:
            black_count (int): 黒石の数
            white_count (int): 白石の数
        """
        # TODO: スコアを表示するコードを書く
        pass
        
    def display_turn(self, player):
        """
        現在のプレイヤーのターンを表示する
        
        Args:
            player (Player): 現在のプレイヤー
        """
        # TODO: プレイヤーのターンを表示するコードを書く
        pass
        
    def display_valid_moves(self, valid_moves):
        """
        有効な手を表示する
        
        Args:
            valid_moves (list): 有効な手の座標タプル(row, col)のリスト
        """
        # TODO: 有効な手を表示するコードを書く
        pass
        
    def display_game_over(self, winner):
        """
        ゲーム終了と勝者を表示する
        
        Args:
            winner (Player): 勝者のプレイヤーオブジェクト、引き分けの場合はNone
        """
        # TODO: ゲーム終了と勝者を表示するコードを書く
        pass
        
    def get_player_move(self, valid_moves):
        """
        プレイヤーの入力から手を取得する
        
        Args:
            valid_moves (list): 有効な手の座標タプル(row, col)のリスト
            
        Returns:
            tuple: 選択した手の座標 (row, col)
        """
        # TODO: プレイヤーの入力を処理するコードを書く
        pass
        
    def display_error(self, message):
        """
        エラーメッセージを表示する
        
        Args:
            message (str): 表示するエラーメッセージ
        """
        # TODO: エラーメッセージを表示するコードを書く
        pass
