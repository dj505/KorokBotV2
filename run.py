import praw
import random
from random import randint
import time
import os

def login():
    r = praw.Reddit('korokBot',
                    user_agent= 'dj505Gaming\'s Korok Bot')
    print('Logged in successfully!')
    return r

def run_bot(r, replied_list, ignored_list):
    standard_reply = 'Yahaha! You found me!\n\n---\n\n ' \
    '^^Koroks ^^found: ^^{} ^^| ^^[Info](https://reddit.com/r/korokbot/) ^^| ' \
    '[^^Suggest ^^a ^^feature](https://www.reddit.com/r/KorokBot/comments/6n35g4/feature_suggestion_and_bux_fix_megathread/) ^^| ' \
    '^^Twee-hee!'.format('Still working on this part')

    dupe_reply = 'Twee hee!\n\n---\n\n' \
    '^^Koroks ^^found: ^^{} ^^| ' \
    '^^[Info](https://reddit.com/r/korokbot/) ^^| ' \
    '[^^Suggest ^^a ^^feature](https://www.reddit.com/r/KorokBot/comments/6n35g4/feature_suggestion_and_bux_fix_megathread/) ^^| ' \
    '^^Twee-hee!'.format('Still working on this part')

    hurt_expressions = ["Ouch.", "Unngh.", "Gya!"]

    hurt_reply = random.choice(hurt_expressions) + '\n\n---\n\n' \
    '^^Koroks ^^found: ^^{} ^^| ' \
    '^^[Info](https://reddit.com/r/korokbot/) ^^| ' \
    '[^^Suggest ^^a ^^feature](https://www.reddit.com/r/KorokBot/comments/6n35g4/feature_suggestion_and_bux_fix_megathread/) ^^| ' \
    '^^Twee-hee!'.format('Still working on this part')

    print('Searching for comments (limit 10)...')
    for comment in r.subreddit('breath_of_the_wild+zelda+botw+legendofzelda+gaming+nintendoswitch+stability_bot+korokbot+yahaha_irl').comments(limit=10):
        if 'korok' in comment.body and comment.id not in replied_list and comment.id not in ignored_list and comment.author != r.user.me():
            if randint(0, 100) < 30:
                if comment.parent().author != r.user.me():
                    print('Yahaha! Korok found! Comment ID {}'.format(comment.id))
                    comment.reply(standard_reply)
                    print('Replied to comment ID {}'.format(comment.id))
                    replied_list.append(comment.id)
                    with open('replied.txt','a') as f:
                        f.write(comment.id + '\n')

                    reddit.redditor('dj505Gaming').message('KorokBot', 'Replied to message ID {}'.format(comment.id))

                else:
                    print('Twee hee! Comment ID {}'.format(comment.id))
                    comment.reply(dupe_reply)
                    print('Replied to comment ID {}'.format(comment.id))
                    replied_list.append(comment.id)
                    with open('replied.txt','a') as f:
                        f.write(comment.id + '\n')

                    reddit.redditor('dj505Gaming').message('KorokBot', 'Replied to message ID {}'.format(comment.id))

            else:
                print('Korok found, randint > 30, ignoring...')
                replied_list.append(comment.id)

                with open('ignored.txt','a') as f:
                    f.write(comment.id + '\n')

    print('Sleeping (10s)...')
    time.sleep(10)

def get_replied_comments():
    if not os.path.isfile('replied.txt'):
        replied_list = []

    else:
        with open('replied.txt','r') as f:
            replied_list = f.read()
            replied_list = replied_list.split('\n')
            replied_list = list(filter(None, replied_list))

    return replied_list

def get_ignored_comments():
    if not os.path.isfile('ignored.txt'):
        replied_list = []

    else:
        with open('replied.txt','r') as f:
            replied_list = f.read()
            replied_list = replied_list.split('\n')
            replied_list = list(filter(None, replied_list))

    return replied_list

r = login()
replied_list = get_replied_comments()
ignored_list = get_ignored_comments()

while True:
    run_bot(r, replied_list, ignored_list)