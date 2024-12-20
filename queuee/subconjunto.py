from collections import deque

def gerar_subconjuntos(nums):

    fila = deque([[]])

    for num in nums:
        tamanho = len(fila)
        
        for _ in range(tamanho):
            subconjunto = fila.popleft()
            
            fila.append(subconjunto)
            fila.append(subconjunto + [num])
    
    for subconjunto in fila:
        print(subconjunto)

gerar_subconjuntos([1, 2, 3])