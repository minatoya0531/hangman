#私の元の回答も関数の中に組み込めた！から正解！

"""
import random

def hangman(word): #引数wordで，プレーヤー2(人間)に当ててほしい単語を受け取る
    wrong = 0 #変数wrongはプレーヤー2が何回間違えたかを数える
    stages = ["", ##変数stagesは文字列のリスト これを用いて吊られた人の絵を描いていく
              "_______      ", #このリストの文字列を1行に1つずつ出力していく
              "|            ",
              "|      |     ",
              "|      O     ",
              "|     /|\    ",
              "|     / \    ",
              "|            ",
              ]
    rletters = list(word) #wordの文字を1文字ずつの要素に分解してリストにしたもの．答えなければならない残りの文字を記憶
    board = ["_"] * len(word) #プレーヤー2に見せるヒントを記録する文字列.catの場合，初期状態は["_", "_", "_"]
    win = False               #プレーヤー2がゲームに勝ったかどうかの状態を記録．初期状態ではFalseを割り当てる．最後に「Welcome to Hangman!」を表示
    print("ハングマンへようこそ!")

    #以下のループはゲームの勝敗が決まるまで回り続ける
    while wrong < len(stages) - 1: #ループはwrongの値がlen(stages) - 1よりも小さい間繰り返される(stagesの数を1から数え，wrongの数を1から数えるという違いを合わせるための-1)
        print("\n") #ゲームの見た目を良くするために空行を出力
        msg = "1文字を予想してね"
        char = input(msg) #プレーヤー2が入力した回答を割り当てる
        if char in rletters: #入力された回答がrletter(プレーヤー2がまだ答えていない文字のリスト)の要素にあったら,boardを更新する(プレーヤー2がcを入力したらboardの内容を["c", "_", "_"]に更新)
            cind = rletters.index(char) #入力された文字がrlettersの何番目にあるかのインデックスを取得
            board[cind] = char #このインデックス値を利用して，boardのアンダースコアを正しい文字に置き換え
            rletters[cind] = '$' #正解した文字を「$」に置き換え(同じ文字が複数存在する場合への対処)
        else:
            wrong += 1 #プレーヤー2の回答が間違っていたらwrongを1つ増やす
        print(" ".join(board)) #スコアボードの出力("_", "_", "_")
        e = wrong + 1
        print("\n".join(stages[0:e])) #stagesリストに含まれるすべての文字列を改行コードで結合し，出力(0からwrongに1を足した数まで)
        if "_" not in board: #プレーヤー2(人間)が勝ったかどうかの確認
            print("あなたの勝ち！") #boardにアンダースコアが無い＝すべての文字が正解された
            print(" ".join(board)) #正解した単語の表示
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け!正解は{}.".format(word))

hangman_list = ["panda", "Finland", "musical"]
random_w = random.choice(hangman_list)
hangman(random_w)

"""

"""
#模範回答
import random

def hangman(): #引数wordで，プレーヤー2(人間)に当ててほしい単語を受け取る
    hangman_list = ["panda", "Finland", "musical"] #関数内にリストを作成
    random_number = random.randint(0,2) #リストの中からランダムで選ぶ
    word = hangman_list[random_number] #ランダムで選んだインデックス値を入れる
    wrong = 0 #変数wrongはプレーヤー2が何回間違えたかを数える
    stages = ["", ##変数stagesは文字列のリスト これを用いて吊られた人の絵を描いていく
              "_______      ", #このリストの文字列を1行に1つずつ出力していく
              "|            ",
              "|      |     ",
              "|      O     ",
              "|     /|\    ",
              "|     / \    ",
              "|            ",
              ]
    rletters = list(word) #wordの文字を1文字ずつの要素に分解してリストにしたもの．答えなければならない残りの文字を記憶
    board = ["_"] * len(word) #プレーヤー2に見せるヒントを記録する文字列.catの場合，初期状態は["_", "_", "_"]
    win = False               #プレーヤー2がゲームに勝ったかどうかの状態を記録．初期状態ではFalseを割り当てる．最後に「Welcome to Hangman!」を表示
    print("ハングマンへようこそ!")

    #以下のループはゲームの勝敗が決まるまで回り続ける
    while wrong < len(stages) - 1: #ループはwrongの値がlen(stages) - 1よりも小さい間繰り返される(stagesの数を1から数え，wrongの数を1から数えるという違いを合わせるための-1)
        print("\n") #ゲームの見た目を良くするために空行を出力
        msg = "1文字を予想してね"
        char = input(msg) #プレーヤー2が入力した回答を割り当てる
        if char in rletters: #入力された回答がrletter(プレーヤー2がまだ答えていない文字のリスト)の要素にあったら,boardを更新する(プレーヤー2がcを入力したらboardの内容を["c", "_", "_"]に更新)
            cind = rletters.index(char) #入力された文字がrlettersの何番目にあるかのインデックスを取得
            board[cind] = char #このインデックス値を利用して，boardのアンダースコアを正しい文字に置き換え
            rletters[cind] = '$' #正解した文字を「$」に置き換え(同じ文字が複数存在する場合への対処)
        else:
            wrong += 1 #プレーヤー2の回答が間違っていたらwrongを1つ増やす
        print(" ".join(board)) #スコアボードの出力("_", "_", "_")
        e = wrong + 1
        print("\n".join(stages[0:e])) #stagesリストに含まれるすべての文字列を改行コードで結合し，出力(0からwrongに1を足した数まで)
        if "_" not in board: #プレーヤー2(人間)が勝ったかどうかの確認
            print("あなたの勝ち！") #boardにアンダースコアが無い＝すべての文字が正解された
            print(" ".join(board)) #正解した単語の表示
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け!正解は{}.".format(word))

hangman()

"""


import random

def hangman(): #引数wordで，プレーヤー2(人間)に当ててほしい単語を受け取る
    hangman_list = ["panda", "Finland", "musical"] #関数内にリストを作成
    word = random.choice(hangman_list) #リストの中からランダムで選ぶ
    wrong = 0 #変数wrongはプレーヤー2が何回間違えたかを数える
    stages = ["", ##変数stagesは文字列のリスト これを用いて吊られた人の絵を描いていく
              "_______      ", #このリストの文字列を1行に1つずつ出力していく
              "|            ",
              "|      |     ",
              "|      O     ",
              "|     /|\    ",
              "|     / \    ",
              "|            ",
              ]
    rletters = list(word) #wordの文字を1文字ずつの要素に分解してリストにしたもの．答えなければならない残りの文字を記憶
    board = ["_"] * len(word) #プレーヤー2に見せるヒントを記録する文字列.catの場合，初期状態は["_", "_", "_"]
    win = False               #プレーヤー2がゲームに勝ったかどうかの状態を記録．初期状態ではFalseを割り当てる．最後に「Welcome to Hangman!」を表示
    print("ハングマンへようこそ!")

    #以下のループはゲームの勝敗が決まるまで回り続ける
    while wrong < len(stages) - 1: #ループはwrongの値がlen(stages) - 1よりも小さい間繰り返される(stagesの数を1から数え，wrongの数を1から数えるという違いを合わせるための-1)
        print("\n") #ゲームの見た目を良くするために空行を出力
        msg = "1文字を予想してね"
        char = input(msg) #プレーヤー2が入力した回答を割り当てる
        if char in rletters: #入力された回答がrletter(プレーヤー2がまだ答えていない文字のリスト)の要素にあったら,boardを更新する(プレーヤー2がcを入力したらboardの内容を["c", "_", "_"]に更新)
            cind = rletters.index(char) #入力された文字がrlettersの何番目にあるかのインデックスを取得
            board[cind] = char #このインデックス値を利用して，boardのアンダースコアを正しい文字に置き換え
            rletters[cind] = '$' #正解した文字を「$」に置き換え(同じ文字が複数存在する場合への対処)
        else:
            wrong += 1 #プレーヤー2の回答が間違っていたらwrongを1つ増やす
        print(" ".join(board)) #スコアボードの出力("_", "_", "_")
        e = wrong + 1
        print("\n".join(stages[0:e])) #stagesリストに含まれるすべての文字列を改行コードで結合し，出力(0からwrongに1を足した数まで)
        if "_" not in board: #プレーヤー2(人間)が勝ったかどうかの確認
            print("あなたの勝ち！") #boardにアンダースコアが無い＝すべての文字が正解された
            print(" ".join(board)) #正解した単語の表示
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け!正解は{}.".format(word))

hangman()

