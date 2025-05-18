#import tools
##from tools import calculate_bmi, get_state
#import edu
#from edu . tools import calculate_bmi, get_state
#from edu import tools
from edu . tools import calculate_bmi as a
from edu . tools import get_state as b

def main():
    try:
        hight: int = int (input("請輸入您的身高(120~220cm間)"))
        weight: int = int (input("請輸入您的體重(30~200kg間)"))
        bmi = a(hight,weight)
        
    except ValueError:
        print("輸入格式錯誤")
    except Exception as e:
        print(e)
    else:    
        print(f"身高(公分):{hight}")
        print(f"體重(公斤):{weight}")
        print(f"bmi{bmi:.1f}")
        print(b(bmi))
         
    print("應用程式結束")
#內建變數
if __name__ == "__main__":
    main()