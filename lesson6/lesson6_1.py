def calculate_bmi(hight:int ,weight:int):
    if hight < 120 or hight > 220:
            raise Exception("未在規定範圍(120~220cm間)，請重新輸入") #自己身高raise錯誤
    if weight < 30 or weight > 200:
            raise Exception("未在規定範圍(30~200kg間)，請重新輸入") #自己體重raise錯誤
    
    bmicalculate = weight / (hight / 100) **2
    return bmicalculate

def main():
    try:
        hight: int = int (input("請輸入您的身高(120~220cm間)"))
        weight: int = int (input("請輸入您的體重(30~200kg間)"))
        bmi = calculate_bmi(hight,weight)
        
    except ValueError:
        print("輸入格式錯誤")
    except Exception as e:
        print(e)
    else:    
        print(f"身高(公分):{hight}")
        print(f"體重(公斤):{weight}")
        print(f"bmi{bmi:.1f}")
        
        if bmi>=27:
            print("太胖了，需要克制飲食與多運動")
        elif bmi>=24:
            print("過重，需要運動!")
        elif bmi<18.5:
            print("過輕，不要挑食多吃營養的食物")
        else:
            print("正常，太棒了!")
    print("應用程式結束")
#內建變數
if __name__ == "__main__":
    main()