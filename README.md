# Project_MazeGame
 Create a game based on the requirements

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
    6.3 C&D logic ()                                                  11/14 √  
            BUG: multipic C looping error                             11/14 √  
            BUG: enemy eat the item and goal
    6.3 D logic ()                                                  11/14 √  
    6.4 E  
    6.5 A&B  
7. Comprehensive test

## Automation scripts
