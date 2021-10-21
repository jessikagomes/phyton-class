nums = [1,2,3]

print(f'Esse eh o timo de variavel: {type(nums)}')

nums.append(3)
print(f'O tamanho da lista eh: {len(nums)}')

nums[2] = 100
print(f'Essa eh a lista atualizada {nums}')

nums.insert(0,-200)
print(f'Essa eh a lista apos inserior -200 no indice 0: {nums}')

print(f'Mostrando oindice 4: {nums[4]}')
print(f'O ultimo elemento da lista eh: {nums[-1]}')