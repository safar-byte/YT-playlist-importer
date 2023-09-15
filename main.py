# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlists.insert
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import csv


import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server(host='localhost',
      port=8080, 
      authorization_prompt_message='Please visit this URL: {url}', 
      success_message='The auth flow is complete; you may close this window.',
      open_browser=True)
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    

    filepath = input("Enter the takeout csv playlist: ")
    
    playlistName = os.path.splitext(os.path.basename(filepath))[0]
    with open(filepath, 'r') as file:
          csvreader = csv.reader(file,dialect='excel')
          rows = []
          for row in csvreader:
              rows.append(row[0])
          rows.pop(0)
          
    request = youtube.playlists().insert(
          part="snippet,status",
          body={
            "snippet": {
              "title": playlistName
            },
            "status": {
              "privacyStatus": "private"
            }
          }
      )
    response = request.execute()
	
    PlaylistId = response["id"]
    for j in rows: 
        request1 = youtube.videos().list(
            
            id=j,
            part="status"
        )
        response1 = request1.execute()
        if response1["items"]==[]:
            rows.remove(j)
         
    for i in rows:
        request = youtube.playlistItems().insert(
          part="snippet",
          body={
            "snippet": {
              "playlistId": PlaylistId,
              
              "resourceId": {
                "kind": "youtube#video",
                "videoId": i
              }
            }
          }
        )
        response = request.execute()
        print(response)
    
         
         


    
if __name__ == "__main__":
    main()