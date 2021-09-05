new_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for n, i in enumerate(new_list):
    if i.isdigit():
        new_list[n] = f'"{i.zfill(2)}"'
    elif i[1:].isdigit():
        new_list[n] = f'"{i[0]}{i[1:].zfill(2)}"'

print(' '.join(new_list))
