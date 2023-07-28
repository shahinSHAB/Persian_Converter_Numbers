
# HOW TO USE THIS FUNCTIONS


**notice:** for all following functions you can set **`to_file`** as your filename to export output in it.

<details>
<summary><p style='color:blue;'>total_toman_num(text: str, to_file: str)</p></summary>

```python
total_toman_num('یک میلیارد و صد و دوازده میلیون و هشتاد و سه هزار و سیصد و پنجاه و هفت تومان')
# output in toman is: 1112083357
```
```python
total_toman_num('یک میلیارد و صد و دوازده میلیون و هشتاد و سه هزار و سیصد و پنجاه و هفت تومان', 'my_file.txt')
# output in toman is: 1112083357 write to my_file.txt file
```
</details>

<details>
<summary><p style='color:blue;'>total_rial_num(text: str, to_file: str)</p></summary>

```python
total_rial_num('صد و یک میلیون و نه صد و شصت و سه هزار و سی و سه تومان')
# output in rial is: 1019630330
```
```python
total_rial_num('صد و یک میلیون و نه صد و شصت و سه هزار و سی و سه تومان', 'my_file.txt')
# output in rial is: 1019630330 write to my_file.txt file
```
</details>

<details>
<summary><p style='color:blue;'>total_to_persian_toman(number: str, to_file: str)</p></summary>

```python
total_to_persian_toman('20123486057')
# output in toman is: بیست میلیارد و صد و بیست و سه میلیون و چهارصد و هشتاد و شش هزار و پنجاه و هفت تومان
```
```python
total_to_persian_toman('20123486057', 'my_file.txt')
# output in toman is: بیست میلیارد و صد و بیست و سه میلیون و چهارصد و هشتاد و شش هزار و پنجاه و هفت تومان write to my_file.txt file
```
</details>

<details>
<summary><p style='color:blue;'>total_to_persian_rial(number: str, to_file: str)</p></summary>

```python
total_to_persian_rial('124365478')
# output rial is: یک میلیارد و دویست و چهل و سه میلیون و ششصد و پنجاه و چهار هزار و هفتصد و هشتاد ریال
```
```python
total_to_persian_rial('124365478', 'my_file.txt')
# output rial is: یک میلیارد و دویست و چهل و سه میلیون و ششصد و پنجاه و چهار هزار و هفتصد و هشتاد ریال write to my_file.txt file
```
</details>