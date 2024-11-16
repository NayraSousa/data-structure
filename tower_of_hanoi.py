def TowerOfHanoi(numberOfDisks, initialHook=1, auxiliaryHook=2, finalHook=3):
    if numberOfDisks==1:
        print(f"Mover o disco 1 da torre {initialHook} para a torre {finalHook}")
        return 
    TowerOfHanoi(numberOfDisks-1, initialHook, finalHook, auxiliaryHook)
    print(f"Mover o disco {numberOfDisks} da torre {initialHook} para a torre {finalHook}")
    TowerOfHanoi(numberOfDisks-1, auxiliaryHook, initialHook, finalHook)

numberOfDisks = int(input("Digite a quantidade de discos: "))
TowerOfHanoi(numberOfDisks)