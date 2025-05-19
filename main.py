#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
リバーシゲームのメインモジュール

このモジュールはリバーシゲームのエントリーポイントです。
ゲームの初期化と実行を担当します。
"""
from controllers.game_controller import GameController
from models.board import Board


def main():
    """
    ゲームのメイン関数
    ゲームコントローラーを初期化して実行します
    """
    board = Board()
    gc = GameController()
    print(board)
    gc.setup_game()
    gc.run()
    gc.end_game()


if __name__ == "__main__":
    main()
