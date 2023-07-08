# Hi this is Shahin Asadi author of this module

# This is a module for converting numbers from digit to text in persian and
# vise versa convert persian text to numbers

# this is just an exercising and not a serious project, so you can use, change
# and modify for your use-case


numbers = {
    'نومدسیلیون': 10 ** 60, 'اُکتودسیلیون': 10 ** 57, 'سپتدسیلیون': 10 ** 54,
    'سیکسدسیلیون': 10 ** 51, 'کویندسیلیون': 10 ** 48,
    'کواتیوردسیلیون': 10 ** 45, 'تریدسیلیون': 10 ** 42, 'دیودسیلیون': 10 ** 39,
    'آندسیلیون': 10 ** 36, 'دسیلیون': 10 ** 33, 'نانیلیون': 10 ** 30,
    'اکتیلیون': 10 ** 27, 'سپتیلیون': 10 ** 24, 'سیکستیلیون': 10 ** 21,
    'کوینتیلیون': 10 ** 18, 'کوادریلیون': 10 ** 15, 'تریلیون': 10 ** 12,
    'میلیارد': 10 ** 9, 'میلیون': 10 ** 6, 'هزار': 10 ** 3,
}

yekan = {
    'نه': 9, 'هشت': 8, 'هفت': 7, 'شش': 6, 'پنج': 5, 'چهار': 4, 'سه': 3,
    'دو': 2, 'یک': 1,
}

dahgan = {
    'نود': 90, 'هشتاد': 80, 'هفتاد': 70, 'شصت': 60, 'پنجاه': 50, 'چهل': 40,
    'سی': 30, 'بیست': 20, 'ده': 10,
}

yk_dg_combine = {
    'یازده': 11, 'دوازده': 12, 'سیزده': 13, 'چهارده': 14, 'پانزده': 15,
    'شانزده': 16, 'هفده': 17, 'هجده': 18, 'نوزده': 19
}

sadgan = {
    'نه صد': 900, 'هشتصد': 800, 'هفتصد': 700, 'ششصد': 600, 'پانصد': 500,
    'چهارصد': 400, 'سیصد': 300, 'دویست': 200, 'صد': 100,
}


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
def le_sadgan(text):
    import re
    text = gt_sadgan(text)[1]
    total = 0
    for item in yekan.keys():
        regex = re.search(f'{item} $', text)
        if regex:
            _yekan = yekan[item]
            total += _yekan
    for item in dahgan.keys():
        if re.search(f'{item}', text):
            _dahgan = dahgan[item]
            total += _dahgan
    for item in sadgan.keys():
        if item in text:
            _sadgan = sadgan[item]
            total += _sadgan
    return total


# mix two calculate numbers bigger and less than thousand
def total_num(text):
    num_1 = gt_sadgan(text)[0]
    num_2 = le_sadgan(text)
    final_num = num_1 + num_2
    return final_num


# return persian text to rial numbers 
def total_rial_num(text, to_file: str = None) -> int:
    final_num = total_num(text)
    rial_num = final_num * 10
    if to_file is None:
        return rial_num
    with open(file=to_file, mode='a') as file:
        file.write(f"{rial_num} Rial\n")


# return persian text to toman numbers 
def total_toman_num(text, to_file: str = None) -> int:
    if to_file is None:
        return total_num(text)
    with open(file=to_file, mode='a') as file:
        file.write(f"{total_num(text)} Toman\n")


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


def total_to_persian_toman(number: str, to_file: str = None) -> str:
    result = total_to_persian(number)
    if to_file is None:
        return result + ' تومان '
    with open(file=to_file, mode='a') as file:
        file.write(f"{result}  تومان \n")


def total_to_persian_rial(number: str, to_file: str = None) -> str:
    number += '0'
    result = total_to_persian(number)
    if to_file is None:
        return result + ' ریال '
    with open(file=to_file, mode='a') as file:
        file.write(f"{result}  ریال \n")
