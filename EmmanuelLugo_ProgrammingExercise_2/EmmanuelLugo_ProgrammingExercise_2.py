"""
Spam (or junk email) costs U.S. organizations billions of dollars a year in spam-prevention software, equipment, network resources, bandwidth, and lost productivity. Research online some of the most common spam email messages and words. Create a list of 30 words and phrases commonly found in spam messages. Write an application in which the user enters an email message. Then your application will scan the message for each of the 30 keywords or phrases. For each occurrence of one of these within the message, add a point to the message's "spam score". Next, rate the likelihood that the message is spam, based on the number of points received. Display the user's spam score, the likelihood message that it is spam, and the words/phrases which caused it to be spam.

You should have at least two functions, but you can have more.

You must also have a technical design document (refer to the Submitting Programming Exercises Module).

Submit both your .py file and .doc/.docx file in this assignment and these files must also be in your repository.


"""

def check_spam():
    red_flags_captured = []
    email_msg = input("Please enter your email message here: ")

    clean_email_msg = email_msg.lower()

    red_flags = ["act now","limited time offer","immediate action required","verify your account","confirm your identity","account is on hold", "account suspended","locked out","update your billing","100% free","risk-free","double your cash","financial freedom","you are a winner","claim your prize","guaranteed investment","earn extra income","cash refund","complimentary gift","cures baldness","miracle cure","scientifically proven","weight loss","burn fat","no prescription required","exclusive discount","unbelievable bargain","secret bonus","urgent","expired"]

    for word in red_flags:
        if word.lower() in clean_email_msg:
            occurrences = clean_email_msg.count(word.lower())
            for i in range(occurrences):
                red_flags_captured.append(word)

    print(len(red_flags))



    spam_score = spam_test(red_flags_captured, red_flags)

    determination = f"Your spam score is {spam_score}%. Please proceed at your own risk based on the likelihood of your email message."
    print(determination)




def spam_test(flags, flag_list):
    score = int((len(flags) / len(flag_list))*100)
    return score



check_spam()