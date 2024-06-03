# Čia bus laikoma visi pasakotojo ir veikėjų tekstai.
# Turime dict, kur yra laikoma scenų pavadinimai (pvz. Home, Store, Outside ir t.t.).
# Scenos viduje yra laikomi visų veikėjų, pasakotojo tekstai listuose.

from ui.constants import USER_NAME

story_text = {
    "HomeRoom": {
        "selection": ["Balcony", "Kitchen", "Bathroom", "Sleep"],
        "story": [f"You are {USER_NAME}.",
                  "You are thirsty. You just came back from a peculiarly exhausting sleep. What do you do?",
                  "You came back to the bedroom."],
        "player": [" ", " ", " "],
    },
    "HomeBalcony": {
        "selection": ["Bedroom", "Smoke", "Outside", "Check Pigeon nest"],
        "story": ["It's the balcony, the day is unpleasantly warm.",
                  "There's a pigeon egg nested on an old box in the leftmost corner.",
                  "You don't seem to have any cigarettes with you.",
                  "You awkwardly climb out of the balcony and then... fall 5 stories to your death.",
                  "You search everywhere, but you can't find any cigarettes.",
                  "You decide to go back to your room."],
        "player": [" ", " ", " "],
    },
    "HomeKitchen": {
        "selection": ["Talk to Mom", "Food", "Outside", "Bedroom", "Ask for ciggie"],
        "story": ["You arrive at the Kitchen, mom is cooking breakfast while smoking a cigarette.",
                  "She doesn't pay you any attention.",
                  "You open the fridge door. There's scarcely any food inside. \nYou conclude that you're not hungry.",
                  "You go back to your room."],
        "player": ["\"Hi.\"", ],
        "mom": ["\"Hi.\"", ],
    },
    "HomeBathroom": {
        "selection": ["Bedroom"],
        "story": ["You've entered the bathroom. Despite sleeping for 11 hours, the mirror reflects your tired face.",
                  "You go back to your room.",
                  "Uhh nothing changed here bro."],
        "player": [" ", " ", " "],
    },
    "HomeLaiptine": {
        "story": ["You put your shoes on and head through your apartment's door.",
                  "You find yourself heading down the stairwell.",
                  "[CHECK SUCCESS] You narrowly miss the eye contact of a passing neighbour.",
                  "[CHECK FAILURE] The neighbour's gaze compels you to say something."],
        "player": ["\"Hello\"", " ", " "],
        "kaimynas": ["\"Hello\"", " ", " "],
    },
    "HomeNarvelis": {
        "selection": ["Listen in", "Stare him down", "Leave"],
        "story": ["You are now Outside.",
                  "But it feels like you've just entered a greenhouse.",
                  "There's a man in his early thirties perched atop the railing of the bench to your right. ",
                  "Feet in black, branded flip-flops firmly placed on the sitting area of the bench. ",
                  "He's talking on the phone.",
                  "And now he's looking at you.",
                  "If by 'Stare him down' you mean 'Sourly fix your gaze on the flip-flops', then you're certainly "
                  "doing it.",
                  "You hold your gaze there for roughly 3 seconds, instinctivelly check your pockets for "
                  "smokes, which you're well aware aren't there.",
                  "And without ever meeting his eyes head-on, you leave.",
                  "You stop, the heavy steel doors of the apartment complex slowly close behind you, "
                  "with a badly oiled creak.",
                  "You immitate checking your pockets for smokes.",
                  "And without meeting his gaze, you move to the left of the door and with an immitated ponderous "
                  "expression, you look towards the playground.",
                  "You don't know whether the man is looking at you or not.",
                  "He resumes his conversation.",
                  "There's the playground in the distance. You see a boy, playing on his own. The afternoon sun made "
                  "all the responsbile people scatter to their hidy-holes.",
                  "Seems like there's only you out, that boy, and this gentleman perched behind you. "
                  "You take a deeper breath.",
                  "And at this moment you must look like the marlboro cowboy-man, from the commercials.",
                  "Or so you think that's what your expression conveys.",
                  "Silence. You weren't aware of it before, but there's no wind.",
                  "The 'conversation' you just heard wasn't as interesting as you thought it would be."],
        "player": [" ", " ", " "],
        "kaimynas": [" ", " ", " "],
    },
    "Store": {
        "selection":
            ["Buy smokes", "Leave", "Try to haggle for the smokes", "Try to steal the smokes"],
        "story":
            ["You're suddenly hit with the respite of air conditioning, set to high.",
             "You feel like you could walk around here for the rest of the day, just to be out of the heat.",
             "You immediately walk to the cash register, and stand in line. There's a few people before you.",
             "You feel like they're as glad, as you are, to be out of the heat.",
             "A few minutes pass. The last person before you is packing his groceries into a bag. It's now your turn.",
             "Just at this moment you remember something.",
             "You frantically check your pockets for the X amount of currency.",
             "You're dead broke.",
             "It's embarrasing really.",
             "Now this is extremely embarrasing.",
             "Please stop, have some dignity.",
             "You try to quickly grab the cigarretes out of the cashier's hand. You fail. The cashier screams for security.",
             "Perhaps this is the stupidest thing you've ever done in your life.",
             "You're interrogated by security, while they wait for the cops to arrive.",
             "Then you're taken away by the cops for attempted theft.",
             "Congratulations, game over.",
             "You pay with the pigeon money. Well, when life gives you lemons..."],
        "player":
            ["\"Good afternoon, a Camel Blue please.\"", "\"I'm sorry but I seem to have no money on me, "
                                                     "can i buy the cigarretes now and return later with the money?\"",
             "\"Pretty please, I swear I'll return with the money.\""],
        "kasininke":
            ["\"Certainly, that'll be X amount of currency.\"", "\"I'm sorry sir but no, you'll need to pay NOW.\"",
             "\"I am sorry sir, but no money, no products.\""],
    },
}
