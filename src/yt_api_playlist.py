import os
import re
from datetime import timedelta
from googleapiclient.discovery import build


def main():
    api_key = os.environ.get("yt_developer_api_key")
    api_service_name = "youtube"
    api_version = "v3"

    # panda playlist from corey
    # pl_id = "PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS"
    # python playlist from corey
    # pl_id = "PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU"
    # other playlist
    pl_id = "PLHiZ4m8vCp9MJDxMOzhYVuTrO1b5n-Tq_"
    yt = build(api_service_name, api_version, developerKey=api_key)

    hours_pattern = re.compile(r'(\d+)H')
    minutes_pattern = re.compile(r'(\d+)M')
    seconds_pattern = re.compile(r'(\d+)S')

    total_seconds = 0

    nextPageToken = None

    while True:
        pl_request = yt.playlistItems().list(part="contentDetails", playlistId=pl_id, maxResults=50, pageToken=nextPageToken)
        pl_response = pl_request.execute()

        vid_ids = []
        for item in pl_response["items"]:
            vid_ids.append(item['contentDetails']['videoId'])
        print(len(vid_ids))
        
        
        vid_request = yt.videos().list(part="contentDetails", id=','.join(vid_ids))
        vid_response = vid_request.execute()

        for item in vid_response['items']:
            duration = item['contentDetails']['duration']
            
            hours = hours_pattern.search(duration)
            minutes = minutes_pattern.search(duration)
            seconds = seconds_pattern.search(duration)

            hours = int(hours.group(1)) if hours else 0
            minutes = int(minutes.group(1)) if minutes else 0
            seconds = int(seconds.group(1)) if seconds else 0

            video_seconds = timedelta(hours=hours, minutes=minutes, seconds=seconds).total_seconds()

            total_seconds += video_seconds
        
        nextPageToken = pl_response.get('nextPageToken')

        if not nextPageToken:
            break

    total_seconds = int(total_seconds)

    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)

    print(f'{hours}:{minutes}:{seconds}')


if __name__ == "__main__":
    main()
