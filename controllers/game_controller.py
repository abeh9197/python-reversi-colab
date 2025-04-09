#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
リバーシのゲームコントローラーを表すモジュール

このモジュールはリバーシゲームのMVCパターンのコントローラー部分を担当します。
"""

from models.game import Game
from models.player import HumanPlayer, ComputerPlayer
from views.console_view import ConsoleView


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
        # TODO: ゲームコントローラーを初期化するコードを書く
        pass
        
    def setup_game(self):
        """
        ゲームのセットアップを行う
        プレイヤーの種類（人間/コンピュータ）を選択する
        """
        # TODO: ゲームをセットアップするコードを書く
        pass
        
    def run(self):
        """
        ゲームのメインループを実行する
        """
        # TODO: ゲームのメインループを実行するコードを書く
        pass
        
    def process_turn(self):
        """
        １ターンの処理を行う
        
        Returns:
            bool: ゲームが続行中ならTrue、終了ならFalse
        """
        # TODO: １ターンの処理を行うコードを書く
        pass
        
    def end_game(self):
        """
        ゲーム終了時の処理を行う
        """
        # TODO: ゲーム終了時の処理を行うコードを書く
        pass
