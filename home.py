import praw
import enchant

reddit = praw.Reddit(client_id="**Gc2pWzi****",
                     client_secret="",
                     password="*******",
                     user_agent="prawapp by u/ar*******al",
                     username="ar*******al")

# to access a particular subreddit
target_sub = "conspiracy_area51"
subreddit = reddit.subreddit(target_sub)

# this will trigger the bot
trigger_phase = "!sgtBot"

# Dict checks the words and suggests possible corrections
d = enchant.Dict("en_US")

for comment in subreddit.stream.comments():
    if trigger_phase in comment.body:
        # extract word from comment
        word = comment.body.replace(trigger_phase, "")

        reply_text = ""

        # enchant now comes to work as it suggest for word
        similar_words = d.suggest(word)
        for similar in similar_words:
            reply_text += similar + " "

        # here comes the bot reply
        comment.reply(reply_text)
