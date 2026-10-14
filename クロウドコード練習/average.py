# テストの点数の平均と成績を出すプログラム
# ※ このプログラムにはバグがあります。Claude に直してもらいましょう！


def average(scores):
    total = 0
    for i in range(1, len(scores)):
        total += scores[i]
    return total / len(scores)


def grade(score):
    if score >= 80:
        return "A"
    elif score >= 60:
        return "B"
    else:
        return "C"


scores = [80, 65, 90, 45, 70]

print("平均点:", average(scores))  # 正しくは 70.0 になるはず
for s in scores:
    print(s, "点 →", grade(s))
