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

    def __init__(self):
        """
        プレイヤーを初期化する

        Args:
            player_id (int): プレイヤーID（1: 黒, 2: 白）
            name (str): プレイヤー名
        """
        self.player = {1: "黒", 2: "白"}

    def get_move(self):
        """
        次の手を決定する（サブクラスでオーバーライドする）
        """
        raise NotImplementedError("サブクラスでget_moveメソッドを実装してください")


class HumanPlayer(Player):
    def get_move(self, valid_moves: dict) -> tuple[int, int]:
        """
        ユーザーの入力から次の手を取得する
        """
        max_turn = max(valid_moves.items(), key=lambda x: x[1])
        print(f"一番めくれる手{max_turn}")
        while True:
            input_value: int = input("列を入力、スペース入れて行を入力してください")
            try:
                input_row, input_col = input_value.split()
                row, col = int(input_row), int(input_col)
                if (row, col) in valid_moves.keys():
                    return row, col
                    break
                else:
                    print("そこには置けません。入力し直してください")
            except ValueError:
                print("無効な入力です\n")


class ComputerPlayer(Player):
    def get_move(self, valid_moves: dict) -> tuple[int, int]:
        """
        アルゴリズムに基づいて次の手を決定する
        """
        # 置けるとこの中から一番ひっくり返せる枚数が多いところを選択
        max_turn = max(valid_moves.items(), key=lambda x: x[1])
        max_place = max_turn[0]
        print(f"一番めくれる手{max_turn}")
        return max_place
