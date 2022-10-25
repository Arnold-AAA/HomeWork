print("Welcome to the scholarship calculator student! \nBefore we can calculate your scholarship, you will need to enter some details. Дet's start!")
studen_name=input("Please enter your name: ").capitalize()
if studen_name.isnumeric():
	print("Please use only alphabet") # make sure student entering alphabet name and also add capitalize to input to avoid mistakes
	exit()
student_birthday=input("Please enter your date of birthday. DD/MM/YYYY: ") # DD = [0,1]  MM[3.4] YYYY[6,7,8,9]
if student_birthday.isalpha() or len(student_birthday) <= 9 or len(student_birthday) >= 11: # make sure student entering date of birthday in correct format
	print("Wrong date of birth. Please use only numbers and make sure you enter your birthday in the correct form. Example 01/02/1234")
	exit()
student_sex=input("Please enter your gender (Man or Woman): ").capitalize() # capitalize to avoid mistakes
if student_sex.isnumeric() or len(student_sex) >= 5:
	print("Please use only alphabet") # if student used numbers program will close
	exit()
studen_ID=input("Please enter your ID code: ")
if studen_ID[-1].isalpha() or studen_ID[-2].isalpha() or studen_ID[-3].isalpha() or studen_ID[-4].isalpha() or studen_ID[-5].isalpha() or studen_ID[-6].isalpha() or studen_ID[-7].isalpha() or studen_ID[-8].isalpha() or studen_ID[-9].isalpha() or studen_ID[-10].isalpha() or studen_ID[-11].isalpha():
	print(f"{studen_name}, please use only numbers") # idk how to make this line shorter, but this one works. here i want make sure student entering only numbers
	exit() # if student enter some alphabet symbols, program will close
else:
	studen_ID [0] == 3 or 4 or 5 or 6 # 3 - man born in
	print("Correct ID code. This code exist.")
	if student_birthday[0:1] == studen_ID [5:6] and student_birthday[8:9] == studen_ID[1:2] and student_birthday[3:4] == studen_ID[3:4]:
		print("Date of birthday matches with student ID code.")
	else:
		student_birthday[0:1] != studen_ID[5:6] and student_birthday[8:9] != studen_ID[1:2] and student_birthday[3:4] != studen_ID[3:4]
		print(f"Sorry {studen_name}.Date of birthday not matches with student ID code.")
		exit() # compare birthday date and student ID
	if student_sex == "Man" and studen_ID[0] == "3" or studen_ID[0] == "5":
		print("ID code and gender match. You are man.")  # if student enter sex man and ID code also show that system says all correct
	elif student_sex == "Woman" and studen_ID[0] == "4" or studen_ID[0] == "6":
		print("ID code and gender match. You are woman.")
		#compare sex with id code
	else:
		print("Your ID code and gender you entered before not matches")
		exit()
	school_fees = int(input("Please enter your school fees (Euro): "))
	print(f"{studen_name} Enter your grades below (min 5 grades). The system will ask you to enter grades until you are done.\nTo exit enter 0.")
	loop_scores = -1
	student_estimates = 0
	while student_estimates >= 0:
		loop_scores += 1
		student_input = int(input(f"{studen_name}, please enter one grade here, from 1 to 5: "))
		student_estimates += student_input
		if student_input >=6:
			print("Please use number from 1 too 5 only.")
			exit()
		elif student_input == 1 or student_input == 2 or student_input == 3 or student_input == 4 or student_input == 5:  # if n is 4, end the loop
			continue
		else:
			break
	GPA = student_estimates / loop_scores # sum all student estimates and divide by every estimate > getting GPA
	GPA_round = round(GPA) # round GPA
	print(f"Your GPA score is {GPA_round}")
	if GPA_round == 5:
		student_grade_5 = school_fees * 0.4  # 40 % from school fees
		print(f"{studen_name}, your scholarship: {int(student_grade_5)} Euro. 40% from school fees. Great job!")
	elif GPA_round == 4:
		student_grade_4 = school_fees * 0.3 # 30 % from school fees
		print(f"{studen_name}, your scholarship: {int(student_grade_4)} Euro. 30% from school fees. Good job!")
	elif GPA_round == 3:
		student_grade_3 = school_fees * 0.2 # 20 % from school fees
		print(f"{studen_name}, your scholarship: {int(student_grade_3)} Euro. 20% from school fees. Not bad!")
	elif GPA_round == 1:
		student_grade_1 = school_fees * 0.1 # 10 % from school fees
		print(f"{studen_name}, your scholarship: {int(student_grade_1)} Euro. 10% from school fees.")
		# Student can get max scholarship 40% from his school fee