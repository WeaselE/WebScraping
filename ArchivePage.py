from pywebcopy import save_webpage

url = 'https://www.reddit.com/r/interestingasfuck/comments/nfp97c/this_is_what_a_super_moon_at_the_temple_of/'
loc = 'C:\\Users\\Wesley\\Desktop\\'

kwargs = {'bypass_robots': True, 'project_name': 'Reddit-Test'}

save_webpage(url, loc, reset_config=True, **kwargs)