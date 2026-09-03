from vernadsky_lab.minerals import register_mineral
from vernadsky_lab.observations import record
from vernadsky_lab.reports import summary, mineral_report

#реєстрацію двох нових мінералів
msg_malahit = register_mineral("Малахіт", "Cu2CO3(OH)2", 4, "Урал", 1747)
msg_rubin = register_mineral("Рубін", "Al2O3:Cr", 9, "М'янма", 1800)
print(msg_malahit)
print(msg_rubin)

#cпробу зареєструвати дублікат
msg_duplicate = register_mineral("Кварц", "SiO2", 7, "Україна", 1546)
print(msg_duplicate)


# Запис трьох спостережень від різних дослідників ---
obs1 = record("Вернадський", "Кварц", "Знайдено друзу прозорих кристалів.")
obs2 = record("Петров", "Малахіт", "Зразок має характерний шовковистий блиск.")
obs3 = record("Сидоров", "Алмаз", "Виявлено ідеалну октаедричну форму.")
print(obs1)
print(obs2)
print(obs3)

# Спроба записати спостереження для незареєстрованого мінералу ---
obs_fail = record("Вернадський", "Криптоніт", "Випромінює дивне зелене світло.")
print(obs_fail)

# Вивід загального зведення ---
print(summary())

# Вивід детального звіту по одному мінералу ---
report_quartz = mineral_report("Кварц")
print(report_quartz)
