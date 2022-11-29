 	enemy = make_hero()
 	while hero[2] > 0 and enemy[2] > 0:
		os.system("cls")
		combat_turn(hero, enemy)
		combat_turn(enemy, hero)
		print("")
		show_hero(hero)
		show_enemy(enemy)
		input("нажмите ентер чтобы сделать следующий ход")
		combat_result(hero, enemy)


def combat_result(hero, enemy) -> None:
	if hero[2] > 0 and enemy[2] <= 0:
		print("f{hero[0]} победил противника {enemy[0]}  и в награду получает:")
	    hero[5] += enemy[5]
	    print(enemy[5], "опыта")
	    hero[10] += enemy[12]
	    print(enemy[10] "монет")
	   print("И забирает предметы":)
	   for item enemy [12]
	   	print(item "end [12]")
	   print(*enemy[12])
	   hero[12] += enemy[12]
	   levelup(hero)

	



	levelup(hero)



def combat_turn(attacker: list, defender: list) -> None:
	"""TODO: DND"""
	if attacker[2] > 0:
		damage = attacker[6]
		defender[2] -= damage
		print(f"{attacker[0]} ударил {defender[0]} на {damage} здоровья")