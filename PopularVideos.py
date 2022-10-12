from selenium import webdriver
import pandas as pd
import time

def getData():

    url = 'https://www.youtube.com/c/JohnWatsonRooney/videos?view=0&sort=p&flow=grid'

    driver = webdriver.Chrome()
    driver.get(url)
    video_list = []


    videos = driver.find_elements('class name', 'style-scope ytd-grid-video-renderer')

    for video in videos:
        title = video.find_element('xpath', './/*[@id="video-title"]').text
        views = video.find_element('xpath', './/*[@id="metadata-line"]/span[1]').text
        when = video.find_element('xpath', './/*[@id="metadata-line"]/span[2]').text
        vid = {'Title':title,
               'Views':views,
               'When':when
        }

        video_list.append(vid)

    df = pd.DataFrame(video_list)
    return df.to_csv("PopularVideos.csv")

getData()