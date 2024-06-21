'''
Leetcode - Two Sum

Explicação:
O algoritmo percorre a lista nums uma vez, 
armazenando no dicionário hasher os complementos necessários para atingir o target 
(ou seja, target - i para cada i na lista).
Se, durante a iteração, encontrar um número que já está no dicionário, 
significa que esse número e o número atual somam target, 
e então retorna os índices desses dois números. 
Isso é eficiente, pois utiliza um único loop (O(n) tempo) 
e espaço adicional proporcional ao tamanho da lista nums (O(n) espaço).
'''

#Solução

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasher = {}
        for idx, i in enumerate(nums):
            if hasher.get(i) is not None:
                return[hasher.get(i), idx]
            hasher[target-i] = idx