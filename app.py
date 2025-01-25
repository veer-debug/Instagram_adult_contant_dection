from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    reels = [
        {"video_url": "https://www.w3schools.com/html/mov_bbb.mp4", "caption": "Enjoying the sunset!"},
        {"video_url": "https://www.w3schools.com/html/movie.mp4", "caption": "Beach vibes"},
        {"video_url": "https://www.w3schools.com/html/mov_bbb.mp4", "caption": "Enjoying the sunset!"},
        {"video_url": "https://www.w3schools.com/html/movie.mp4", "caption": "Beach vibes"},
        {"video_url": "https://www.w3schools.com/html/mov_bbb.mp4", "caption": "Enjoying the sunset!"},
        {"video_url": "https://www.w3schools.com/html/movie.mp4", "caption": "Beach vibes"},
        {"video_url": "https://www.w3schools.com/html/mov_bbb.mp4", "caption": "Enjoying the sunset!"},
        {"video_url": "https://www.w3schools.com/html/movie.mp4", "caption": "Beach vibes"},
        {"video_url": "https://www.w3schools.com/html/mov_bbb.mp4", "caption": "Enjoying the sunset!"},
        {"video_url": "https://www.w3schools.com/html/movie.mp4", "caption": "Beach vibes"},
        {"video_url": "https://www.w3schools.com/html/mov_bbb.mp4", "caption": "Enjoying the sunset!"},
        {"video_url": "https://www.w3schools.com/html/movie.mp4", "caption": "Beach vibes"},
        {"video_url": "https://www.w3schools.com/html/mov_bbb.mp4", "caption": "Enjoying the sunset!"},
        {"video_url": "https://www.w3schools.com/html/movie.mp4", "caption": "Beach vibes"},
        {"video_url": "https://www.w3schools.com/html/mov_bbb.mp4", "caption": "Enjoying the sunset!"},
        {"video_url": "https://www.w3schools.com/html/movie.mp4", "caption": "Beach vibes"},
        {"video_url": "https://www.w3schools.com/html/mov_bbb.mp4", "caption": "Enjoying the sunset!"},
        {"video_url": "https://www.w3schools.com/html/movie.mp4", "caption": "Beach vibes"},
        {"video_url": "https://www.w3schools.com/html/mov_bbb.mp4", "caption": "Enjoying the sunset!"},
        {"video_url": "https://www.w3schools.com/html/movie.mp4", "caption": "Beach vibes"},
        {"video_url": "https://www.w3schools.com/html/mov_bbb.mp4", "caption": "Enjoying the sunset!"},
        {"video_url": "https://www.w3schools.com/html/movie.mp4", "caption": "Beach vibes"},
        {"video_url": "https://www.w3schools.com/html/mov_bbb.mp4", "caption": "Enjoying the sunset!"},
        {"video_url": "https://www.w3schools.com/html/movie.mp4", "caption": "Beach vibes"},
        {"video_url": "https://www.w3schools.com/html/mov_bbb.mp4", "caption": "Enjoying the sunset!"},
        {"video_url": "https://www.w3schools.com/html/movie.mp4", "caption": "Beach vibes"},
        {"video_url": "https://www.w3schools.com/html/mov_bbb.mp4", "caption": "Enjoying the sunset!"},
        {"video_url": "https://www.w3schools.com/html/movie.mp4", "caption": "Beach vibes"},
        {"video_url": "https://www.w3schools.com/html/mov_bbb.mp4", "caption": "Enjoying the sunset!"},
        {"video_url": "https://www.w3schools.com/html/movie.mp4", "caption": "Beach vibes"},
        {"video_url": "https://www.w3schools.com/html/mov_bbb.mp4", "caption": "Enjoying the sunset!"},
        {"video_url": "https://www.w3schools.com/html/movie.mp4", "caption": "Beach vibes"},
        {"video_url": "https://www.w3schools.com/html/mov_bbb.mp4", "caption": "Morning workout"}
    ]
    return render_template('index.html', reels=reels)

if __name__ == '__main__':
    app.run(debug=True)
