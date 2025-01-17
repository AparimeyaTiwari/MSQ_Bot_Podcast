from youtube_transcript_api import YouTubeTranscriptApi

YouTubeTranscriptApi.get_transcript('Z1RJmh_OqeA&t=514s')
transcript_list = YouTubeTranscriptApi.list_transcripts("Z1RJmh_OqeA&t=514s")

for transcript in transcript_list:
    print(transcript.fetch())
