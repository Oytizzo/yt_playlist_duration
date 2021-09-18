import os
from googleapiclient.discovery import build


def main():
    api_key = os.environ.get("yt_developer_api_key")
    api_service_name = "youtube"
    api_version = "v3"

    yt = build(api_service_name, api_version, developerKey=api_key)

    pl_request = yt.playlists().list(
        part="contentDetails, snippet",
        channelId="UCCezIgC97PvUuR4_gbFUs5g"
    )
    pl_response = pl_request.execute()

    # print(pl_response)
    for item in pl_response["items"]:
        print(item)
        print()


if __name__ == "__main__":
    main()
