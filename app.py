from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

# STORIES = {
#     "silly_story": {
#         "promtps": ["place", "noun", "verb", "adjective", "plural_noun"],
#         "story": """Once upon a time, in a long-ago {place}, there lived an exceptionally
#        {adjective} {noun}. It loved to {verb} with {plural_noun}."""
#     },

#     "excited_story": {
#         "prompts": ["noun", "verb"],
#         "story": """OMG!! OMG!! I love to {verb} a {noun}!"""
#     }
# }

@app.get("/")
def generate_prompt_form():
    prompts = silly_story.prompts
    return render_template('questions.html', prompts=prompts )

# @app.get("/results")
# def