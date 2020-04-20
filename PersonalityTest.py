
assessment = [
    {"question":"Am the life of the party?", "type":1, "math":"+"},
    {"question":"Feel little concern for others.", "type":2, "math":"-"},
    {"question":"Am always prepared?", "type":3, "math":"+"},
    {"question":"Get stressed out easily.", "type":4, "math":"-"},
    {"question":"Have a rich vocabulary.", "type":5, "math":"+"},
    {"question":"Don't talk a lot.", "type":1, "math":"-"},
    {"question":"Am interested in people?", "type":2, "math":"+"},
    {"question":"Leave my belongings around.", "type":3, "math":"-"},
    {"question":"Am relaxed most of the time?", "type":4, "math":"+"},
    {"question":"Have difficulty understanding abstract ideas.", "type":5, "math":"-"},
    {"question":"Feel comfortable around people.", "type":1, "math":"+"},
    {"question":"Insult people.", "type":2, "math":"-"},
    {"question":"Pay attention to details.", "type":3, "math":"+"},
    {"question":"Worry about things.", "type":4, "math":"-"},
    {"question":"Have a vivid imagination.", "type":5, "math":"+"},
    {"question":"Keep in the background.", "type":1, "math":"-"},
    {"question":"Sympathize with others' feelings.", "type":2, "math":"+"},
    {"question":"Make a mess of things.", "type":3, "math":"-"},
    {"question":"Seldom feel blue.", "type":4, "math":"+"},
    {"question":"Am not interested in abstract ideas?", "type":5, "math":"-"},
    {"question":"Start conversations.", "type":1, "math":"+"},
    {"question":"Am not interested in other people's problems?", "type":2, "math":"-"},
    {"question":"Get chores done right away.", "type":3, "math":"+"},
    {"question":"Am easily disturbed?", "type":4, "math":"-"},
    {"question":"Have excellent ideas.", "type":5, "math":"+"},
    {"question":"Have little to say.", "type":1, "math":"-"},
    {"question":"Have a soft heart.", "type":2, "math":"+"},
    {"question":"Often forget to put things back in their proper place.", "type":3, "math":"-"},
    {"question":"Get upset easily.", "type":4, "math":"-"},
    {"question":"Do not have a good imagination.", "type":5, "math":"-"},
    {"question":"Talk to a lot of different people at parties.", "type":1, "math":"+"},
    {"question":"Am not really interested in others?", "type":2, "math":"-"},
    {"question":"Like order.", "type":3, "math":"+"},
    {"question":"Change my mood a lot.", "type":4, "math":"-"},
    {"question":"Am quick to understand things?", "type":5, "math":"+"},
    {"question":"Don't like to draw attention to myself.", "type":1, "math":"-"},
    {"question":"Take time out for others.", "type":2, "math":"+"},
    {"question":"Shirk my duties.", "type":3, "math":"-"},
    {"question":"Have frequent mood swings.", "type":4, "math":"-"},
    {"question":"Use difficult words.", "type":5, "math":"+"},
    {"question":"Don't mind being the center of attention.", "type":1, "math":"+"},
    {"question":"Feel others' emotions.", "type":2, "math":"+"},
    {"question":"Follow a schedule.", "type":3, "math":"+"},
    {"question":"Get irritated easily.", "type":4, "math":"-"},
    {"question":"Spend time reflecting on things.", "type":5, "math":"+"},
    {"question":"Am quiet around strangers?", "type":1, "math":"-"},
    {"question":"Make people feel at ease.", "type":2, "math":"+"},
    {"question":"Am exacting in my work?", "type":3, "math":"+"},
    {"question":"Often feel blue.", "type":4, "math":"-"},
    {"question":"Am full of ideas?", "type":5, "math":"+"}
]
numquestions = len(assessment)

introduction = "\n\nThis high-resolution description is one of the major advantages of this testing process and its statistical procedures, and it will provide you with a very detailed understanding of exactly who you are and how you are similar to and different from the other people around you. You might find it interesting to compare your report with that of the people you are close to: friends, intimate partners and family members. Doing so will help you understand why it is that you agree with some people, and disagree with others—even about fundamental truths. Personality differences, which are profoundly affected by basic biological factors, as well as lifetime experience, help determine such things as social behavior (loner vs socialite), political belief (highly open people are more liberal), work ethic (much stronger in conscientious people), interest in people vs things (agreeableness is associated with the former), and appreciation for art and literature (associated with openness). These differences are real, and can be very large. It is crucially important to understand yourself and other people so that you can better cope with the diversity of opinion and viewpoint that makes up the personal, familial and social world."

traits = "\n\nYou will receive information about your position along each of the Big Five dimensions of Extraversion (associated with positive emotion), Neuroticism (negative emotion), Agreeableness (the primary dimension of care for others), Conscientiousness (associated with duty, precision and responsibility) and Openness (interest in ideas and aesthetics), including customized descriptive paragraphs for your specific percentile positions. That five-dimensional description will be further expanded upon and developed for each of the ten aspects of the Big Five:\n\nExtraversion can be thought of as a combination of Enthusiasm (spontaneous joy and engagement) and Assertiveness (social dominance, often verbal in nature).\nNeuroticism can be though of as a combination of Withdrawal (the tendency to avoid in the face of uncertainty) and Volatility (the tendency to become irritable and upset when things go wrong.\nAgreeableness can be thought of as a combination of Compassion (the tendency to empathically experience the emotion of others) and Politeness (the proclivity to abide by interpersonal norms).\nConscientiousness can be thought of as a combination of Industriousness (the ability to engage in sustained, goal-directed effort) and Orderliness (the tendency to schedule, organize and systematize).\nOpenness to Experience can be thought of as a combination of Openness (creativity and aesthetic sensitivity) and Intellect (interest in abstract concepts and ideas; unrelated to IQ)."


helptext = "\n\nDescribe yourself as you generally are now, not as you wish to be in the future.\nDescribe yourself as you honestly see yourself, in relation to other people you know of the same sex as you are, and roughly your same age.\nSo that you can describe yourself in an honest manner, your responses will be kept in absolute confidence.\n\nIndicate for each statement which answer best fits as a description of you:\n1. Very Inaccurate\n2. Moderately Inaccurate\n3. Neither Accurate Nor Inaccurate\n4. Moderately Accurate\n5. Very Accurate\n\nOnce you have submitted your answer, you will be asked to type 'y' (or 'Y') to confirm it."
answerdescriptions = [
    "Strongly Disagree",
    "Somewhat Disagree",
    "Neither Agree or Disagree",
    "Somewhat Agree",
    "Strongly Agree"
]
typeScores = [0,0,0,0,0]
questionnum = 0
print("Welcome to the Big Five Aspect Scale Personality Test!\nProgrammed in Python by Stephen Emmons and Marcus Wren\n"+str(questionnum)+" Total Questions\n")
print(introduction)
print(traits)
print(helptext)

print("\n\nType a number 1-5 to represent your answer. Type 'help' to see this information again during the assessment!")
input("Press ENTER when you are ready to begin...\n")
for questiondata in assessment:
    questionnum = questionnum + 1
    validanswer = False # initial state
    while validanswer == False: # force 1-5 answer, to prevent python error closing script
        print("\nQuestion #" + str(questionnum) + ":")
        answer = input(questiondata['question']+"\n") # ask question
        if answer.isdigit():
            answer = int(answer)
            if answer > 5 or answer < 1:
                print("ERROR: Your answer must be a number 1-5\n")
                validanswer = False
            else:
                print("Your Answer: " + answerdescriptions[answer-1])
                confirm = input("Type Y to confirm your answer, then press ENTER.\n")
                if confirm == "Y" or confirm == "y":
                    if questiondata['math'] == "+":
                        answerMath = answer
                    else:
                        answerMath = 5 - (answer-1)
                    typeScores[int(questiondata['type'])-1] = typeScores[int(questiondata['type'])-1] + answerMath
                    validanswer = True
                else:
                    print("\nPlease answer this question again & confirm it...\nYou can type 'help' for more information!\n")
        elif answer == 'help' or answer == "HELP":
            print("\n\n********************************************\n********************************************\n********************HELP********************\n********************************************\n********************************************")
            print(helptext + "\n\nPlease continue by typing a number 1-5... \n")
        else:
            print("\nYou must answer the question with a number 1-5. Type 'help' for information!")
typeinfo = ["Extraversion","Agreeableness","Conscientiousness","Emotional Stability","Intellect/Imagination"]
num = 0
for type in typeinfo:
    print(type + ": " + str(typeScores[num]))
    num = num + 1

print("\n\nThank you for taking the Big Five Aspect Scale Personality Test.")


