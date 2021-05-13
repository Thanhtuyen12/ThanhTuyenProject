#!/usr/bin/env python3


data = {
    "xanh lá": "#3cba54",
    "vàng": "#f4c20d",
    "đỏ": "#db3236",
    "xanh da trời": "#4885ed",
}


def solve(colors):
    """Ghi ra file index.html code HTML để tạo ra logo của Google với màu sắc
    chính xác.
    Biết cách để tạo chữ G màu xanh da trời dùng code HTML sau::

      <span style="color:#4885ed">G</span>

    Return list chứa các tuple, mỗi tuple  chứa chữ cái trong 'Google' và màu
    của nó.
    Gợi ý: dùng `zip`

        In [1]: list(zip(['xanh', 'do'], ['XXX', 'YYY']))
        Out[1]: [('xanh', 'XXX'), ('do', 'YYY')]
    """
    result = []
    list_color = ['xanh da trời', "đỏ", "vàng",
                  'xanh da trời', "xanh lá", "đỏ"]
    list_code_google = [colors[color] for color in list_color]
    result = list(zip("Google", list_code_google))
    f = open('index.html', 'wt')
    for char, code in result:
        f.write('<span style="color:{}">{}</span>'.format(code, char))

    return result


def main():
    """Biết mã hex của các màu trong Google logo là:"""
    colors = data
    print(solve(colors))


if __name__ == "__main__":
    main()
