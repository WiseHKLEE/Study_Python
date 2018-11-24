#relative Package : sound Package 사용하기 위해 from 뒤에 ..(부모 디텍토리) 입력하여 relative하게 import
#from graphic.render import echo_test 와 아래는 동일
from ..sound.echo import echo_test

def render_test():
    print("render")
    echo_test()