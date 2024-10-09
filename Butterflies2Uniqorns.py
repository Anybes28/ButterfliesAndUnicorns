import os

script_dir = os.path.dirname(__file__)

pattern = "nftset=/repVal/4#inet#fw4#vpn_domains"

def main():
    
    resultArray = []
    resultFile = open(script_dir + "\\Uniqorns.lst", "r")
    for line in resultFile:
        line=line.strip()
        resultArray.append(line)
    resultFile.close()

    file = open(script_dir + "\\Butterflies.txt", "r")
    for line in file:
        line=line.strip()
        value = pattern
        value= value.replace("repVal", line)
        if value in resultArray:
            continue
        resultArray.append(value)
        
    file.close()

    resultString = "\n".join(resultArray)

    resultFile = open(script_dir + "\\Uniqorns.lst", "w")
    resultFile.write(resultString)
    resultFile.close()
    print("Complete")

   
    


    
       


if __name__ == "__main__":
    main()