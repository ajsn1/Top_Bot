import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


# quote_pool = {
#     "jjk": [
#         {
#             "character": "Gojo Satoru",
#             "quote": "Throughout heaven and earth, I alone am the honored one."
#         },
#         {
#             "character": "Gojo Satoru",
#             "quote": "Love is the most twisted curse of all."
#         },
#         {
#             "character": "Nanami Kento",
#             "quote": "You've got it from here."
#         },
#         {
#             "character": "Itadori Yuji",
#             "quote": "I don't know how I'll feel when I'm dead, but I don't want to regret the way I lived."
#         },
#         {
#             "character": "Megumi Fushiguro",
#             "quote": "I choose who I save."
#         }
#     ],

#     "kny": [
#         {
#             "character": "Rengoku Kyojuro",
#             "quote": "Set your heart ablaze."
#         },
#         {
#             "character": "Tanjiro Kamado",
#             "quote": "Hard work is the sum of daily actions."
#         },
#         {
#             "character": "Zenitsu Agatsuma",
#             "quote": "If you can only do one thing, hone it to perfection."
#         },
#         {
#             "character": "Giyu Tomioka",
#             "quote": "The weak have no rights or choices."
#         },
#         {
#             "character": "Shinobu Kocho",
#             "quote": "Humans are to be protected and saved."
#         }
#     ],

#     "sakamoto": [
#         {
#             "character": "Taro Sakamoto",
#             "quote": "Peaceful days are worth fighting for."
#         },
#         {
#             "character": "Shin",
#             "quote": "Strong people protect what matters to them."
#         },
#         {
#             "character": "Taro Sakamoto",
#             "quote": "Family comes before everything else."
#         },
#         {
#             "character": "Lu Xiaotang",
#             "quote": "A true assassin never leaves a trace."
#         },
#         {
#             "character": "Nagumo",
#             "quote": "Even legends can live ordinary lives."
#         }
#     ]
# }


