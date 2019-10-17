import sys
import time

test_case = int(sys.argv[1])

result = []

def test_time():
    start = time.time()
    input("RAPIDO, digite a palavra desejada: ")
    finish = time.time()
    return finish - start

print(f"seram feitas {test_case} iterações.")
while test_case > 0:
    input("Pressione Enter começar o caso de teste")
    tempo_digitanto = test_time()
    result.append(round(tempo_digitanto, 2))
    test_case -= 1

print(result)