#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
リバーシのプレイヤーを表すモジュール

このモジュールはリバーシゲームのプレイヤー（人間とコンピュータ）を管理します。
"""


class Player:
    """
    リバーシのプレイヤーを表す基底クラス
    
    Attributes:
        player_id (int): プレイヤーID（1: 黒, 2: 白）
        name (str): プレイヤー名
    """
    
    def __init__(self, player_id, name):
        """
        プレイヤーを初期化する
        
        Args:
            player_id (int): プレイヤーID（1: 黒, 2: 白）
            name (str): プレイヤー名
        """
        # TODO: プレイヤーを初期化するコードを書く
        pass
        
    def get_move(self, board):
        """
        次の手を決定する（サブクラスでオーバーライドする）
        
        Args:
            board (Board): 現在の盤面
            
        Returns:
            tuple: 選択した手の座標 (row, col)
        """
        raise NotImplementedError("サブクラスでget_moveメソッドを実装してください")
        
        
class HumanPlayer(Player):
    """
    人間プレイヤーを表すクラス
    
    キーボード入力で手を選択します。
    """
    
    def get_move(self, board):
        """
        ユーザーの入力から次の手を取得する
        
        Args:
            board (Board): 現在の盤面
            
        Returns:
            tuple: 選択した手の座標 (row, col)
        """
        # TODO: ユーザー入力を処理するコードを書く
        pass
        
        
class ComputerPlayer(Player):
    """
    コンピュータプレイヤーを表すクラス
    
    簡単なアルゴリズムで手を選択します。
    """
    
    def get_move(self, board):
        """
        アルゴリズムに基づいて次の手を決定する
        
        Args:
            board (Board): 現在の盤面
            
        Returns:
            tuple: 選択した手の座標 (row, col)
        """
        # TODO: コンピュータの思考ルーチンを書く
        pass
