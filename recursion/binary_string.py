def BinaryString(numberOfBits):
    if numberOfBits==0: return []
    if numberOfBits==1: return ["0", "1"]
    return (AddToList("0", BinaryString(numberOfBits-1))+AddToList("1", BinaryString(numberOfBits-1)))

def AddToList(bitOne, bitArray):
    return [bitOne+bit for bit in bitArray]

numberOfBits = int(input("Digite a quantidade de bits: "))
print(BinaryString(numberOfBits))
