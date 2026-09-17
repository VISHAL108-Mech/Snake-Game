# 🐍 Snake Game

A classic **Snake Game** built from scratch in Python using the built-in `turtle` graphics module — no external game engine, just pure Python, object-oriented design, and a bit of trigonometry-flavored geometry for movement and collision detection.

> Move the snake with your arrow keys, eat the food, grow longer, and try not to run into the wall — or yourself.

---

## 🎮 Demo

<img width="952" height="545" alt="Screenshot 2026-09-17 211043" src="https://github.com/user-attachments/assets/296d6c73-0a93-4675-a3c9-1dc7675cfc1c" />


---

## ✨ Features

- 🧠 **Object-Oriented Architecture** — game logic is split into clean, single-responsibility classes (`Snake`, `Food`, `Score`) instead of one giant script.
- ⌨️ **Real-time keyboard controls** using `turtle.Screen().onkey()` event listeners for Up / Down / Left / Right.
- 🍎 **Randomized food spawning** with distance-based collision detection.
- 📈 **Live scoreboard** that tracks and persists the high score.
- 💥 **Two collision systems**:
  - Wall boundary detection
  - Self-collision (head vs. body segments)
- 🎨 Custom background image support (`bgpic`) for a more polished look than the default turtle canvas.
- 🔁 Smooth game loop with manual screen refresh control (`tracer(0)` + `update()`), so nothing flickers.

---

## 🛠️ Tech Stack

| Category | Tool / Concept |
|---|---|
| Language | Python 3 |
| Graphics | `turtle` (standard library) |
| Paradigm | Object-Oriented Programming (OOP) |
| Core Concepts | Event-driven programming, game loops, collision detection, file I/O |
| Data Persistence | Local `data.txt` file for high score storage |

---

## 📂 Project Structure

```
Snake Game/
│
├── main.py          # Entry point — game setup, loop, and collision logic
├── snake.py         # Snake class — movement, growth, and reset logic
├── food.py          # Food class — random spawning logic
├── scoring.py        # Score class — scoreboard display & high score tracking
├── data.txt          # Stores the persisted high score
├── bg_1.png          # Background image for the game screen
└── README.md
```

This modular structure keeps `main.py` readable and focused purely on **orchestration** — it wires the pieces together rather than doing everything itself, which is a good habit to show off in a portfolio since it mirrors how larger real-world codebases are organized.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed (turtle ships with the standard library, so no `pip install` needed for graphics)

### Run it
```bash
git clone https://github.com/VISHAL108-Mech/Snake-Game.git
cd snake-game
python main.py
```

### Controls
| Key | Action |
|---|---|
| ↑ | Move Up |
| ↓ | Move Down |
| ← | Move Left |
| → | Move Right |

---

## 🧩 How It Works

### 1. Game Window Setup
The screen is configured once at startup, and `tracer(0)` disables automatic screen updates so the game can control exactly when to redraw — this is what keeps the animation smooth instead of jittery.

```python
screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=400)
screen.bgpic("bg_1.png")
screen.tracer(0)
```

### 2. Listening for Input
Rather than polling for keypresses, the game binds each arrow key directly to a method on the `Snake` object using `onkey()` — a clean example of event-driven programming.

```python
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
```

### 3. The Game Loop
The core loop manually refreshes the screen, pauses briefly to control snake speed, and advances the snake's position every tick.

```python
while start_game:
    screen.update()
    time.sleep(0.1)
    snake.move()
```

### 4. Food Detection & Growth
Uses `distance()` — turtle's built-in geometric helper — to check if the snake's head is close enough to the food to "eat" it.

```python
if snake.head.distance(food) < 15:
    food.generate_food()
    snake.extend_snake()
    scoreboard.calculate_score()
```

### 5. Wall Collision
Checks the snake head's x/y coordinates against the boundaries of the 600×400 play area.

```python
if (
    snake.head.xcor() > 285
    or snake.head.xcor() < -285
    or snake.head.ycor() > 185
    or snake.head.ycor() < -185
):
    scoreboard.reset()
    snake.reset()
```

### 6. Self-Collision
Loops through every body segment (excluding the head) and checks proximity — a simple but effective way to detect the snake biting itself.

```python
for snake_body in snake.snake_list[1:]:
    if snake.head.distance(snake_body) < 10:
        scoreboard.reset()
        snake.reset()
```

---

## 📚 What This Project Demonstrates

- Translating game rules (movement, collision, scoring) into clean, testable classes
- Using Python's `turtle` module beyond basic shapes — for a full interactive application
- Managing application state (score, snake length, game-over conditions) across multiple files
- Reading/writing to a local file (`data.txt`) for simple data persistence between sessions
- Practical use of distance-based geometry for real-time collision detection

---

## 🔮 Future Improvements

- [ ] Add difficulty levels (increasing speed as score grows)
- [ ] Add sound effects for eating food / game over
- [ ] Add a pause/resume feature
- [ ] Package as a standalone executable
- [ ] Add unit tests for `Snake`, `Food`, and `Score` classes

---

## 👤 Developer

VISHAL YADAV
- GitHub: https://github.com/VISHAL108-Mech
- LinkedIn: www.linkedin.com/in/vishal-yadav-2a91a7428
- Email: vy4122000@gmail.com
