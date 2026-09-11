---
title: "Thinking Like an Engineer"
description: "The ideas underneath good code on a team: complexity, readability, designing around change, and knowing when to stop."
tags:
  - programming
  - beginner
difficulty: beginner   # beginner | intermediate | advanced
time_estimate: "40 minutes"
prerequisites:
  - "Some programming experience in any language"
status: published   # draft | review | published
# author: "@github-username"  # only if committing someone else's work
---

# Thinking Like an Engineer

!!! abstract "What You Will Learn"
    By the end of this guide you will be able to:

    - Name the three ways complexity shows up in code, and spot them
    - Explain why code that's easy to *read* matters more than code that's clever
    - Split a system around the decisions most likely to change
    - Tell the difference between code that works and code that scales
    - Know when to stop designing and just build the thing

**Difficulty:** Beginner · **Time:** ~40 minutes

---

## Introduction

When you're programming for a class, the finish line is usually "it works." You hand it in, it gets graded, and you never open that file again.

A game (and software projects in general) is the opposite. For example, the SIGGD games last for a whole year, a lot of different people touch it, and the code you write in October gets changed in February by some random person. On a project like that, "it works" is just the first step. The code also has to be something other people can understand and change without breaking many other things.

That's basically what this guide is about. None of it is Unity-specific, since these are ideas that are still very relevant today (yes, even with AI), so don't worry if some of it takes a while to click, this gets way more obvious as you start doing things.

---

## Complexity Is the Enemy

John Ousterhout, who teaches software design at Stanford, wrote a whole book arguing that the biggest problem in software is **complexity**: anything about the code that makes it hard to understand or change. He splits it into three symptoms:

| Symptom | What it feels like |
|---|---|
| **Change amplification** | A simple change needs edits in lots of different places. |
| **Cognitive load** | You have to hold a lot in your head to make a change safely. |
| **Unknown unknowns** | It isn't obvious *what* you need to change, or what you need to know, to do something correctly. |

The last one is the most complicated to both discover and address. At least with the first two, you can see the work in front of you. With unknown unknowns, you make the change, it looks fine, and something breaks somewhere you'd never know to look.

He also names the two main causes pf this, **dependencies** (pieces of code that can't be understood or changed on their own) and **obscurity** (important information that isn't obvious from the code).

!!! question "Predict: three small requests"
    Here's a condensed version of a script that shows up in a lot of first game tutorials you might see online:

    ```csharp
    public class Player : MonoBehaviour
    {
        public int health = 100;
        public Text healthText;
        public AudioSource audioSource;
        public AudioClip hurtSound;

        private void Update()
        {
            if (Keyboard.current.aKey.isPressed)
            {
                transform.position += Vector3.left * 5f * Time.deltaTime;
            }

            if (Keyboard.current.dKey.isPressed)
            {
                transform.position += Vector3.right * 5f * Time.deltaTime;
            }
        }

        public void TakeDamage(int amount)
        {
            health -= amount;
            healthText.text = "HP: " + health;
            audioSource.PlayOneShot(hurtSound);

            if (health <= 0)
            {
                healthText.text = "DEAD";
                GameObject.Find("GameOverScreen").SetActive(true);
            }
        }
    }
    ```

    Three requests come in over the next month:

    1. Support a gamepad.
    2. Show health as hearts instead of text.
    3. Enemies should be able to take damage the same way.

    For each one: which lines change, what could accidentally break, and which of the three symptoms are you running into?

??? success "Check your prediction"
    1. **Gamepad:** every input check in `Update` changes, and they're tangled up with the movement math. You'd probably duplicate each `if` for the gamepad, which doubles the movement code too. That's change amplification.
    2. **Hearts:** `TakeDamage` has to change, even though "how health is displayed" has nothing to do with "how damage works." You have to read the damage and sound code just to find the UI lines (cognitive load), and any mistake breaks damage for the player.
    3. **Enemies taking damage:** there's nothing to reuse. Health, UI, sound, and game over are all welded into `Player`. Copy it into `Enemy` and you now have two copies of the damage logic, one of which shows the game over screen when an enemy dies, unless you remember to remove it.

    And one unknown unknown is hiding in plain sight: `GameObject.Find("GameOverScreen")`. If anyone (not even you) renames that object in the scene and the game over screen stops working, nothing in this file tells you that the name matters.

---

## Code Is Read Way More Than It's Written

You'll spend far more time reading code than writing it: your teammates' code, library code, and your own code from two weeks ago (which is basically a different person). Reading code is hard since your working memory can only juggle a handful of things at once. Everything a reader has to hold in their head (what does this variable mean, what does `true` mean in this call, what order do these have to happen in) costs a little bit more memory, and it gets very hard to keep track of.

Thus, readable code isn't about being pretty. It's about spending less of the reader's memory:

- **Names that say what things are** mean the reader doesn't have to remember.
- **Consistent style** means the reader doesn't have to decode each file's personal conventions. (That's what the [C# Style Guide](csharp-style-guide.md) is for.)
- **Small methods with clear names** let the reader skip the details until they need them.

!!! question "Predict: what wouldn't you know?"
    You've just joined the team, and you need to make the turret fire faster. You find this:

    ```csharp
    public class Turret : MonoBehaviour
    {
        public static bool paused;

        private float timer;
        private bool ready;

        public void Setup(bool a, bool b, int n)
        {
            // ...
            ready = true;
        }

        private void Update()
        {
            if (paused || !ready)
            {
                return;
            }

            timer += Time.deltaTime;

            if (timer > 0.4f)
            {
                Fire();
                timer = 0f;
            }
        }
    }
    ```

    Make a list of everything you'd have to go find out before you could safely change this, or that could trip you up later.

??? success "Check your prediction"
    Here's what's hiding in there:

    - **What do `a`, `b`, and `n` mean?** You'd have to find every call to `Setup` and reverse-engineer it. A call like `Setup(true, false, 3)` is unreadable.
    - **Who calls `Setup`, and when?** If nobody calls it, the turret may never fire, since in the code tells you it's required.
    - **Who sets `paused`?** It's `static` and public, so literally any script could be changing it. You'd have to search the whole project.
    - **Is `0.4f` the fire rate?** Probably, but it's a magic number, so you can't be sure, and there's no tooltip telling you it's in seconds (though it's a fair assumption).

    Every one of those is an unknown unknown. The fixes are small: clearly named parameters (or separate methods instead of a bundle of `bool`s), setup that happens automatically so it can't be forgotten, no public static flags, and a named, serialized fire rate.

---

## Design Around What Will Change

In 1972, a researcher named David Parnas published a paper about how to split a program into modules. The obvious approach was to split by *steps*: one module for step 1, one for step 2, and so on. Parnas showed that this falls apart as soon as anything changes, and proposed a different rule: **list the decisions most likely to change, and give each one its own module that hides it from everyone else,** a principle called *information hiding*.

Look back at the `Player` script. What's likely to change? How input works (keyboard, gamepad, rebinding), how health is displayed, and what happens on death. Each of those is a decision, and right now they're all mixed together in one class, so changing any of them risks the others. If we just hid each one behind its own component, then changing the display can't break damage, because the damage code doesn't know how health is displayed.

That's the question to ask whenever you're designing something: *what here is likely to change, and if it does, how many places will I have to touch?* (It's also step 5 of [Designing a System](designing-a-system.md#step-5-split-data-from-code-and-hide-what-will-change).)

---

## Responsibilities, Coupling, and Cohesion

A few words you'll hear constantly in legit software industry:

- A **responsibility** is something a piece of code knows or does. Good classes have a small number of closely related ones.
- **Cohesion** is how closely the things inside one class belong together. High cohesion is good: everything in `Health` is about health.
- **Coupling** is how much one piece of code depends on the details of another. Low coupling is good: `Health` can change without breaking the UI.

A pretty simple test for both is just *if two things change for the same reason, they belong together. If they change for different reasons, split them.* The health number and the heart icons change for different reasons (game balance versus UI design), so they don't belong in the same class. This idea is the "S" in the SOLID principles (single responsibility), which Unity's [design patterns and SOLID e-book](https://unity.com/resources/design-patterns-solid-ebook) walks through with game examples (I won't!).

---

## Deep Modules

So I'm talking about Ousterhout a lot here, but I swear its really useful!
Here's one more. The best classes are **deep**: a simple interface on the outside, hiding a lot of complexity on the inside.

A save system you use by calling `SaveSystem.Save()`, which quietly handles serialization, file paths, versioning, and backups, is deep. You get a lot of power for one line. A save system where you have to call `OpenFile()`, `WriteHeader()`, `WriteSection()` six times, `WriteChecksum()`, and `CloseFile()` in exactly the right order is shallow; its "interface" is just as complicated as its implementation, which means every caller has to know how to use it.

Thus, "more classes" and "smaller classes" aren't automatically better. What you want is for each piece to take complexity *off* the hands of whoever uses it.

---

## Design It Twice

Your first idea for how to build something is just the first one you had, not necessarily the best one. Before committing to a design, sketch a completely different alternative and compare them. Even when the first design wins, you'll understand *why* it won, which is exactly what will help if things need to change. [Designing a System](designing-a-system.md#step-7-design-it-twice) goes through a full worked example.

---

## Strategic vs. Tactical Programming

Ousterhout (am I glazing him too much?) draws a line between two ways of working:

- **Tactical programming** is getting the current task working as fast as possible. Each shortcut seems harmless on its own.
- **Strategic programming** is treating "is this still easy to change?" as part of the job, and spending a little extra time on design with every change.

Tactical feels faster, and for most short term projects, it is. However, the shortcuts will cost you, and a few months in, every change takes three times as long as it should because it has to work around all the earlier ones. This is professionally called **technical debt**, and stopping this is the goal of most big software projects. At SIGGD, I'm not asking anyone for perfect code; it doesn't exist. All you need to do is leave each piece of code a little better than a pure shortcut would, consistently.

---

## Knowing When to Stop

All of this can be overdone. It's easy to spend a week building a beautifully flexible system for a feature that never sees the light of day, or a framework that handles fifty cases when the game only ever has two. I am incredibly guilty of this unfortunately (re: *Project Deimos*'s cutscene engine), but it's good to know when to stop.

One term that gets tossed around is [YAGNI](https://martinfowler.com/bliki/Yagni.html), You Aren't Gonna Need it. Building something for a future you think might need it costs you the time it takes to design and build the system, the other work you could've been doing, and the extra complexity everyone deals with after, and if the guess was wrong, you pay to remove the system too. However, YAGNI is not a justification for neglecting the health of your code base. Thus, there's a balance to be found:

- **Don't build features and flexibility you don't need yet.**
- **Do keep what you build clean enough to change**, so that when you *do* need it, adding it is easy.

TLDR: If you just use clear names, small pieces, hidden decisions, and no magic numbers, you can really easily add things later on with little issue.

---

## Make: Redesign the Player

!!! example "Make: pull the Player apart"
    Take the `Player` script from [Complexity Is the Enemy](#complexity-is-the-enemy) and redesign it so that all three change requests (gamepad, hearts, enemies taking damage) would each touch as few places as possible. You don't need to write the code. List the pieces, what each is responsible for, and how they find out about each other.

??? tip "Hint 1"
    For each of the three change requests, ask: which *one* piece of code should that change live in?

??? tip "Hint 2"
    Look for the decisions that are likely to change, and for things that change for different reasons (cohesion). Input, health, how health is displayed, sound, and what happens on death are all candidates. The [Component pattern](https://gameprogrammingpatterns.com/component.html) chapter shows a very similar split.

??? tip "Hint 3"
    Try one piece per decision: something that reads input, something that moves, something that tracks health, something that shows health, and something that reacts to death. For "how do they find out about each other," think about whether health should call the UI directly, or just announce that it changed and let the UI listen.

??? note "What a good answer includes"
    - Each of the three change requests lands in one piece (or close to it).
    - Health doesn't know how it's displayed, or that the game over screen exists.
    - The damage logic exists once, and enemies reuse it.
    - The `GameObject.Find` by name is gone, replaced by something that can't silently break when an object gets renamed.
    - You didn't create a piece that exists "just in case." Every piece answers one of the change requests or an obvious near-future need.

---

Ousterhout count: three (I lowkey expected more)

## Next Steps

- [Designing a System](designing-a-system.md): these ideas turned into a step-by-step process.
- [The OOP Toolkit](oop-toolkit.md): the specific tools for keeping pieces decoupled.
- [C# Style Guide](csharp-style-guide.md): readability, written down as rules.

---

## Further Reading

- [A Philosophy of Software Design](https://web.stanford.edu/~ouster/cgi-bin/book.php) by John Ousterhout: complexity, deep modules, strategic programming, and "design it twice." Short, readable, and the source of most of this guide.
- [On the Criteria To Be Used in Decomposing Systems into Modules](https://cacm.acm.org/research/on-the-criteria-to-be-used-in-decomposing-systems-into-modules/) by David Parnas: the 1972 paper behind information hiding. Only six pages.
- [The Programmer's Brain](https://www.manning.com/books/the-programmers-brain) by Felienne Hermans: why reading code is hard, and how to get better at it.
- [YAGNI](https://martinfowler.com/bliki/Yagni.html) by Martin Fowler: the real costs of building things before you need them.
- [Level up your code with design patterns and SOLID](https://unity.com/resources/design-patterns-solid-ebook): Unity's free e-book on SOLID and design patterns, with game examples.
