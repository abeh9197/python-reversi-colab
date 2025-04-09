#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
リバーシゲームのメインモジュール

このモジュールはリバーシゲームのエントリーポイントです。
ゲームの初期化と実行を担当します。
"""

from controllers.game_controller import GameController


def main():
    """
    ゲームのメイン関数
    ゲームコントローラーを初期化して実行します
    """
    game = GameController()
    game.run()


if __name__ == "__main__":
    main()
