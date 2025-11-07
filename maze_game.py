import random

class MazeGame:
    def __init__(self, size=5):
        self.size = size
        self.player_pos = [0, 0]
        self.goal_pos = [size-1, size-1]
        self.maze = self.create_maze()
        
    def create_maze(self):
        # 创建空迷宫
        maze = [['⬜' for _ in range(self.size)] for _ in range(self.size)]
        
        # 设置起点和终点
        maze[0][0] = '🚶'
        maze[self.size-1][self.size-1] = '🏁'
        
        # 添加一些随机障碍物
        obstacles = self.size * 2  # 障碍物数量
        for _ in range(obstacles):
            while True:
                x, y = random.randint(0, self.size-1), random.randint(0, self.size-1)
                # 确保不覆盖起点和终点
                if (x, y) != (0, 0) and (x, y) != (self.size-1, self.size-1):
                    if maze[x][y] == '⬜':
                        maze[x][y] = '🪨'
                        break
        
        return maze
    
    def print_maze(self):
        print("\n" + "="*30)
        print("     数字迷宫游戏")
        print("="*30)
        for row in self.maze:
            print(' '.join(row))
        print("\n控制说明:")
        print("W - 上移 | A - 左移 | S - 下移 | D - 右移")
        print("Q - 退出游戏")
        print(f"当前位置: ({self.player_pos[0]}, {self.player_pos[1]})")
    
    def move_player(self, direction):
        x, y = self.player_pos
        
        # 根据方向移动
        if direction == 'w' and x > 0:  # 上
            new_x, new_y = x-1, y
        elif direction == 's' and x < self.size-1:  # 下
            new_x, new_y = x+1, y
        elif direction == 'a' and y > 0:  # 左
            new_x, new_y = x, y-1
        elif direction == 'd' and y < self.size-1:  # 右
            new_x, new_y = x, y+1
        else:
            print("❌ 无法向这个方向移动！")
            return False
        
        # 检查是否撞到障碍物
        if self.maze[new_x][new_y] == '🪨':
            print("💥 撞到石头了！无法通过")
            return False
        
        # 移动玩家
        self.maze[x][y] = '⬜'  # 清空原位置
        self.player_pos = [new_x, new_y]
        
        # 检查是否到达终点
        if self.player_pos == self.goal_pos:
            self.maze[new_x][new_y] = '🎉'
            return 'win'
        else:
            self.maze[new_x][new_y] = '🚶'
            return True
    
    def play(self):
        print("🎮 开始数字迷宫游戏！")
        moves = 0
        
        while True:
            self.print_maze()
            
            command = input("\n请输入移动方向 (W/A/S/D): ").lower().strip()
            
            if command == 'q':
                print("👋 游戏结束！")
                break
            elif command in ['w', 'a', 's', 'd']:
                result = self.move_player(command)
                moves += 1
                
                if result == 'win':
                    self.print_maze()
                    print(f"\n🎉 恭喜！你成功到达终点！")
                    print(f"📊 总共移动了 {moves} 步")
                    break
                elif not result:
                    continue
            else:
                print("❌ 无效输入！请使用 W/A/S/D 控制移动")

# 运行游戏
if __name__ == "__main__":
    # 可以选择迷宫大小 (3-8 比较合适)
    game = MazeGame(size=5)
    game.play()