import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.animation import FuncAnimation
from Vertex import Vertex

TOTAL_TIME = 10  # seconds
DELTA_TIME = 1  # seconds

INITIAL_LENGTH = 1
SIN60 = np.sqrt(3) / 2
COS60 = 1 / 2

vertices: list[Vertex] = []

fig, ax = plt.subplots(1, 1, figsize=(7.5, 7.5))
x = []
y = []
line = ax.plot(0, 0)[0]
time = np.arange(0, TOTAL_TIME, DELTA_TIME)  # seconds
frame_count = int(TOTAL_TIME / DELTA_TIME)


def init():
    ax.set_title("Koch Snowflake Simulation on the Coordinate Plane")
    ax.set_xlim(-INITIAL_LENGTH, INITIAL_LENGTH)
    ax.set_ylim(-INITIAL_LENGTH, INITIAL_LENGTH)
    # ax.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
    # ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")

    return ax.lines


def update(frame):
    t = time[frame]

    create_koch_snowflake_vertices(frame)

    line.set_data(x, y)

    print(f"Frame: {frame}, t: {t}, vertices: {len(vertices)}")

    return (line,)


def create_koch_snowflake_vertices(n):  # n: 코흐 눈송이 단계
    x.clear()
    y.clear()

    if n == 0:
        length = INITIAL_LENGTH
        vertices.append(Vertex(0, 0))
        vertices.append(Vertex(length / 2, (length * SIN60)))
        vertices.append(Vertex(length, 0))
    else:
        length = INITIAL_LENGTH / (3**n)

        for i in range(len(vertices)):
            index = (
                i + i * 3
            )  # 한 번 반복할 때마다 vertices의 구하고자 하는 vertex 인덱스가 3씩 증가함
            vertex = vertices[index]

            if index + 1 < len(vertices):
                next_vertex = vertices[index + 1]
            else:
                next_vertex = vertices[0]

            # 정삼각형일 때
            if (
                vertex.x - next_vertex.x < 0 and vertex.y - next_vertex.y < 0
            ):  # 왼쪽 아래 꼭짓점 -> 가운데 위 꼭짓점일 때
                vertex = vertices[
                    index + 1
                ]  # 첫 번째 꼭짓점이 (0, 0)일 때를 생각해서 다음 꼭짓점으로 이동

                vertices.insert(
                    index + 1,
                    Vertex(vertex.x - length * COS60, vertex.y - length * SIN60),
                )
                vertices.insert(
                    index + 1,
                    Vertex(
                        vertex.x - length * COS60 - length, vertex.y - length * SIN60
                    ),
                )
                vertices.insert(
                    index + 1,
                    Vertex(
                        vertex.x - length * 2 * COS60, vertex.y - length * 2 * SIN60
                    ),
                )
            elif (
                vertex.x - next_vertex.x < 0 and vertex.y - next_vertex.y > 0
            ):  # 가운데 위 꼭짓점 -> 오른쪽 아래 꼭짓점일 때
                vertices.insert(
                    index + 1,
                    Vertex(
                        vertex.x + length * 2 * COS60, vertex.y - length * 2 * SIN60
                    ),
                )
                vertices.insert(
                    index + 1,
                    Vertex(
                        vertex.x + length * COS60 + length, vertex.y - length * SIN60
                    ),
                )
                vertices.insert(
                    index + 1,
                    Vertex(vertex.x + length * COS60, vertex.y - length * SIN60),
                )
            elif (
                vertex.x - next_vertex.x > 0 and vertex.y - next_vertex.y == 0
            ):  # 오른쪽 아래 꼭짓점 -> 왼쪽 아래 꼭짓점일 때
                vertices.insert(index + 1, Vertex(vertex.x - length * 2, vertex.y))
                vertices.insert(
                    index + 1,
                    Vertex(
                        vertex.x - length * COS60 - length, vertex.y - length * SIN60
                    ),
                )
                vertices.insert(index + 1, Vertex(vertex.x - length, vertex.y))
            # 역삼각형일 때
            elif (
                vertex.x - next_vertex.x > 0 and vertex.y - next_vertex.y < 0
            ):  # 가운데 아래 꼭짓점 -> 왼쪽 위 꼭짓점일 때
                vertices.insert(
                    index + 1,
                    Vertex(
                        vertex.x - length * 2 * COS60, vertex.y + length * 2 * SIN60
                    ),
                )
                vertices.insert(
                    index + 1,
                    Vertex(
                        vertex.x - length * COS60 - length, vertex.y + length * SIN60
                    ),
                )
                vertices.insert(
                    index + 1,
                    Vertex(vertex.x - length * COS60, vertex.y + length * SIN60),
                )
            elif (
                vertex.x - next_vertex.x < 0 and vertex.y - next_vertex.y == 0
            ):  # 왼쪽 위 꼭짓점 -> 오른쪽 위 꼭짓점일 때
                vertices.insert(index + 1, Vertex(vertex.x + length * 2, vertex.y))
                vertices.insert(
                    index + 1,
                    Vertex(vertex.x + length * (3 / 2), vertex.y + length * SIN60),
                )
                vertices.insert(index + 1, Vertex(vertex.x + length, vertex.y))
            elif (
                vertex.x - next_vertex.x > 0 and vertex.y - next_vertex.y > 0
            ):  # 오른쪽 위 꼭짓점 -> 가운데 아래 꼭짓점일 때
                vertices.insert(
                    index + 1,
                    Vertex(
                        vertex.x - length * 2 * COS60, vertex.y - length * 2 * SIN60
                    ),
                )
                vertices.insert(
                    index + 1,
                    Vertex(
                        vertex.x - length * 2 * COS60 + length,
                        vertex.y - length * 2 * SIN60,
                    ),
                )
                vertices.insert(
                    index + 1,
                    Vertex(vertex.x - length * COS60, vertex.y - length * SIN60),
                )

    for vertex in vertices:
        x.append(vertex.x)
        y.append(vertex.y)
    x.append(vertices[0].x)
    y.append(vertices[0].y)


anim = FuncAnimation(
    fig,
    update,
    frames=frame_count,
    init_func=init,
    interval=DELTA_TIME * 1000,
    repeat=False,
)
plt.show()

# anim.save("animation.gif")
