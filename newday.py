import os

item = "01"

os.mkdir("./Day" + item)
open("./Day" + item + "/input.txt", "w").close()
open("./Day" + item + "/input_easy.txt", "w").close()

main = open("./Day" + item + "/main.py", "w")
main.write('def main(test=False):\n\trows = open("input_easy.txt").read()\n\tif not test:')
main.write('\n\t\trows = open("input.txt").read()\n\n\nif __name__ == \'__main__\':\n\tmain(True)\n')
main.close()
