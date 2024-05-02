import argparse
import sys
import os
import glob
import stat
from datetime import datetime

def get_latest_file(path):
    list_of_files = glob.glob(path + '/*')
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file


def main():
    if (len(sys.argv) == 1):
        x = 0
        while (x != 3):
            if (x < 1):
                line1 = input("What do you want to achieve today on your computer ?\n")
                if not line1.strip():
                    print("Please write something !")
                    continue
                else:
                    x = 1
            if (x < 2):
                line2 = input("What did you achieve yesterday ?\n")
                if not line2.strip():
                    print("Please write something !")
                    continue
                else:
                    x = 2
            if (x < 3):
                line3 = input("What grade would you give your productivity for yesterday\n")
                if not line3.strip():
                    print("Please write something !")
                    continue
                if not line3.strip().isdigit() or not 0 <= int(line3.strip()) <= 10:
                    print("Please enter a number between 0 and 10!")
                    continue
                else:   
                    x = 3
            
        now = datetime.now()
        date_str = f"{now.year}_{now.month}_{now.day}"
        formatted_message = f"Today's date: {date_str}\n\nWhat do you want to achieve today on your computer ?\n{line1}\nWhat did you achieve yesterday  ?\n{line2}\nWhat grade would you give your productivity for yesterday\n{line3}"
        if not os.path.exists('./exnihilolog/'):
            os.makedirs('./exnihilolog/')
        
        with open("./exnihilolog/"+date_str+".txt", 'w') as f:
            f.write(formatted_message + '\n')
    else:
        file = get_latest_file("./exnihilolog")
        while True:
            line4 = input("Did you do a bit of leetcode today? (yes/no) \n").lower()
            if line4 in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        line5 = input("Tell me something you ve learned today !\n")
        with open (file, 'a') as f:
            f.write("Did you do a bit of leetcode today? (yes/no) \n" + line4 + "\n")
            f.write("Tell me something you ve learned today !\n" + line5 + "\n")
            f.write("\n\nYou're on the right path continue\n")
        os.chmod(file, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
        print("File is now sealed \n")



if __name__ == "__main__":
    main()