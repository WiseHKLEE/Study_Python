dic = {'.-':'A', '-...':'B', '-.-.':'C','-..':'D','.':'E', '..-.':'F', '--.':'G', '....':'H',
       '..':'I', '.---':'J', '-.-':'K', '.-..':'L', '--':'M', '-.':'N', '---':'O', '.--.':'P',
       '--.-':'Q', '.-.':'R', '...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W', '-..-':'X',
       '-.--':'Y', '--..':'Z'}


def morse(n):
    result = []
    for word in n.split("  "): #split은 문자열은 특정 기준으로 나눠서 List에 넣어줌
        for chat in word.split(" "):
            result.append(dic[chat])
        result.append(" ")
    return ''.join(result)   #join은 split과는 반대의 개념으로 List값들을 특정 단어를 포함하여 합병시켜준다. 해당 코드에서는 null('')을 추가하였기 때문에 List로 된 값들이 문자열로 변환 됨



print(morse(".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--"))







