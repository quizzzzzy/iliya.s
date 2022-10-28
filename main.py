import os
import shop


def show_menu():
	"""
	Показывает главное меню
	Из него начинается игра или заканчивается программа
	TODO:
	  Настройки: цыет текста
	  Сохрарнение/звгрузка

	"""

	while True:
		os.system("cls")
		print("1 - начать новую игру")
		print("2 - Выйти")
		answer = input("Введите номер ответа и нажмите ENTER")
		if answer == "1":
			start_game()
			break
			print("Игра запущена")
		elif answer == "2":
			print("Выходим  из игры")
			break
	
	print("Выходим из меню! Пока!")
	

def start_game():
	"""
	создаёт персонажа:
	  player_name - имя игрока
	  player_money - деньги игрока, >= 0 иначе игра заканчивается
	  player_hp - жизни игрока
	  player_xp - опыт игрока
	запускает игру
	игра контролируется переменной is_game

	"""
	  # создаём игрока
	player_name = input("Введите имя игрока и нажмите ENTER")
	if not player_name: player_name = "user"
	player_money = 1000
	player_hp = 100
	player_xp = 0


	is_game = True
	while is_game:
			os.system("cls")
			print(f"имя: {player_name}")
			print(f"жизни: {player_hp}")
			print(f"деньги: {player_money}")
			print(f"опыт: {player_xp}")
			print("игра запущена")
			print(f"{player_name} приехал к камню")
			print("1 - поехать на битву с разбойниками")
			print("2 - поехать играть в кости")
			print("3 - поехать в лавку алхимика")
			answer = input ("введите номер ответа и нажмите ENTER")

			if answer == "1":
				print("поехал на битву")
			elif answer == "2":
				print("поехал играть в кости")
			elif answer == "3":
				shop.shop(player_name,player_money,player_hp,player_xp)
				
			input("ENTER - дальше")
				

show_menu()
