def calculate_bmi(hight:int ,weight:int):
    if hight < 120 or hight > 220:
            raise Exception("未在規定範圍(120~220cm間)，請重新輸入") #自己身高raise錯誤
    if weight < 30 or weight > 200:
            raise Exception("未在規定範圍(30~200kg間)，請重新輸入") #自己體重raise錯誤
    
    bmicalculate = weight / (hight / 100) **2
    return bmicalculate

def get_state(bmi:float):
    if bmi>=27:
        message = "太胖了，需要克制飲食與多運動"
    elif bmi>=24:
        massage = "過重，需要運動!"
    elif bmi<18.5:
        massage = "過輕，不要挑食多吃營養的食物"
    else:
        massage = "正常，太棒了!"
    return massage