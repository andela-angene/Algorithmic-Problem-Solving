# a = {
#     'a': 3
# }
#
# try:
#     a['a']
#     print('done')
# except:
#     print('ok')

st = 'slkdjf [split] lsdfjklsdf <br> [split]'

st = st.replace('<br>', '<br />').split('[split]')
result = ''
for item in st:
    item = item.strip()
    if item:
        result += '<a>%s</a>' %item

print(result)
