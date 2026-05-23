import random
import requests
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


# tambahan function
def gen_anime_quote(anime):

    quote_pool = {
        "jjk": [
            {
                "character": "Gojo Satoru",
                "quote": "Throughout heaven and earth, I alone am the honored one."
            },
            {
                "character": "Gojo Satoru",
                "quote": "Love is the most twisted curse of all."
            },
            {
                "character": "Nanami Kento",
                "quote": "You've got it from here."
            },
            {
                "character": "Itadori Yuji",
                "quote": "I don't know how I'll feel when I'm dead, but I don't want to regret the way I lived."
            },
            {
                "character": "Megumi Fushiguro",
                "quote": "I choose who I save."
            }
        ],

        "kny": [
            {
                "character": "Rengoku Kyojuro",
                "quote": "Set your heart ablaze."
            },
            {
                "character": "Tanjiro Kamado",
                "quote": "Hard work is the sum of daily actions."
            },
            {
                "character": "Zenitsu Agatsuma",
                "quote": "If you can only do one thing, hone it to perfection."
            },
            {
                "character": "Giyu Tomioka",
                "quote": "The weak have no rights or choices."
            },
            {
                "character": "Shinobu Kocho",
                "quote": "Humans are to be protected and saved."
            }
        ],

        "sakamoto": [
            {
                "character": "Taro Sakamoto",
                "quote": "Peaceful days are worth fighting for."
            },
            {
                "character": "Shin",
                "quote": "Strong people protect what matters to them."
            },
            {
                "character": "Taro Sakamoto",
                "quote": "Family comes before everything else."
            },
            {
                "character": "Lu Xiaotang",
                "quote": "A true assassin never leaves a trace."
            },
            {
                "character": "Nagumo",
                "quote": "Even legends can live ordinary lives."
            }
        ]
    }

    quote = random.choice(quote_pool[anime])

    return f"{quote['quote']} - {quote['character']}"

# def get_duck_image_url():    
#     url = 'https://random-d.uk/api/random'
#     res = requests.get(url)
#     data = res.json()
#     return data['url']


def get_anime_image_url(keyword):
    url = f"https://kitsu.io/api/edge/anime?filter[text]={keyword}"
    res = requests.get(url)
    data = res.json()
    all_anime_url = [item['attributes']['posterImage']['original'] for item in data['data']]
    anime_url = random.choice(all_anime_url)

    return anime_url

# non_recyclable_waste = ["food scraps", "dirty tissue", "diaper", "cigarette butt", "styrofoam"]
# recyclable_waste = ["plastic bottle", "plastic cup", "glass bottle", "newspaper", "cardboard", "can"]

def get_waste_type(waste):

    #standarisasi inputan
    waste = waste.lower().strip()
    non_recyclable_waste = ["food scraps", "dirty tissue", "diaper", "cigarette butt", "styrofoam"]
    recyclable_waste = ["plastic bottle", "plastic cup", "glass bottle", "newspaper", "cardboard", "can"]

    if waste in recyclable_waste:
        return "It's a recylable waste"
    elif waste in non_recyclable_waste:
        return "It's a non-recyclable waste"
    else:
        return "I can't define the waste type"



def get_reduce_waste_tips(how_many):
    reduce_waste_tips = [
        "Cobalah untuk menghindari penggunaan barang sekali pakai, seperti gelas dan botol plastik",
        "Pindah ke e-reader untuk mengurangi konsumsi kertas",
        "Pilih produk bahan makanan dan makanan ringan dengan kemasan sesedikit mungkin, beli makanan berdasarkan beratnya (tanpa kemasan), dan cobalah beralih ke tas yang dapat digunakan kembali",
        "Cobalah untuk mendaur ulang. Sediakan tempat sampah khusus untuk produk yang dapat didaur ulang dan pindahkan ke tempat daur ulang setelah penuh"
    ]

    return random.choices(reduce_waste_tips, k=how_many)
