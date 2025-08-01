# modules/hashtag_generator.py

HASHTAG_BANK = {
    "fashion": [
        "#ootd", "#fashiongram", "#styleinspo", "#streetwear", "#aestheticstyle"
    ],
    "fitness": [
        "#fitspo", "#workoutmotivation", "#gains", "#fitnessaddict", "#gymflow"
    ],
    "travel": [
        "#wanderlust", "#passportready", "#travelblogger", "#sunsetlover", "#exploremore"
    ],
    "makeup": [
        "#makeuplover", "#glowup", "#beautyblogger", "#slaythelook", "#softglam"
    ],
    "photography": [
        "#moodygrams", "#lensculture", "#visuals", "#depthobsessed", "#snapshot"
    ]
}

def suggest_hashtags(niche):
    niche = niche.lower()
    return HASHTAG_BANK.get(niche, [
        "#personalbrand", "#contentcreator", "#instagrowth", "#aesthetic", "#viralvibes"
    ])
