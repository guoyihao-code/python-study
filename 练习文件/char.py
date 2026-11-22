import argparse
import sys
def cnt_word(path:str)->dict:
    total_lines=0
    valid_lines=0
    chars=0
    try:
        with open(path,"r",encoding="utf-8") as f:
            for line in f:
                total_lines+=1
                chars+=len(line)
                if line.strip():
                    valid_lines+=1
    except FileNotFoundError:
        print("文件不存在")
        sys.exit(1)
    except PermissionError:
        print("文件没有权限")
        sys.exit(1)
    except UnicodeDecodeError:
        print("文件编码不对")
        sys.exit(1)
    except Exception as e:
        print(f"错误:{e}")
        sys.exit(1)
    return {"total_lines": total_lines, "valid_lines": valid_lines, "chars": chars}
if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-m",default="lines",choices=["lines","valid","chars"],help="请输入你的操作")
    parser.add_argument("file_path",)
    args=parser.parse_args()
    res=cnt_word(args.file_path)
    if args.m=="lines":
        print(res["total_lines"])
    elif args.m=="valid":
        print(res["valid_lines"])
    elif args.m=="chars":
        print(res["chars"])




