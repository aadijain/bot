import sys
import json
import re
import time
import praw
import logger

reload(sys)
sys.setdefaultencoding('unicode_escape')

def start(reddit):
    print "Logged in as user: ", reddit.user.me()
    while True:
        try:
            submission = reddit.submission(id='6h5y3v')
            submission.comments.replace_more(limit=0)
            comments = submission.comments.list()
            # subreddit = reddit.subreddit('all')
            # comments = subreddit.stream.comments()
            for comment in comments:
                st = comment.body
                # st[:6] == 'MEGA: ' and
                if(comment.author != reddit.user.me()):
                    re.sub('^', '###', st, flags=re.MULTILINE)
                    comment.reply(st)
        except KeyboardInterrupt:
            print "Stopping..."
            break
        except Exception as e:
            print "Error..."
            logger.log(e)
            time.sleep(15)

if __name__ == '__main__':
    config = json.loads(open('config.json').read())
    reddit = praw.Reddit(client_id=config["client_id"],
                         client_secret=config["client_secret"],
                         user_agent=config["user_agent"],
                         username=config["username2"],
                         password=config["password2"])
    #mega_bot
    start(reddit)