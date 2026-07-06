"""
Spam (or junk email) costs U.S. organizations billions of dollars a year in spam-prevention software, equipment, network resources, bandwidth, and lost productivity. Research online some of the most common spam email messages and words. Create a list of 30 words and phrases commonly found in spam messages. Write an application in which the user enters an email message. Then your application will scan the message for each of the 30 keywords or phrases. For each occurrence of one of these within the message, add a point to the message's "spam score". Next, rate the likelihood that the message is spam, based on the number of points received. Display the user's spam score, the likelihood message that it is spam, and the words/phrases which caused it to be spam.

You should have at least two functions, but you can have more.

You must also have a technical design document (refer to the Submitting Programming Exercises Module).

Submit both your .py file and .doc/.docx file in this assignment and these files must also be in your repository.


"""

def check_spam():

    red_flags = ["Act now!","Limited time offer","Immediate action required","100% free","Risk-free","Double your cash/income","Financial freedom","You are a winner!","Verify your account","Confirm your identity","Your account is on hold","Important information regarding...","Cures baldness""Miracle cure","Scientifically proven","Weight loss","Burn fat","No prescription required","Winner","Prize","Selected","Gift","Claim","Cash","Investment","Income","Refund","Earn","Urgent","Immediate","Expired","Required","Important","Free","Complimentary","Discount","Bargain","Bonus","Verify","Confirm","Suspended","Locked","Update"]

    print(len(red_flags))

check_spam()