"""
unicodeの国旗: U+1F1E6 〜 U+1F1FF
U+1F1E6(Aに相当): bytes([0xF0, 0x9F, 0x87, 0xA6])

ex. JPの国旗:
    ord('P') - ord('A') = 15
    U+1F1E6 + 15 = U+1F1F5

    ord('J') - ord('A') = 9
    U+1F1E6 + 9 = U+1F1EF

    U+1F1EF U+1F1F5 = 🇯🇵

solver:
    1. 読み取り and 国旗1文字抜き出し
    2. byte変換 and U+1F1E6との差分(diff) and a-zに変換
    3. 繋げて出力

"""

def rev_risl(c):
    c_byte = c.encode("utf-8")
    base_bytes = bytes([0xF0, 0x9F, 0x87, 0xA6]) #U+1F1E6

    # 4バイトかつ,先頭3がU+1F1E6と同じ
    if len(c_byte) == 4 and c_byte[:3] == base_bytes[:3]:
        diff = c_byte[3] - base_bytes[3]
        if 0 <= diff <= 25:
            return chr(ord('a') + diff) #offsetを計算→a-zに変換

    return c    #   { }  はそのまま

output_txt = "/Users/manki/Desktop/セキュリティ/AlpacaHack/flags-for-the-flag/output.txt"

with open(output_txt, "r") as f:
    data = f.read()

def map_rev_risl(s):
    return "".join(map(rev_risl, s))


print(map_rev_risl((data)))




