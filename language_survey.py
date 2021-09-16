from survey import AnnonymousSurvey

# Определение вопроса с созданием экземпляра AnnonymousSurvey.
question = "What language did you first learn to speak?"
my_survey = AnnonymousSurvey(question)

# Вывод вопроса и сохранение ответов.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
	response = input("Language: ")
	if response == 'q':
		break
	my_survey.store_response(response)

# Вывод результатов опроса.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
