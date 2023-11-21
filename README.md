# Project_MazeGame
 Create a game based on the requirements

**Main Scripts**  
[CMD_game](main.py)  
[Algo_Auto](auto_withE.py)  

### require [pdf](./files/エンジニア採用課題_require.pdf)  
map1: https://nangokrstudios.jp/products/recruit/pg/quiz01.txt  
map2: https://nangokrstudios.jp/products/recruit/pg/quiz02.txt  
map3: https://nangokrstudios.jp/products/recruit/pg/quiz03.txt  

# Development Plan
Mainlogic -> Map1 -> Map2 -> Map3

## Mainlogic
1. Generating windows   11/9 √
2. Character control    11/9 √  
    2.1 Getting Keyboard Input and Judging  
    2.2 Clearing the screen  
3. Map system           11/10 √
    3.1 event system
    3.2 '#'             
        BUG: Inputs are not counted after touching the wall         11/12 √
4. Item goal system     11/10 √
    4.1 'G'
    4.2 'o'
    4.3 Enemy
    4.4 G&O_logic
5. UI system            
    5.1 time&score        11/10 √
    5.2 output            11/12 √
6. Enemy system  
    6.1 catalog           11/12 √  
    6.2 test behavior instance          11/12 √  
        BUG: hit the wall(enemy)        11/12 √  
    6.3 C&D  
        6.3.1 C no wall  
        6.3.2 C with wall  
            BUG: Enemy's movement are not counted after player touched the wall     11/12 √  
            BUG: multipic C looping error  

    Require Update:  
    6.3 C&D (simple)                                                  11/14 √  
            BUG: multipic C looping error                             √  
            BUG: enemy eat the item and goal - point 4
    6.4 E (simple)                                                    11/14 √  
    6.5 A&B (simple)                                                  11/14 √  
    6.6 Global enemy_list                                             11/14 √
    6.7 A&B (complete)                                                11/14 √
    6.8 C&D                                                           11/16 √
    6.9 E                                                             11/16 √

## Automation scripts
7. Auto
    7.1 map1_auto_noEnmey                                             11/19 √
    7.2 map1_auto_withEnmey                                           11/19 √
        TIP: enemies,enemy_list


