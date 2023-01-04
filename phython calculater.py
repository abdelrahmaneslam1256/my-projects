#هنا انا بستدعي كتبة ماث
import math
#هنا انابعرف الفانكشن بتاعتي والي اسمها ران
def run ():
#هنا باخد اينبوت من اليوزر
     x= int(input("enter the first num : "))
     s = input("enter sympole X or / or+ or -: ") .lower()
#هنا انا لو حطيت كيو بيخرج من البرنامج
     if s == 'q':
        quit()
     y= int(input("enter the second num : "))
#هنا بتتكون كل العمليات
     if s == '*':
         print(x*y)
     elif s == '/':
         print(x/y)
     elif s == '+':
         print (x+y)
     elif s == '-':
         print (x-y)
    
#هنا انا بعمل لووب عشان البرنامج يفضل مسستمر لحد ما اليوسر يعمل اينبوت كيو
while True:
#هنا بستدعي الفانكشن بتاعي الي عملتها
     run()