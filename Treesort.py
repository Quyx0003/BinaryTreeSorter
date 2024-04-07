import sys
from DictBinTree import DictBinTree  

def main():
    T = DictBinTree()  
    for line in sys.stdin:  
        num = int(line.strip())  
        T.insert(num) 

    sorted_numbers = T.orderedTraversal()  
    for num in sorted_numbers:  
        print(num)  

if __name__ == "__main__":
    main()  

