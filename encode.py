class Leaves:
    def __init__(self, data=None):
        self.data = data
        self.bin = ''
        self.right = None
        self.left = None
        self.code = ''
        self.is_leaves = True

    def __str__(self):
        return "大树"


def create_weight_table(s):
    weight_table_dic = {}
    for c in s:
        if weight_table_dic.get(c) is None:
            count = 0
            for compare in s:
                if c == compare:
                    count += 1
                    weight_table_dic[c] = count
    return weight_table_dic


def create_bin_tree(left, right):
    # 左1，右0
    if not isinstance(left[0], Leaves):
        left_leaves = Leaves(left[0])
    else:
        left_leaves = left[0]
    if not isinstance(right[0], Leaves):
        right_leaves = Leaves(right[0])
    else:
        right_leaves = right[0]
    left_leaves.bin = '0'
    right_leaves.bin = '1'
    return left_leaves, right_leaves


def create_huffman_tree(weight_list):
    while not len(weight_list) == 1:
        tree = Leaves()
        tree.is_leaves = False
        tree.left, tree.right = create_bin_tree(weight_list[0], weight_list[1])
        weight_list.append((tree, weight_list[0][1] + weight_list[1][1]))
        weight_list.remove(weight_list[1])
        weight_list.remove(weight_list[0])
        weight_list.sort(key=lambda item: item[1], reverse=False)
    huffman_tree = weight_list[0][0]
    return huffman_tree


def get_huffman_code(tree, code, dic):
    tree.code = code + tree.bin
    if tree.is_leaves:
        dic[tree.data] = tree.code
    if tree.left is not None:
        get_huffman_code(tree.left, tree.code, dic)
    if tree.right is not None:
        get_huffman_code(tree.right, tree.code, dic)


def show_encoded(s, dic):
    for c in s:
        print(dic[c], end='')
    print()


if __name__ == '__main__':
    dic = {}
    s = input("输入字符串: ")
    weight_table = create_weight_table(s)
    weight_table = sorted(weight_table.items(), key=lambda item: item[1], reverse=False)
    print("Weight is :")
    print(weight_table)
    tree = create_huffman_tree(weight_table)
    get_huffman_code(tree, '', dic)
    print("Dictionary is :")
    print(dic)
    print("Encoded is :")
    show_encoded(s, dic)
