from questions import QUESTIONS


def isAnswerCorrect(question, ans):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''

    return True if question["answer"]==ans else False


def lifeLine(ques):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''
    import random
    count=0
    while count<=2:
        temp=random.randint(1,4)
        if ques["answer"]!=temp:
            temp="option" + str(temp)
            ques["temp"]=""
            count+=1
    return ques


def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
    print("Welcome to KBC!")
    ques_count=0
    prize_money=0
    lifeline_used=False
    min_reward=0
    while ques_count<15:
        print(f'\tQuestion {ques_count+1}: {QUESTIONS[ques_count]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[ques_count]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[ques_count]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[ques_count]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[ques_count]["option4"]}')
        ans = input('Your choice ( 1-4 ) : ')
        if(ans.lower()=="quit"):
            break

        if(ans.lower()=="lifeline" and ques_count!=14 and lifeline_used==False):
            question=lifeLine(QUESTIONS[ques_count])
            print(f'\tQuestion {ques_count+1}: {QUESTIONS[ques_count]["name"]}' )
            print(f'\t\tOptions:')
            print(f'\t\t\tOption 1: {QUESTIONS[ques_count]["option1"]}')
            print(f'\t\t\tOption 2: {QUESTIONS[ques_count]["option2"]}')
            print(f'\t\t\tOption 3: {QUESTIONS[ques_count]["option3"]}')
            print(f'\t\t\tOption 4: {QUESTIONS[ques_count]["option4"]}')
            ans = input('Your choice ( 1-4 ) : ')
        
        try:
            int(ans)
        except:
            print("Invalid Input!")
            continue

    # check for the input validations

        if isAnswerCorrect(QUESTIONS[ques_count], int(ans) ):
            if(ques_count==4):
                min_reward=10000
            elif(ques_count==10):
                min_reward=320000
            prize_money+=QUESTIONS[ques_count]["money"]
            print('\nCorrect !')

        else:
            prize_money=min_reward
            print('\nIncorrect !')
            break

        ques_count+=1
    print("Amount you won : " , prize_money)

    # print the total money won in the end.


kbc()
