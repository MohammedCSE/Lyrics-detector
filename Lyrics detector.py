import speech_recognition as sr
import requests
import webbrowser
recognizer = sr.Recognizer()


print("Say a lyric...")
try:
    with sr.Microphone() as mic:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        audio = recognizer.listen(mic)

        user_input = recognizer.recognize_google(audio)
        print("you said : ", user_input)


except sr.UnknownValueError:
    print("Could not understand. Try again.")
    exit()

access_token = "oFES-nbs91A7Dm_nEVDWl36SIKKkjg_fQA7h5kDf_fgSrKtjUSyvV_jI3YfwmaRc"
url = "https://api.genius.com/search"
headers = {"Authorization": f"Bearer {access_token}"}
params = {"q": user_input}

response = requests.get(url, headers=headers, params=params)
data = response.json()
if data["response"]["hits"]:
    song = data["response"]["hits"][0]["result"]
    title = song["title"]
    artist = song["primary_artist"]["name"]
    print(f"Found song: {title} - {artist}")

    query = f"{title} {artist} official music video"
    youtube_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"

    webbrowser.open(youtube_url)

else:
    print("No song found ")