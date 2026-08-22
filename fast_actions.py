import re


ACTION_PATTERNS = {

    "play_music": [
        r"\bplay (some )?music\b",
        r"\bplay (a )?(random )?song\b",
        r"\bput on (some )?music\b",
        r"\blet'?s listen to (some )?music\b",
    ],

    "get_time": [
        r"\bwhat time is it\b",
        r"\bwhat'?s the time\b",
        r"\bcurrent time\b",
        r"\btell me the time\b",
    ],

    "capture_image": [
        r"\btake (a )?(photo|picture)\b",
        r"\bcapture (a )?(photo|picture|image)\b",
        r"\bwhat do you see\b",
        r"\blook around\b",
    ]
}

DEFAULT_VALUES = {
    "play_music": "random",
    "get_time": "now",
    "capture_image": "environment"
}

def detect_fast_action(text):
    text = text.lower().strip()

    for action, patterns in ACTION_PATTERNS.items():

        for pattern in patterns:

            if re.search(pattern, text):

                return {
                    "action": action,
                    "value": DEFAULT_VALUES.get(action)
                }

    return None