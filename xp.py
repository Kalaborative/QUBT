#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json

data = '''
{"leaderboard":{"filter":"global","time_filter":"monthly","top":[{"player":{"id":"1821951314821868479","name":"Count Carlvelt | ҜΞ 〽️","title":"Champion of Mario","location":{"country_code":"AQ","region_code":"XX"},"locale":"en","profile_photo":{"url":"http://quizup-players.imgix.net/players/1821951314821868479/pictures/b9ydz943x5/original.jpg?s=d9bad6fee0a15b3b75337226ffb5dbc5"},"private":false,"is_followed_by_me":false,"team_member":false,"url":"/services/players/1821951314821868479","wallpaper":{"url":"http://quizup-players.imgix.net/players/1821951314821868479/pictures/zd87nl0aba/wallpaper/original.jpg?s=09611b590efb4df36668354356c221fc"},"feature_flags":[],"permissions":[],"rank":1},"rank":1,"xp":408900,"stats":null},{"player":{"id":"1961129427782491551","name":"razin","title":"Living on Yoshi's Island","location":{"country_code":"MY","region_code":"XX"},"locale":"en","profile_photo":{"url":"http://quizup-players.imgix.net/players/1961129427782491551/pictures/xsdlcbsofj/original.jpg?s=229f26383545a429c67620ba0d7ce7d5"},"private":false,"is_followed_by_me":false,"team_member":false,"url":"/services/players/1961129427782491551","wallpaper":null,"feature_flags":[],"permissions":[],"rank":1},"rank":2,"xp":365489,"stats":null},{"player":{"id":"1250020463922127737","name":"Sniwott #C-ILA","title":"Got Nu-clear Vision","location":{"country_code":"US","region_code":"NY"},"locale":"en","profile_photo":{"url":"http://quizup-players.imgix.net/players/1250020463922127737/pictures/gysuymb3ek/original.jpg?s=8f7dea3ef73de5288d38d088eca9e4be"},"private":false,"is_followed_by_me":false,"team_member":false,"url":"/services/players/1250020463922127737","wallpaper":{"url":"http://quizup-players.imgix.net/players/1250020463922127737/pictures/9ilo6hua51/wallpaper/original.jpg?s=d189bd40a886d9524ec9bfb674edbc45"},"feature_flags":[],"permissions":[],"rank":1},"rank":3,"xp":180648,"stats":null},{"player":{"id":"232331719813879116","name":"Thrill. | ҜΞ 〽️","title":"Champion of Mario","location":{"country_code":"US","region_code":"GU"},"locale":"en","profile_photo":{"url":"http://quizup-players.imgix.net/players/232331719813879116/pictures/bt20qm9t3j/original.jpg?s=75e5fabc20b8b375f44efc0d3aff680c"},"private":false,"is_followed_by_me":false,"team_member":false,"url":"/services/players/232331719813879116","wallpaper":{"url":"http://quizup-players.imgix.net/players/232331719813879116/pictures/dfkhg82qrj/wallpaper/original.jpg?s=89838aaa33312f0b68d45edbdd16cdaa"},"feature_flags":["beta"],"permissions":[],"rank":1},"rank":4,"xp":167762,"stats":null},{"player":{"id":"409312047928373400","name":"SqM14","title":"Fawful","location":{"country_code":"US","region_code":"GA"},"locale":"en","profile_photo":{"url":"http://quizup-players.imgix.net/players/409312047928373400/pictures/knooqavfxm/original.jpg?s=836ef5121a64a804d6ea3d6c2e1ef711"},"private":true,"is_followed_by_me":false,"team_member":false,"url":"/services/players/409312047928373400","wallpaper":{"url":"http://quizup-players.imgix.net/players/409312047928373400/pictures/qkSPiuB12F/wallpaper/original.jpg?s=1adf667179f8df23122da9df63394e3c"},"feature_flags":[],"permissions":[],"rank":1},"rank":5,"xp":113450,"stats":null},{"player":{"id":"1151892228714177327","name":"Nils | ҜΞ","title":"Champion of Mario","location":{"country_code":"DE","region_code":"XX"},"locale":"de","profile_photo":{"url":"http://quizup-players.imgix.net/players/1151892228714177327/pictures/b9hdsvwowl/original.jpg?s=59193c693e413d9fd0e16f34b0521807"},"private":false,"is_followed_by_me":false,"team_member":false,"url":"/services/players/1151892228714177327","wallpaper":{"url":"http://quizup-players.imgix.net/players/1151892228714177327/pictures/jc8odgoiy1/wallpaper/original.jpg?s=055f56f8adefef94e6b167a6155329f7"},"feature_flags":[],"permissions":[],"rank":1},"rank":6,"xp":112149,"stats":null},{"player":{"id":"1535996816616549659","name":"ㅤㅤ ㅤㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤㅤ ㅤㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤㅤ ㅤㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ sugarc🍓ated |  ҜΞ 〽ㅤ                                                     #Senpai                    #StopCOVID19","title":" ","location":{"country_code":"NL","region_code":"XX"},"locale":"en","profile_photo":{"url":"http://quizup-players.imgix.net/players/1535996816616549659/pictures/37ypkkyj97/original.jpg?s=8c75b7b1f3de0e93290b8468298e42f5"},"private":false,"is_followed_by_me":false,"team_member":false,"url":"/services/players/1535996816616549659","wallpaper":{"url":"http://quizup-players.imgix.net/players/1535996816616549659/pictures/sukz04kee4/wallpaper/original.jpg?s=593961822bc2c3e4427f770ae878e5cc"},"feature_flags":[],"permissions":[],"rank":1},"rank":7,"xp":55965,"stats":null},{"player":{"id":"1171125623591764793","name":"Eddy CICALINI","title":"Boomshine Drinker","location":{"country_code":"FR","region_code":"XX"},"locale":"fr","profile_photo":{"url":"http://quizup-players.imgix.net/players/1171125623591764793/pictures/75ie6uukvj/original.jpg?s=d0ca3bde0cb6a5cd348d0473528637e9"},"private":true,"is_followed_by_me":false,"team_member":false,"url":"/services/players/1171125623591764793","wallpaper":{"url":"http://quizup-players.imgix.net/players/1171125623591764793/pictures/eu16yo4i4n/wallpaper/original.jpg?s=55adaa83558f043f2a4ea3bda3d47569"},"feature_flags":[],"permissions":[],"rank":1},"rank":8,"xp":46625,"stats":null},{"player":{"id":"1474750236198273499","name":"commshepard","title":"Kadiwéu","location":{"country_code":"US","region_code":"CA"},"locale":"en","profile_photo":{"url":"http://quizup-players.imgix.net/players/1474750236198273499/pictures/55up7cxwgv/original.jpg?s=6aa9983e327ad6b53282555132e4a322"},"private":true,"is_followed_by_me":false,"team_member":false,"url":"/services/players/1474750236198273499","wallpaper":{"url":"http://quizup-players.imgix.net/players/1474750236198273499/pictures/7gkr64di9g/wallpaper/original.jpg?s=e71af3e7ed9b814d52d5511a3ee1ca5c"},"feature_flags":[],"permissions":[],"rank":1},"rank":9,"xp":10621,"stats":null},{"player":{"id":"1972289543440921171","name":"Kiki","title":"Lemmy Koopa","location":{"country_code":"DE","region_code":"XX"},"locale":"de","profile_photo":{"url":"http://quizup-players.imgix.net/players/1972289543440921171/pictures/g0wuxht8hc/original.jpg?s=6a7772d0eb536a69b11d1a18b32321fd"},"private":false,"is_followed_by_me":false,"team_member":false,"url":"/services/players/1972289543440921171","wallpaper":{"url":"http://quizup-players.imgix.net/players/1972289543440921171/pictures/h9tirlzgua/wallpaper/original.jpg?s=5d563ee485335d95469ef8d457fe7047"},"feature_flags":[],"permissions":[],"rank":1},"rank":10,"xp":6683,"stats":null},{"player":{"id":"1732957433708170226","name":"Justin Lieu","title":"Hexplosive Expert","location":{"country_code":"US","region_code":"NJ"},"locale":"en","profile_photo":{"url":"http://quizup-players.imgix.net/players/1732957433708170226/pictures/937lcxq24o/original.gif?s=02d55f8bbf7e9601e269bb7004abe8ab"},"private":false,"is_followed_by_me":false,"team_member":false,"url":"/services/players/1732957433708170226","wallpaper":{"url":"http://quizup-players.imgix.net/players/1732957433708170226/pictures/qovhyqq4ni/wallpaper/original.jpg?s=39485e329421386fe27bcd04925c0170"},"feature_flags":[],"permissions":[],"rank":1},"rank":11,"xp":6452,"stats":null},{"player":{"id":"563087403741591763","name":"Darren","title":"Igloo Designer","location":{"country_code":"CA","region_code":"XX"},"locale":"en","profile_photo":{"url":"http://quizup-players.imgix.net/players/563087403741591763/pictures/1g8azrkkd8/original.jpg?s=a6efb745f11de21e4909f7291109937d"},"private":false,"is_followed_by_me":false,"team_member":false,"url":"/services/players/563087403741591763","wallpaper":{"url":"http://quizup-players.imgix.net/players/563087403741591763/pictures/xi5l4l8hdq/wallpaper/original.jpg?s=87e1e483f1e5d4757e3d0163cc809d39"},"feature_flags":[],"permissions":[],"rank":1},"rank":12,"xp":6143,"stats":null},{"player":{"id":"1912474867119541306","name":"BenjiElChti","title":"Jackie Chun","location":{"country_code":"FR","region_code":"XX"},"locale":"fr","profile_photo":{"url":"http://quizup-players.imgix.net/players/1912474867119541306/pictures/wc9essty95/original.jpg?s=0833b0a539395050d051c766073c43d5"},"private":false,"is_followed_by_me":false,"team_member":false,"url":"/services/players/1912474867119541306","wallpaper":{"url":"http://quizup-players.imgix.net/players/1912474867119541306/pictures/wmxddtf9tj/wallpaper/original.jpg?s=3a014463d465ac4c081b179b638aa53f"},"feature_flags":[],"permissions":[],"rank":1},"rank":13,"xp":5559,"stats":null},{"player":{"id":"715954103893616617","name":"Vana | ҜΞ 〽","title":"Twirlin' in Berlin","location":{"country_code":"CA","region_code":"XX"},"locale":"en","profile_photo":{"url":"http://quizup-players.imgix.net/players/715954103893616617/pictures/ipp03qy0xq/original.jpg?s=364d5096c0c48fdb9a43f8eb4abfd975"},"private":false,"is_followed_by_me":false,"team_member":false,"url":"/services/players/715954103893616617","wallpaper":{"url":"http://quizup-players.imgix.net/players/715954103893616617/pictures/xx0t81up2k/wallpaper/original.jpg?s=03eee53049a0341c33f5ceea613e02ab"},"feature_flags":[],"permissions":[],"rank":1},"rank":14,"xp":4773,"stats":null},{"player":{"id":"983072663175985000","name":"Marius","title":"Pessi + mist","location":{"country_code":"DE","region_code":"XX"},"locale":"de","profile_photo":{"url":"http://quizup-players.imgix.net/players/983072663175985000/pictures/4mlaort0ze/original.jpg?s=bd7b40f15e812140543dba205075fbb7"},"private":true,"is_followed_by_me":false,"team_member":false,"url":"/services/players/983072663175985000","wallpaper":{"url":"http://quizup-players.imgix.net/players/983072663175985000/pictures/ajdbc41tkj/wallpaper/original.jpg?s=bbd94917609d61f4c0308d37aefa0eee"},"feature_flags":[],"permissions":[],"rank":1},"rank":15,"xp":4475,"stats":null}],"player_rank":4,"has_more":false,"is_current":true,"time_remaining":144303,"month":6,"week":null,"year":2020,"neighbors":[{"player":{"id":"232331719813879116","name":"Thrill. | ҜΞ 〽️","title":"Champion of Mario","location":{"country_code":"US","region_code":"GU"},"locale":"en","profile_photo":{"url":"http://quizup-players.imgix.net/players/232331719813879116/pictures/bt20qm9t3j/original.jpg?s=75e5fabc20b8b375f44efc0d3aff680c"},"private":false,"is_followed_by_me":false,"team_member":false,"url":"/services/players/232331719813879116","wallpaper":{"url":"http://quizup-players.imgix.net/players/232331719813879116/pictures/dfkhg82qrj/wallpaper/original.jpg?s=89838aaa33312f0b68d45edbdd16cdaa"},"feature_flags":["beta"],"permissions":[],"rank":1},"rank":4,"xp":167762,"stats":null}],"percentile":99}}
'''

parsed = json.loads(data)

parsed = parsed["leaderboard"]["top"]

current_xp_data = {}

for p in parsed:
    current_xp_data[p["player"]["name"]] = p["xp"] 

formatted = json.dumps(parsed, indent=4)

print(formatted)
print(json.dumps(current_xp_data, indent=4))