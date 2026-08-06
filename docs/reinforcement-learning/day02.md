# Day 02 - Agent Position

## 오늘 목표

Grid 안에서 Agent의 위치를 컴퓨터가 기억하도록 구현한다.

---

## 오늘 구현한 것

- Agent 위치 저장
- row 탐색
- col 탐색
- Start(S) 위치 찾기

---

## 오늘 배운 Python

### len()

리스트 길이

### range()

0부터 n-1까지 반복

### 2차원 리스트

grid[row][col]

---

## 강화학습에서는?

오늘 구현한

```python
agent = [0,0]
```

은

강화학습의

> **State**

를 표현하는 첫 단계이다.

Agent는

현재

어디에 있는가?

를 항상 기억해야 한다.

---

## 오늘의 핵심

환경(Environment)

```
S . . .

. X . .

. . X .

. . . G
```

은

변하지 않는다.

반면

Agent의 위치만

```
(0,0)

↓

(0,1)

↓

(1,1)
```

계속 변한다.

그래서

Environment와 Agent를 분리해서 관리한다.

---

## 오늘 느낀 점

(직접 작성)

---

## 다음 시간

Agent 이동 구현