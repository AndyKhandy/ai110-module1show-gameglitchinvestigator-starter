# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").



1. The first bug I found was the hints were backward. The answer was 65 and when I entered 50 it said to go lower
2. Another bug I noticed was that the range of the numbers was wrong for the different modes (Easy, Normal, and Hard)
2. Another bug I noticed is that pressing enter doesn't submit your guess when it said it would
3. Another thing I noticed is that you can choose a number out of range (not sure if it's a bug)
4. When you reset the game your score is still kept (not sure if it's supposed to be like that)
5. Another bug I found is that when you guess the right number if you got a negative score it shows a positive score.
6. The Normal mode and Easy mode swapped number of attempts

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Guess of 21 | Tell the user a negative score | Told the user a positive score| You won! The secret was 21. Final score: 25 |
|New Game | Start a new game| didn't start a new game |You already won. Start a new game to play again.
|Guess of 50 | Too low | Too high| Too high! |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude for this project. One of the bugs that I asked Claude to explain was the bug of a guess that is lower than the secret number outputing too high.

 One AI suggestion that was correct was a bug where one of the functions made the guess a string when it should be an integer (causing lexicon comparison). I verified the result by asking AI to create pytest tests and they all passed.

 An AI suggestion that was incorrect was saying that the hints were fixed after fixing the guess to a string problem but it still involved me switching the logic to ensure the right message was displayed. I verified that the logic was still wrong with the tests for high and low.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided whether a bug was really fixed by first checking my tests and then checking the streamlit/website to see if the changes were refleceted.

One test I ran was test_easy_range() which ensured that the low and high value for get_range_for_difficulty("Easy") == (1,20). It showed that the fixes I made ensured that the modes had the right ranges

I first told AI what the tests should do and then asked AI to include tests for all cases (Easy, Normal, Hard)

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
