# Alien Invasion

**Alien Invasion** is a 2D arcade-style game where the player takes on the role of a defender of Earth against an alien invasion. 
The player starts with three lives and their goal is to survive for as long as possible while scoring as many points as they can. 
The game features a simple control scheme, where the player moves left and right using the arrow keys and shoots using the space bar. 
The aliens attack in waves, becoming progressively more difficult to defeat as the player progresses.

### Задачи
Используя библиотеку pygame, создать классическую 2D игру, где игрок выступает в роли защитника земли от инопланетного вторжения.

### Что было сделано
Реализовал:
1) модель космического корабля, которым игрок может двигаться в право и в лево
2) игрок имеет 3 жизни
3) игрок может стрелять управляя кораблем
4) модели инопланетян реагируют на столкновения с игроком и снарядами
5) каждый новый уровень сложность возрастает за счет увеличения скорости пришельцев
6) за каждого сбитого пришельца игрок получает очки. С каждым новым уровнем количество очков растет
7) звуки стрельбы и музыка во время игры
8) кнопка играть на стартовом экране
9) каждый объект имеет свой модуль(например: пришелец, снаряд, корабль и т.д.)


![Screenshot from 2023-04-18 19-26-20](https://user-images.githubusercontent.com/93368311/232834782-374427ba-6a70-4057-8af0-43122bca80d0.png)

## Requirments
1) Python3
2) Pygame

## Installing
1) Download python3 from [here](https://www.python.org/).
2) Use command for install pygame `python3 -m pip install -U pygame --user`.
3) Open file *alien_invasion.py*
