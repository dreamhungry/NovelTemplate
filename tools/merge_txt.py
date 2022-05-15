# coding=utf-8
import os

def MergeAllTxtFiles(input_path, output_path):
    for root, dirs, files in os.walk(input_path):
        for d in dirs:
            content = []
            for r, ds, fs in os.walk(os.path.join(root, d)):
                for f in fs:
                    with open(os.path.join(r, f), "rt", encoding="utf-8") as fp:
                        content += fp.readlines()
                        content.append("\r\n")
            output = os.path.join(root, "%s.txt"%d)
            with open(output, "w+", encoding="utf-8") as fp:
                fp.writelines(content)


if __name__ == "__main__":
    input = "./"
    output = "./"
    MergeAllTxtFiles(input, output)
    
