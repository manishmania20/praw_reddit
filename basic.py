import praw
#from praw.models import MoreComments

#create a password flow app where tokens refresh after every hour
reddit = praw.Reddit(client_id="UMttwT3KhBENcA",  
                    client_secret="9T6FdBRuRmxcNXoVVsrL3_NMpYQ",
                    password="a*rWCdd*K^2nbGTgB8iGhJf9nVQc",  
                    user_agent="prawapp",
                    username="OkInstruction7131")

#check if it's a read-only or auth instance
#print(reddit.read_only)

#to make the app read_only 
#reddit.read_only=true 

#returns the username
#print(reddit.user.me())

#to access a particular subreddit
subreddit = reddit.subreddit('assassinscreed')

#display the subreddit name
#print(subreddit.display_name)

#display the subreddit title
#print(subreddit.title)

#display the subreddit description
#print(subreddit.description)

"""display similar info but for a specific post sorted by top/hot/new/gilded/controversial
    it's in form of a list so we iterate through it using limit=n where 'n' being no of submissions to display"""
"""
for post in subreddit.top(limit=1):
    print('Title: ',post.title)
    print('Upvotes: ',post.score)
    print('Upvotes percentage:',post.upvote_ratio*100)
    print('Comments: ',post.num_comments)
    print('Submission by: ',post.author)
    #print(post.id)
    print(post.url)
    #print(post.created_utc)
    #use CommentForest to display the top comments of the post in concern
    for top_level_comment in post.comments:
        print(top_level_comment.body)
    for top_level_comment in post.comments:
        check if MoreComments or basically the  load more comments is part of the top_level_comment
        if isinstance(top_level_comment,MoreComments):
            continue
        print(top_level_comment.body)

    #replace_more() method is considerably better to use as it auto removes all the more comments
    post.comments.replace_more(limit=0)
    for top_level_comment in post.comments:
        print(top_level_comment.body)
"""
#to know about karma in store for a particular Redditor and condition being account isn't deleted or shadowbanned
redditor = reddit.redditor('manxmaniac')

#display info of the redditor 
print('Username: ',redditor.name)
print('Post karma: ',redditor.link_karma)
print('Comment karma: ',redditor.comment_karma)
total_karma = redditor.link_karma + redditor.comment_karma
print('Overall karma: ',total_karma)
print('Email verification status: ',redditor.has_verified_email)
print('Friends with me?: ',redditor.is_friend)
