# check_spam() acts as the main function. Takes an assesses whether email message is spam.
def check_spam():
    # Empty variables that we'll use to store the spam words and likelihood determination.
    red_flags_captured = []
    likelihood = ""

    # Asks the user to drop in their email message to scan for spam words.
    email_msg = input("Please enter your email message here: ")
    # to make things easier to compare, we'll make all words in email lowercase.
    clean_email_msg = email_msg.lower()

    # list of 30 common words found in spam messages.
    red_flags = [
        "act now", "limited", "urgent", "immediate", "required",
        "verify", "confirm", "identity", "suspended", "locked",
        "billing", "free", "risk-free", "cash", "income",
        "winner", "prize", "claim", "gift", "refund",
        "investment", "earn", "bonus", "discount", "bargain",
        "miracle", "proven", "weight loss", "cure", "expired"
    ]

    # loops through every word in red flag list
    for word in red_flags:
        #checks word in red flag list for existence in email message.
        if word.lower() in clean_email_msg:

            #if red flag word present in email, counts how many times it occurs.
            #loop, for each time the word occurs, it adds the word to captured list.
            occurrences = clean_email_msg.count(word.lower())
            for i in range(occurrences):
                red_flags_captured.append(word)


    # the actual spam score is returned once calculated in the spam test (see below).
    spam_score = spam_test(red_flags_captured, red_flags)

    #Spam score will be associated with spam likelihood association.
    if spam_score >= 30:
        likelihood = "very high"
    elif spam_score >= 15:
        likelihood = "high"
    elif spam_score >= 10:
        likelihood = "above average"
    elif spam_score >= 5:
        likelihood = "below average"
    else:
        likelihood = "not high"

    #The final message to the user.
    determination = f"Your spam score is {spam_score}%, making the likelihood your email message being spam {likelihood}."

    print(determination)



# the function will take the captured flag list and the common spam word list as args.
def spam_test(flags, flag_list):

    #The score will be the quotient of count of captured flags divided by count of common spam words.
    score = int((len(flags) / len(flag_list))*100)
    return score



check_spam()