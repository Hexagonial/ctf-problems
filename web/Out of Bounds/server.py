import os
from flask import Flask, redirect, url_for, render_template

glitches = [
    "Post 0 glitch",
    "Borderlands 2 - Bloodshot Stronghold Skip",
    "Pandora LastEpisode - Platforming Skip",
    "Deep Rock Galactic - Space Rig OOB",
    "Kitty Kart 64"
]

gifs = [
    "lolisWalk.gif",
    "borderlands.webp",
    "pandora.webp",
    "drg.webp",
    "kk64.webp"
]

descriptions = [
    "Post 0 description",

    """
    In Borderlands 2's Bloodshot Stronghold, you can skip the entire area by rocket jumping through the ceiling and parkouring the rooftops.
    Cya later, toilet room!!
    """,

    """
    In Pandora LastEpisode, the "Options" tab of the Memoire has a hitbox which you can collide with and use it to fly into the sky.
    Forget the platforming between Ancient Sacred Cave and Phantom of Coccytus!
    """,

    """
    In Deep Rock Galactic's Space Rig, you can explore the vastness of space by using this elevator to clip through the corner.
    marisa
    """,

    """
    In Kitty Kart 64, you can go out of bounds. I'm sure this has no unfavorable repercussions.
    """
]

credits = [
    "Credit 0",
    "Footage by Unicycle Jimmy on YouTube",
    "Footage by Hexagonial",
    "Footage by Hexagonial",
    "Footage by ManlyBadassHero on YouTube"
]

app = Flask(__name__)

@app.route("/post/0/")
def index():
    return render_template("index.html")

@app.route("/")
def root():
    return redirect(url_for("index"))

@app.route("/postnotfound/")
def notFound():
    return "Whew! Thankfully, I made sure that weird post indexes are handled and are thus still in bounds for this website!"

@app.route("/post/<postNum>/")
def post(postNum: str):
    # Initialize variables to fill the webpage with.
    index = 0
    glitch = glitches[0]
    gif = gifs[0]
    description = descriptions[0]
    credit = credits[0]

    # Check if the request post number is numeric.
    if postNum.isnumeric() == False:
        try:
            index = int(postNum)
            print("Non-numeric index: " + str(index))
            if index < 0:
                glitch = "TexSAW 2024 - Out of Bounds Out of Bounds"
                description =   """
                                In the \"Out of Bounds\" CTF problem for TexSAW 2024,
                                you can find the flag when browsing to a post with a negative number.

                                texsaw{aw4y_fr0m_the_b0und4rie5_4cd1efa8}
                                """
                credit = "CTF problem by Hexagonial"
            else:
                # I don't think this is possible but it's here!
                return redirect(url_for("notFound"))
        except:
            return redirect(url_for("notFound"))
    else:
        index = int(postNum)

        # If trying to get a post that has not been added yet
        if index > len(glitches)-1 and index != 727:
            glitch= "This post doesn't exist yet!"
            description="One day I'll find an OOB glitch to add here!"
            credit = "Footage by... there is no footage"
        # Normal post exists
        elif index == 727:
            glitch = "727! WYSI!!"
            description = "wyfsi"
            gif = "wysi.gif"
            credit = ""
        else:
            glitch = glitches[index]
            gif = gifs[index]
            description = descriptions[index]
            credit = credits[index]
    
    description = description.split("\n")
    return render_template("post.html", index=index, glitch=glitch, description=description, credit=credit, gif=gif)

@app.route("/admin/")
def admin():
    return  """
            This is where I'd put an admin panel for admins.\n
            Too bad I don't have any!
            """

if __name__ == "__main__":
    app.run()