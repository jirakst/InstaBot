# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = ''
insta_password = ''

comments = [
        'Nice shot! @{}',
        'I love your profile! @{}',
        'Your feed is an inspiration :thumbsup:',
        'Just incredible :open_mouth:',
        'What camera did you use @{}?',
        'Love your posts @{}',
        'Looks awesome @{}',
        'Getting inspired by you @{}',
        ':raised_hands: Yes!',
        'I can feel your passion @{} :muscle:'
]

# experimental feautre - for smart hashtags
tags = [
    'architecture',
    'photography',
    'bw'
]

hashtags = [
        'architecture', 
        'architectural',
        'architect',
        'archi',
        'architexture',
        'architecturephotography',
        'architecturelovers',
        'architectureporn'
        'architexture',
        'photo',
        'photoshoot',
        'photoeveryday',
        'photogram',
        'photographylovers',
        'bw',
        'bwphotography',
        'stairs',
        'building',
        'buildings',
        'structure',
        'photography',
        'photographers',
        'photography📷',
        'minimalism'
        'philippines',
]	

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False,
                  want_check_browser=False)

with smart_run(session):
  """ Activity flow """		
  # general settings		
  session.set_dont_include(["mahlonhoward"])		
  
  # activity
  session.set_do_like(enabled=True, percentage=70)
  session.set_dont_like(["naked", "nsfw"])
  session.set_do_follow(True, percentage=50)

  # smart hashtags
  session.set_smart_hashtags(tags, limit=7, sort='top', log_tags=True)
  session.like_by_tags(use_smart_hashtags=True, amount=10)

  # Joining Engagement Pods
  session.set_do_comment(enabled=True, percentage=35)
  session.set_comments(comments)
  session.join_pods(topic='architecture', engagement_mode='no_comments')

  # Relationship bounds
  session.set_relationship_bounds(enabled=True, max_followers=16000)

  # Quota supervisor
  session.set_quota_supervisor(
        enabled=True,
        sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
        sleepyhead=True,
        stochastic_flow=True,
        notify_me=True,
        peak_likes_hourly=57,
        peak_likes_daily=585,
        peak_comments_hourly=21,
        peak_comments_daily=182,
        peak_follows_hourly=48,
        peak_follows_daily=None,
        peak_unfollows_hourly=35,
        peak_unfollows_daily=402,
        peak_server_calls_hourly=None,
        peak_server_calls_daily=4700
    )


# ClarifAI
#session.set_use_clarifai(enabled=True, api_key='<your_api_key>')
#session.clarifai_check_img_for(['nsfw'])

#session.end()
