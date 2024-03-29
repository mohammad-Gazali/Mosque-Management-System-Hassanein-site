q_map = {str(i): 5 for i in range(1, 582)}

q_map["النبأ"] = 7
q_map["النازعات"] = 8
q_map["عبس"] = 5
q_map["التكوير"] = 5
q_map["الانفطار"] = 4
q_map["المطففين"] = 6
q_map["الانشقاق"] = 5
q_map["البروج"] = 5
q_map["الطارق"] = 3
q_map["الأعلى"] = 3
q_map["الغاشية"] = 4
q_map["الفجر"] = 6
q_map["البلد"] = 4
q_map["الشمس"] = 3
q_map["الليل"] = 4
q_map["الضحى"] = 2
q_map["الشرح"] = 1
q_map["التين"] = 2
q_map["العلق"] = 3
q_map["القدر"] = 1
q_map["البينة"] = 5
q_map["الزلزلة"] = 3
q_map["العاديات"] = 2
q_map["القارعة"] = 3
q_map["التكاثر"] = 2
q_map["العصر"] = 1
q_map["الهمزة"] = 2
q_map["الفيل"] = 2
q_map["قريش"] = 1
q_map["الماعون"] = 3
q_map["الكوثر"] = 1
q_map["الكافرون"] = 2
q_map["النصر"] = 1
q_map["المسد"] = 2
q_map["الإخلاص"] = 1
q_map["الفلق"] = 2
q_map["الناس"] = 2


def apply_q_map(lis):
    return sum(list(map(lambda x: q_map[x], lis)))
