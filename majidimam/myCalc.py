while True:

        operator = input("Press any digit to continue or 'exit' to stop : ")

        if operator == "exit":
                print("Thank you for using this Calculator!")
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

                print("Please select operation -\n" \
		"1. Add (+)\n" \
		"2. Subtract (-)\n" \
		"3. Multiply (*)\n" \
		"4. Divide (\)\n")


                # Take input from the user
                select = int(input("Select operations form 1, 2, 3 and 4 :  "))

                if select == 1 :
                                
                            number_1=int(input("Enter first number  :  "))
                            number_2 = int(input("Enter second number:  "))
                            result = add(number_1, number_2)
                            print(number_1, "+", number_2, "=", result)
                            print("Select next operation -\n" \
		                        "1. Add\n" \
		                        "2. Subtract\n" \
                                        "3. Multiply\n" \
		                        "4. Divide\n")
                            select = int(input("Select operations form 1, 2, 3, 4 :  "))
                            if select == 1:
                                        number_3 = int(input("Enter any number: "))
                                        result2=add(result, number_3)
                                        print(result, "+", number_3, "=", result2 )

                            elif select == 2:
                                        number_3 = int(input("Enter any number: "))
                                        result2 = subtract(result, number_3)
                                        print(result, "-", number_3, "=", result2 )

                            elif select == 3:
                                         number_3 = int(input("Enter any number: "))
                                         result2=multiply(result, number_3)
                                         print(result, "*", number_3, "=", result2)

                            elif select == 4:
                                         number_3 = int(input("Enter any number: "))
                                         if number_3==0:
                                                      print(" Number not define")
                                         else : 
                                                      result2= divide(result, number_3)
                                                      print(result, "/", number_3, "=", result2)
                            else:
                                         print("Invalid input")


                elif select == 2:

                            number_1 = int(input("Enter first number: "))
                            number_2 = int(input("Enter second number: "))

                            result = subtract(number_1, number_2)
                            print(number_1, "-", number_2, "=", result)
                            print("Select next operation -\n" \
		                        "1. Add\n" \
		                        "2. Subtract\n" \
		                        "3. Multiply\n" \
		                        "4. Divide\n")
                            select = int(input("Select operations form 1, 2, 3, 4 :  "))
                            if select == 1:
                                    number_3 = int(input("Enter any number: "))
                                    result2= add(result, number_3)
                                    print(result, "+", number_3, "=", result2)

                            elif select == 2:

                                    number_3 = int(input("Enter any number: "))
                                    result2=subtract(result, number_3)
                                    print(result, "-", number_3, "=", result2)

                            elif select == 3:

                                     number_3 = int(input("Enter any number: "))
                                     result2=multiply(result, number_3)
                                     print(result, "*", number_3, "=", result2 )

                            elif select == 4:

                                     number_3 = int(input("Enter any number: "))
                                     if number_3==0:
                                              print(" Number not define")
                                     else :
                                             result2=divide(result, number_3)
                                             print(result, "/", number_3, "=", result2 )
                         
                            else:
                                     print("Invalid input")


                elif select == 3:

                            number_1 = int(input("Enter first number: "))
                            number_2 = int(input("Enter second number: "))
                            result = multiply(number_1, number_2)
                            print(number_1, "*", number_2, "=", result)
                            print("Select next operation -\n" \
		                        "1. Add\n" \
		                        "2. Subtract\n" \
		                        "3. Multiply\n" \
		                        "4. Divide\n")
                            select = int(input("Select operations form 1, 2, 3, 4 :  "))
                            if select == 1:
                                        number_3 = int(input("Enter any number: "))
                                        result2=add(result, number_3)
                                        print(result, "+", number_3, "=", result2)

                            elif select == 2:

                                        number_3 = int(input("Enter any number: "))
                                        result2=subtract(result, number_3)
                                        print(result, "-", number_3, "=", result2)

                            elif select == 3:

                                         number_3 = int(input("Enter any number: "))
                                         result2=multiply(result, number_3)
                                         print(result, "*", number_3, "=", result2)

                            elif select == 4:

                                          number_3 = int(input("Enter any number: "))
                                          if number_3==0:
                                                      print(" Number not define")
                                          else :
                                                      result2=divide(result, number_3)
                                                      print(result, "/", number_3, "=", result2)
                            else:
                                         print("Invalid input")


                elif select == 4:

                            number_1 = int(input("Enter first number: "))
                            number_2 = int(input("Enter second number: "))
                            result = divide(number_1, number_2)
                            print(number_1, "/", number_2, "=", result)
                            print("Select next operation -\n" \
		                        "1. Add\n" \
		                        "2. Subtract\n" \
		                        "3. Multiply\n" \
		                        "4. Divide\n")
                            select = int(input("Select operations form 1, 2, 3, 4 :  "))
                            if select == 1:
                                        number_3 = int(input("Enter any number: "))
                                        result2 =  add(result, number_3)
                                        print(result, "+", number_3, "=", result2)

                            elif select == 2:

                                        number_3 = int(input("Enter any number: "))
                                        result2= subtract(result, number_3)
                                        print(result, "-", number_3, "=", result2)

                            elif select == 3:

                                         number_3 = int(input("Enter any number: "))
                                         result2 = multiply(result, number_3)
                                         print(result, "*", number_3, "=", result2)

                            elif select == 4:

                                         number_3 = int(input("Enter any number: "))
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
                my_object = calculator()
                print("Current result : ", result2)
                my_object.reset()
                print("After Reset, Current Value : ",my_object.current_value)



