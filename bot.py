import json
from json.decoder import JSONDecodeError
from selenium import webdriver
import time
from time import sleep
from termcolor import colored
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--headless")
chrome_options.add_argument("log-level=3")
browser = webdriver.Chrome(options=chrome_options)
browser.implicitly_wait(5)

init_site = "https://www.quizup.com/en/login"
email = "wackydawg411@gmail.com"
pw = "Comput3ch"

browser.get(init_site)

browser.find_element_by_id("email").send_keys(email)
browser.find_element_by_id("password").send_keys(pw)

browser.find_element_by_class_name("SubmitButton").click()

# print("Monitoring global MARIO UNIVERSE.")
# print("Monitoring global NAME THE FLAG.")
print("Monitoring global LOGOS.")
print("Monitoring global NAME THE POKEMON.")

WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "MyMiniProfile__name")))
mario_universe_global = "https://www.quizup.com/api/topics/en-mario-universe/leaderboard?filter_by=global&time_filter=monthly&year=2020&month=6"
name_the_flag_global = "https://www.quizup.com/api/topics/name-the-flag/leaderboard?filter_by=global&time_filter=monthly&year=2020&month=6"
logos_global = "https://www.quizup.com/api/topics/logos/leaderboard?filter_by=global&time_filter=monthly&year=2020&month=6"
name_the_pokemon_global = "https://www.quizup.com/api/topics/name-the-pokemon/leaderboard?filter_by=global&time_filter=monthly&year=2020&month=6"
general_knowledge_global = "https://www.quizup.com/api/topics/general-knowledge/leaderboard?filter_by=global&time_filter=monthly&year=2020&month=6"

time_to_run = int(input("Enter how many minutes to run for: ")) * 60



def get_xp_data(link):
    browser.get(link)
    response = browser.find_element_by_tag_name("body").text

    parsed = json.loads(response)
    parsed = parsed["leaderboard"]["top"]

    xp_table = {}
    for p in parsed:
        xp_table[p["player"]["name"]] = p["xp"] 

    return xp_table
        
init_xp_data_1 = get_xp_data(logos_global)
init_xp_data_2 = get_xp_data(name_the_pokemon_global)

# print(response)
# print(json.dumps(init_xp_data_1, indent=4))

print("Initial data loaded.")
sleep(15)

reported_players = []

def monitor(api_link, db):
    new_xp_data = get_xp_data(api_link)
    if new_xp_data == db:
        pass
    else:
        for player in new_xp_data:
            if db[player]:
                difference = new_xp_data[player] - db[player]
                if not difference:
                    pass
                elif difference <= 1000:
                    print(colored("player {}: {} XP".format(player, difference), "green"))
                elif difference > 1000:
                    print(colored("player {}: {} XP".format(player, difference), "red"))
                    reported_players.append(player)
            else:
                print("Player not tracked: {}".format(player))

print("Monitoring...")
start_time = time.time()

while (time.time() - start_time) < time_to_run:
    try:
        # print("Checking Mario Universe...")
        monitor(logos_global, init_xp_data_1)
        # print("Checking Name the Flag...")
        monitor(name_the_pokemon_global, init_xp_data_2)
        sleep(5)
        init_xp_data_1 = get_xp_data(logos_global)
        init_xp_data_2 = get_xp_data(name_the_pokemon_global)
        sleep(60)
    except JSONDecodeError:
        print("Error parsing table. Retrying in ten seconds.")
        sleep(10)

browser.quit()
print("Monitoring complete.")

if reported_players:
    print("Following players are reported:")
    for r in reported_players:
        print(r)
else:
    print("No players reported!")