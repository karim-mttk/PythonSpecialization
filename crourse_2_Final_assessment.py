#problem 1:
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation (s):
    for i in punctuation_chars:
        s=s.replace(i,"")
    return s

#problem 2:
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


def strip_punctuation(s):
    for i in punctuation_chars:
        s = s.replace(i, "")
    return s


def get_pos(s):
    s = strip_punctuation(s)
    s = s.lower()
    c = 0
    for word in s.split():
        if word in positive_words:
            c += 1
    return c

#problem 3:
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(s):
    for i in punctuation_chars:
        s = s.replace(i, "")
    return s


def get_neg(s):
    s = strip_punctuation(s)
    s = s.lower()
    c = 0
    for word in s.split():
        if word in negative_words:
            c += 1
    return c

#problem 4:
# Function to calculate the sentiment scores for each tweet
def calculate_sentiment_scores():
    # Open the input file
    with open("project_twitter_data.csv", "r") as input_file:
        # Read the lines of the input file
        lines = input_file.readlines()

        # Create the output file
        with open("resulting_data.csv", "w") as output_file:
            # Write the header row
            output_file.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")

            # Process each tweet in the input file
            for line in lines[1:]:
                row = line.strip().split(",")
                tweet_text = row[0]
                num_retweets = int(row[1])
                num_replies = int(row[2])

                # Strip punctuation and convert to lowercase
                processed_text = strip_punctuation(tweet_text.lower())

                # Calculate the positive score
                positive_score = get_pos(processed_text)

                # Calculate the negative score
                negative_score = get_neg(processed_text)

                # Calculate the net score
                net_score = positive_score - negative_score

                # Write the row to the output file
                output_file.write(
                    "{},{},{},{},{}\n".format(num_retweets, num_replies, positive_score, negative_score, net_score))


# Call the function to calculate the sentiment scores and create the resulting data file
calculate_sentiment_scores()

