# Author -> Shahin Asadi

# This is a module for converting numbers from digit to text in persian and
# vise versa convert persian text to numbers

# this is just an exercising and not a serious project, so you can use, change
# and modify for your use-case
from utils import total_num, total_to_persian, le_sadgan, gt_sadgan


# return persian text to rial numbers
def total_rial_num(text: str, to_file: str = None) -> int:
    final_num = total_num(text)
    rial_num = final_num * 10
    if to_file is None:
        return rial_num
    with open(file=to_file, mode='a') as file:
        file.write(f"{rial_num} Rial\n")


# return persian text to toman numbers
def total_toman_num(text: str, to_file: str = None) -> int:
    if to_file is None:
        return total_num(text)
    with open(file=to_file, mode='a') as file:
        file.write(f"{total_num(text)} Toman\n")


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


# Some Examples -->
example_1 = total_toman_num('یک میلیارد و صد و دوازده میلیون و هشتاد و سه هزار و سیصد و پنجاه و هفت تومان')
example_2 = total_rial_num('صد و یک میلیون و نه صد و شصت و سه هزار و سی و سه تومان')
example_3 = total_to_persian_toman('20123486057')
example_4 = total_to_persian_rial('124365478')

print(example_1)
# output toman is: 1112083357
print(example_2)
# output rial is: 1019630330
print(example_3)
# output toman is: بیست میلیارد و صد و بیست و سه میلیون و چهارصد و هشتاد و شش هزار و پنجاه و هفت تومان
print(example_4)
# output rial is: یک میلیارد و دویست و چهل و سه میلیون و ششصد و پنجاه و چهار هزار و هفتصد و هشتاد ریال
