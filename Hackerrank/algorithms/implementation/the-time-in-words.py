hour, mins = int('5'), int('47')

number_list = ["zero","one","two","three","four","five","six","seven","eight","nine"]
teen_list = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
decades_list =["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]


def convert_to_word(n):
    if n < 10:
        return number_list[n]
