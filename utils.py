from constants import (
    numbers, dahgan, sadgan,
    yekan, yk_dg_combine
)


def raw_number(txt):
    txt = txt.replace('تومان', '')
    return txt


# calculate and convert every three digit number from persian text to number
# for numbers that bigger than thousand
def gt_sadgan(text):
    txt = raw_number(text)
    total = 0
    for item in numbers.keys():
        if txt and item in txt:
            ls_txt = txt.split(item)
            if ' و' in ls_txt[0]:
                sub_ls = ls_txt[0].split(' و ')
            else:
                sub_ls = ls_txt[0].split(' ')
            sum_num = 0
            for n_item in sub_ls:
                n_item = n_item.strip()
                _sadgan = _dahgan = _yekan = 0
                if n_item in sadgan.keys():
                    _sadgan = sadgan[n_item]
                    sum_num += _sadgan
                elif n_item in dahgan.keys():
                    _dahgan = dahgan[n_item]
                    sum_num += _dahgan
                elif n_item in yk_dg_combine.keys():
                    _yk_dg_comb = yk_dg_combine[n_item]
                    sum_num += _yk_dg_comb
                elif n_item in yekan.keys():
                    _yekan = yekan[n_item]
                    sum_num += _yekan
            total_num = sum_num * numbers[item]
            total += total_num
            ls_txt.pop(0)
            new_txt = ls_txt[0]
            txt = new_txt
    return total, txt


# calculate and convert every three digit number from persian text to number
# for numbers that less than thousand
def le_sadgan(text: str):
    txt = text.strip()
    total = 0
    flag = False
    ls = txt.split('و')
    lst = [item.strip() for item in ls if item]
    for item in sadgan.keys():
        if item == lst[0]:
            total += sadgan[item]
            lst.pop(0)
    for item in yk_dg_combine.keys():
        for word in lst:
            if item == word:
                total += yk_dg_combine[item]
                flag = True
    if not flag:
        for item in dahgan.keys():
            for word in lst:
                if item == word:
                    total += dahgan[item]
                    lst.remove(word)
        if lst:
            for item in yekan.keys():
                for word in lst:
                    if item == word:
                        total += yekan[item]
                        lst.remove(word)
    return total


# mix two calculate numbers bigger and less than thousand
def total_num(text):
    num_1, text_2 = gt_sadgan(text)
    num_2 = le_sadgan(text_2)
    final_num = num_1 + num_2
    return final_num


def yekan_to_persian(number: str) -> str | None:
    if (len(number) == 1) and (number != '0'):
        for k, v in yekan.items():
            if v == int(number):
                return k
    elif (len(number) == 1) and (number == '0'):
        return None


def dahgan_to_persian(number: str) -> str | None:
    if (len(number) == 2) and (number[0] != '0'):
        for k, v in yk_dg_combine.items():
            if v == int(number):
                return k
        for k, v in dahgan.items():
            if v // 10 == int(number[0]):
                return k
    elif (len(number) == 2) and (number[0] == '0'):
        return None


def sadgan_to_persian(number: str) -> str | None:
    if (len(number) == 3) and (number[0] != '0'):
        for k, v in sadgan.items():
            if v // 100 == int(number[0]):
                return k
    elif (len(number) == 3) and (number[0] == '0'):
        return None


def mix_of_placement_to_persian(number: str) -> str:
    flag = True
    if len(number) == 3:
        sd_result = sadgan_to_persian(number) if \
            sadgan_to_persian(number) is not None else ''
        number = number[1:]
    else:
        sd_result = ''
    if len(number) == 2:
        if number[0] == '1':
            flag = False
        if sd_result:
            dg_result = ' و ' + dahgan_to_persian(number) if \
                dahgan_to_persian(number) is not None else ''
        else:
            dg_result = dahgan_to_persian(number) if \
                dahgan_to_persian(number) is not None else ''
        number = number[1:]
    else:
        dg_result = ''
    if len(number) == 1 and flag:
        if sd_result or dg_result:
            yk_result = ' و ' + yekan_to_persian(number) if \
                yekan_to_persian(number) is not None else ''
        else:
            yk_result = yekan_to_persian(number) if \
                yekan_to_persian(number) is not None else ''
    else:
        yk_result = ''
    return sd_result + dg_result + yk_result


def total_to_persian(number: str) -> str:
    num_div, num_mod = divmod(len(number), 3)
    lst_number_placement = []
    a, b = 0, 3
    if num_mod == 0:
        for _ in range(num_div):
            lst_number_placement.append(number[a:b])
            a, b = b, b + 3
    else:
        b = num_mod + 3
        lst_number_placement.append(number[a:num_mod])
        for _ in range(num_div):
            lst_number_placement.append(number[num_mod:b])
            num_mod, b = b, b + 3

    if len(lst_number_placement) == 1:
        return mix_of_placement_to_persian(number)
    else:
        first_cycle = True
        new_numbers = {v: k for k, v in numbers.items()}
        cp_placement_number = lst_number_placement.copy()
        result = ''
        lst_len = len(lst_number_placement) - 1
        for _ in range(len(lst_number_placement) - 1):
            if (num := cp_placement_number.pop(0)) != '000':
                if first_cycle:
                    result += mix_of_placement_to_persian(num) \
                            + ' ' + new_numbers[10 ** (3 * lst_len)]
                else:
                    result += ' و ' + mix_of_placement_to_persian(num) \
                            + ' ' + new_numbers[10 ** (3 * lst_len)]
            first_cycle = False
            lst_len -= 1
            if lst_len < 1:
                break
        if cp_placement_number[-1] != '000':
            result += ' و ' + mix_of_placement_to_persian(
                cp_placement_number[-1])
        return result
