import os
from googleapiclient.discovery import build


def main():
    api_key = os.environ.get("yt_developer_api_key")
    api_service_name = "youtube"
    api_version = "v3"

    yt = build(api_service_name, api_version, developerKey=api_key)

    request = yt.channels().list(
        part="statistics",
        id="UCCezIgC97PvUuR4_gbFUs5g",
    )

    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()
