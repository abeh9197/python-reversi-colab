#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
リバーシの盤面を表すモジュール

このモジュールはリバーシゲームの盤面の状態と操作を管理します。
"""


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
        # TODO: 盤面を初期化するコードを書く
        pass
        
    def reset(self):
        """
        盤面を初期状態にリセットする
        中央に黒白の石を2つずつ配置する
        """
        # TODO: 盤面をリセットするコードを書く
        pass
        
    def is_valid_move(self, row, col, player):
        """
        指定した場所に石を置けるかどうかを判定する
        
        Args:
            row (int): 行インデックス
            col (int): 列インデックス
            player (int): プレイヤー番号（1: 黒, 2: 白）
            
        Returns:
            bool: 石を置けるならTrue、そうでなければFalse
        """
        # TODO: 石を置けるかどうかを判定するコードを書く
        pass
        
    def get_valid_moves(self, player):
        """
        指定したプレイヤーが石を置ける場所のリストを返す
        
        Args:
            player (int): プレイヤー番号（1: 黒, 2: 白）
            
        Returns:
            list: 石を置ける場所の座標タプル(row, col)のリスト
        """
        # TODO: 石を置ける場所のリストを返すコードを書く
        pass
        
    def place_stone(self, row, col, player):
        """
        指定した場所に石を置き、挟まれた相手の石を裏返す
        
        Args:
            row (int): 行インデックス
            col (int): 列インデックス
            player (int): プレイヤー番号（1: 黒, 2: 白）
            
        Returns:
            bool: 石を置くことができたらTrue、できなければFalse
        """
        # TODO: 石を置き、挟まれた石を裏返すコードを書く
        pass
        
    def count_stones(self):
        """
        盤面上の黒石と白石の数を数える
        
        Returns:
            tuple: (黒石の数, 白石の数)
        """
        # TODO: 石の数を数えるコードを書く
        pass
        
    def is_game_over(self):
        """
        ゲームが終了したかどうかを判定する
        
        Returns:
            bool: ゲームが終了していればTrue、そうでなければFalse
        """
        # TODO: ゲーム終了判定のコードを書く
        pass
        
    def __str__(self):
        """
        盤面の文字列表現を返す（デバッグ用）
        
        Returns:
            str: 盤面の文字列表現
        """
        # TODO: 盤面の文字列表現を返すコードを書く
        pass
