while True:

        operator = input("Press any digit to continue or 'exit' to stop : ")

        if operator == "exit":
                print("Thank you for using this Calculator !")
                break
        else:
                # Python program for simple calculator

                # Function to add two numbers
                def add(num1, num2):
                            return num1 + num2

                # Function to subtract two numbers
                def subtract(num1, num2):
                            return num1 - num2

                # Function to multiply two numbers
                def multiply(num1, num2):
                            return num1 * num2

                # Function to divide two numbers
                def divide(num1, num2):
                        if num2==0:
                                return "Cannot divide by Zero"
                        return num1 / num2
                # Take input from the user
                number_1= int(input())
                select1= input()
                if select1 =='+' :
                            number_2 = int(input())
                            result = add(number_1, number_2)
                            print(number_1, "+", number_2, "=", result)
                            select2 =input()
                            if select2 =='+':
                                        number_3 = int(input())
                                        result2=add(result, number_3)
                                        print(result, "+", number_3, "=", result2 )

                            elif select2 =='-':
                                        number_3 = int(input())
                                        result2 = subtract(result, number_3)
                                        print(result, "-", number_3, "=", result2 )

                            elif select2 =='*':
                                         number_3 = int(input())
                                         result2=multiply(result, number_3)
                                         print(result, "*", number_3, "=", result2)

                            elif select2 =='/':
                                         number_3 = int(input())
                                         if number_3==0:
                                                      print(" Number not define")
                                         else : 
                                                      result2= divide(result, number_3)
                                                      print(result, "/", number_3, "=", result2)
                            else:
                                         print("Invalid input")


                elif select1 =='-':

                            number_2 = int(input())
                            result = subtract(number_1, number_2)
                            print(number_1, "-", number_2, "=", result)
                            select2 = input()
                            if select2 =='+':
                                    number_3 = int(input())
                                    result2= add(result, number_3)
                                    print(result, "+", number_3, "=", result2)

                            elif select2 =='-':
                                    number_3 = int(input())
                                    result2=subtract(result, number_3)
                                    print(result, "-", number_3, "=", result2)

                            elif select2 == '*':

                                     number_3 = int(input())
                                     result2=multiply(result, number_3)
                                     print(result, "*", number_3, "=", result2 )

                            elif select2 == '/':

                                     number_3 = int(input())
                                     if number_3==0:
                                              print(" Number not define")
                                     else :
                                             result2=divide(result, number_3)
                                             print(result, "/", number_3, "=", result2 )
                         
                            else:
                                     print("Invalid input")


                elif select1 =='*':

                            number_2 = int(input())
                            result = multiply(number_1, number_2)
                            print(number_1, "*", number_2, "=", result)
                            select2 =input()
                            if select2 =='+':
                                        number_3 = int(input())
                                        result2=add(result, number_3)
                                        print(result, "+", number_3, "=", result2)

                            elif select2 =='-':

                                        number_3 = int(input())
                                        result2=subtract(result, number_3)
                                        print(result, "-", number_3, "=", result2)

                            elif select2 =='*':

                                         number_3 = int(input())
                                         result2=multiply(result, number_3)
                                         print(result, "*", number_3, "=", result2)

                            elif select2 =='/':

                                          number_3 = int(input())
                                          if number_3==0:
                                                      print(" Number not define")
                                          else :
                                                      result2=divide(result, number_3)
                                                      print(result, "/", number_3, "=", result2)
                            else:
                                         print("Invalid input")


                elif select1 =='/':
                            number_2 = int(input())
                            result = divide(number_1, number_2)
                            print(number_1, "/", number_2, "=", result)
                            select2 = input()
                            if select2 == '+':
                                        number_3 = int(input())
                                        result2 =  add(result, number_3)
                                        print(result, "+", number_3, "=", result2)

                            elif select2 == '-':

                                        number_3 = int(input())
                                        result2= subtract(result, number_3)
                                        print(result, "-", number_3, "=", result2)

                            elif select2 == '*':

                                         number_3 = int(input())
                                         result2 = multiply(result, number_3)
                                         print(result, "*", number_3, "=", result2)

                            elif select2 == '/':

                                         number_3 = int(input())
                                         if number_3==0:
                                                      print(" Number not define")
                                         else :
                                                      result2=divide(result, number_3)
                                                      print(result, "/", number_3, "=", result2)
                            else:
                                         print("Invalid input")

                else:
                            print("Invalid input")
                class calculator:
                            def __init__(self):
                                            self.initial_value = 0
                                            self.current_value = self.initial_value
                            def reset(self):
                                            self.current_value= self.initial_value
                action=input("Please type 'Print' to print history and 'Reset' to clear  :")
                my_object = calculator()
                match action:
                        case 'print':
                                print(number_1,select1,number_2," = ",result)
                                print(result,select2,number_3," = ",result2)
                        case 'reset':
                                 my_object.reset()
                                 print("After Reset, Current Value : ",my_object.current_value)
                        case _:
                                print("Invalid output")
                                

                
                
               
