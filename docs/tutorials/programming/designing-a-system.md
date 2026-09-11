---
title: "Designing a System"
description: "A repeatable process for designing a game system before you build it: scenarios, CRC cards, trade-offs, and a class diagram, with a full worked example."
tags:
  - programming
  - unity
  - beginner
difficulty: beginner   # beginner | intermediate | advanced
time_estimate: "60 minutes"
prerequisites:
  - "[How Unity Thinks](how-unity-thinks.md) (recommended)"
  - "Index cards or paper, and something to write with"
status: published   # draft | review | published
# author: "@github-username"  # only if committing someone else's work
---

# Designing a System

!!! abstract "What You Will Learn"
    By the end of this guide you will be able to:

    - Turn a vague feature ("checkpoints!") into concrete scenarios
    - Find the objects in a system and give each one clear responsibilities
    - Test a design by walking through it before writing any code
    - Compare two designs and pick one for a reason
    - Draw a class diagram other people can actually read

**Difficulty:** Beginner · **Time:** ~60 minutes

---

## Prerequisites

Before starting, make sure you have:

- [ ] A few index cards and a pen, or a whiteboard, or anything else you can share and draw on
- [ ] A group of three or four people, if you're doing this during meeting
- [ ] Read [How Unity Thinks](how-unity-thinks.md), or you're comfortable with GameObjects and components

---

## Introduction

Here's a thing that happens constantly on game teams, and software projects in general. Someone gets assigned "the checkpoint system," opens their editor, and starts cooking something. Two days later it works, sort of, but the player script now knows about the fade effect, the checkpoint knows about the enemies, and adding "reset the collectibles on respawn" means editing four files. Nobody made a bad decision on purpose. They just made all of their decisions while typing, one line at a time, without ever seeing the whole thing at once.

This guide is about seeing the whole thing first. You'll design a system on paper, with boxes and arrows, before anybody writes a line of it. It isn't about producing a perfect plan, because the plan *will* change when you build it. It's about making the big decisions (who owns what, who talks to whom, what's likely to change) deliberately, while they're still cheap to change.

The process has nine(ish) steps, and you'll see every step applied to a full example, a **checkpoint and respawn system**, so you know what each step's output looks like before you make your own.

!!! info "Using this on a real system"
    None of this is workshop-only. When you're about to build a real system for the game, run the same steps (even alone, even quickly), then turn the result into a page with the [System Template](../../contributing/templates/system-template.md) and link it from the system's GitHub issue. Future you (and everyone else!) will be very grateful.

---

## Roles

If you're in a group, I recommend you split these up. It'll probably keep things going smoothly, but also feel free to do whatever.

| Role | Job |
|---|---|
| **Facilitator** | Keeps time, keeps the group moving through the steps, and makes sure everything is considered. |
| **Scribe** | Writes the cards and draws the diagram. |
| **Skeptic** | Tries to break the design. "What happens if the player dies *during* the fade?" is the type of stuff they should be asking. |

---

## Step 1: Write the Scenarios

**You'll produce:** three to five short scenarios, plus at least one edge case.

A scenario is one concrete thing that happens, told from a player's perspective: "the player does X, then Y happens." Ideally, this isn't something vague like "the system handles respawning," since that could mean anything, but "the player falls in a pit, the screen fades out, and they reappear at the last checkpoint."

Scenarios are a soft introduction to unit tests, a set of trials that every decision you make later gets tested against. Saving these will force you to notice the questions that nobody's answered yet.

???+ example "Worked example: scenarios"
    1. The player walks through a checkpoint for the first time. It lights up, and a "Checkpoint reached" message appears for a moment.
    2. The player dies (falls in a pit, or runs out of health). The screen fades to black, the player reappears at the last checkpoint they reached with full health, and the screen fades back in.
    3. The player reaches a second checkpoint. Now dying sends them there, not to the first one.
    4. The player walks back through the *first* checkpoint again. It becomes the active one again.
    5. **Edge case:** the player dies before touching any checkpoint. They respawn at the start of the level.
    6. **Edge case:** the player takes damage from lava *while* the respawn fade is happening. Nothing extra happens.

    Writing scenario 4 forced a decision: does revisiting an old checkpoint reactivate it?. And one question didn't get answered at all: do enemies reset when you respawn? That one becomes an open question for now.

    In practice, these decisions you'll have to make will be in conjunction with other teams, like design. For now, we can make those decisions ourselves, but game development is a multidisciplinary task, so collaboration here will help in the future.

---

## Step 2: Find the Candidate Objects

**You'll produce:** a rough list of the objects your system might need.

Go through your scenarios and underline the **nouns** (they're candidate objects) and the **verbs** (they're candidate responsibilities).

Then filter it, because not every noun deserves to be a class:

- Some nouns are just **data**. A "spawn point" might only be a position.
- Some are **processes**, not things. "Respawning" is something that happens; the question is who *does* it.
- Some already **exist**. If the game already has a `PlayerHealth`, reuse it.

???+ example "Worked example: candidates"
    **Nouns:** player, checkpoint, message, screen, health, level start, pit, lava, enemies.

    **Verbs:** walk through, light up, show, die, fade, reappear, remember (which checkpoint was last), restore (health).

    **After filtering:**

    - `Checkpoint`: definitely a thing.
    - `PlayerHealth`: already exists in the game; we'll use it.
    - Something that fades the screen: `ScreenFader`.
    - Something that shows the message: `CheckpointMessage` (UI).
    - "Level start" is really just a place to respawn, which sounds a lot like a checkpoint, so perhaps we could reuse that if there's no functional difference.
    - "Remember the last checkpoint" and "make the player reappear" are verbs with no obvious owner yet. That's the real question this design needs to resolve.

---

## Step 3: Make CRC Cards

**You'll produce:** one index card per class.

CRC stands for **Class, Responsibilities, Collaborators**. It's a technique from the late 1980s, invented specifically to teach people to think in objects, and it still works (if you just slow down for a bit). Each card has:

- **Class:** the name, at the top.
- **Responsibilities:** two to four short verb phrases for what this class knows or does. For example, "Remembers the active checkpoint." "Detects the player."
- **Collaborators:** the other classes it has to work with to do its job.

Keep them small on purpose. If a card runs out of room, then the class probably does too much (at least at this scale).

???+ example "Worked example: first draft of the cards"
    | Class | Responsibilities | Collaborators |
    |---|---|---|
    | **Checkpoint** | Knows where the player should appear. Detects the player walking through. Shows active or inactive visuals. | Player |
    | **RespawnSystem** | Remembers the active checkpoint. Respawns the player when they die. | Checkpoint, PlayerHealth, ScreenFader |
    | **PlayerHealth** | Tracks health. Announces when the player dies. Resets to full. | (none) |
    | **ScreenFader** | Fades the screen to black and says when it's done. | (none) |
    | **CheckpointMessage** | Shows "Checkpoint reached" briefly. | RespawnSystem |

    `RespawnSystem` exists because of the question from step 2: *somebody* has to own "remember the last checkpoint" and "run the respawn." (See Step 7, where this is compared against the more straightforward but worse alternative, where checkpoints do it themselves.)

---

## Step 4: Walk the Scenarios

**You'll produce:** updated cards, and a list of gaps you found.

This is the most important step in testing your design. Lay the cards out on the table, take a scenario, and act it out: whoever holds a card speaks for that class (if this is cringe you don't have to I guess). "I'm the Checkpoint. The player just walked through me, so I tell the RespawnSystem..." When a scenario needs something that no card is responsible for, you've found a gap, so give the responsibility to an existing card or make a new one.

This is a really easy and simple way to poke holes in a design that's too flimsy. The Skeptic should be throwing "what if" questions the whole time.

???+ example "Worked example: walking scenario 2 (the player dies)"
    - **PlayerHealth:** "Health hit zero. I announce that the player died."
    - **RespawnSystem:** "I heard that. I tell the ScreenFader to fade out."
    - **ScreenFader:** "Faded out. I tell whoever asked that I'm done."
    - **RespawnSystem:** "I move the player to the active checkpoint's spawn position, and tell PlayerHealth to reset to full. Then I ask ScreenFader to fade back in."
    - **Skeptic:** "Wait. During the fade, can the player still move? Can they still take damage?"

    **Gaps found:**

    1. **Player control during respawn.** Nobody stops the player from moving while the screen is black. We don't want RespawnSystem reaching into the player's movement script, so instead RespawnSystem announces "respawn started" and "respawn finished", and `PlayerController` listens and disables input in between. New collaborator, and RespawnSystem never has to know the movement script exists.
    2. **Scenario 5, no checkpoint yet.** RespawnSystem has no active checkpoint to send the player to. Level start is very similar to a checkpoint, so just make it one; put a `Checkpoint` at the level start that begins active. No special case needed.
    3. **Scenario 6, damage during the fade.** If PlayerHealth announces another death mid-respawn, we'd start a second respawn. RespawnSystem needs to know it's already respawning and ignore deaths until it's done.

---

## Step 5: Split Data from Code, and Hide What Will Change

**You'll produce:** a list of values designers should be able to tune, and a list of decisions likely to change, with where each one is hidden.

Two questions for every card:

1. **What's data?** Numbers, timings, and settings a designer will want to tweak shouldn't be buried in code. They become serialized fields or data assets. ([Data-Driven Design](data-driven-design.md) goes deep on this.)
2. **What's likely to change?** This is the big one. A system should be split up around the *decisions most likely to change*, with each one hidden inside one module so that changing it doesn't ripple through everything else. List the things you think will change, and make sure each one is contained in one place.

???+ example "Worked example: data and change"
    **Data (designer-tunable):**

    - Fade duration (on `ScreenFader`).
    - How long the message stays up (on `CheckpointMessage`).
    - Where each checkpoint puts the player (a child spawn-point object on each `Checkpoint`, so designers can drag it into place).

    **Likely to change, and where it's hidden:**

    | Likely change | Where it lives | Why that's safe |
    |---|---|---|
    | *What* resets on respawn (enemies? collectibles? timers?) | Each system that cares listens for "respawn finished" and resets itself | Adding "reset the enemies" never touches RespawnSystem |
    | How the transition looks (fade, wipe, dissolve) | Entirely inside `ScreenFader` | RespawnSystem only knows "transition out, transition in, tell me when done" |
    | Whether old checkpoints can reactivate | One rule inside RespawnSystem | Checkpoints just report being reached; they don't decide |

    That first row is also the answer to our open question from step 1. We still don't know *whether* enemies reset, but the design no longer cares; the enemy system can just hook into it now.

---

## Step 6: Decide How Things Talk

**You'll produce:** arrows between your cards showing who calls whom and who listens to whom, plus a state diagram if anything has distinct modes.

For every collaborator line on your cards, decide how that might happen. The options below are meant to be useful but not exhaustive, theres certainly other ways as well!

| Option | Use it when | Example |
|---|---|---|
| **Direct reference** (a serialized field, a method call) | A really needs B to do something, and there's one obvious B | RespawnSystem tells ScreenFader to fade |
| **Event** (announce it, let listeners react) | A just wants to say "this happened," and doesn't care who's listening, or how many | PlayerHealth announces the player died |
| **Interface** (depend on "anything that can X") | A needs *a kind of* thing, and there could be several kinds | Anything that can be damaged is an `IDamageable` |

Also look at the *direction* of each arrow. Arrows that go both ways between two cards (A knows B and B knows A) are a warning sign, because now neither can change without the other. [The OOP Toolkit](oop-toolkit.md) goes deeper on all three options.

If a class might behave differently depending on what it's currently doing, it might function as a state machine with different states. A state diagram is just the states as boxes and the events that move between them as arrows.

???+ example "Worked example: communication"
    - `Checkpoint` &rarr; `RespawnSystem`: **direct call.** When the player walks through, the checkpoint calls `respawnSystem.ActivateCheckpoint(this)`. Each checkpoint gets the reference from a serialized field. It's one obvious receiver, and the arrow only goes one way.
    - `PlayerHealth` &rarr; `RespawnSystem`: **event.** PlayerHealth announces `Died` and has no idea who's listening. (The audio system and the stats screen might listen too.)
    - `RespawnSystem` &rarr; `ScreenFader`: **direct call**, with a callback so the fader can say when it's finished.
    - `RespawnSystem` &rarr; everyone else: **events.** `CheckpointActivated`, `RespawnStarted`, and `RespawnFinished`. `CheckpointMessage`, `PlayerController`, and anything that needs resetting just listen.

    RespawnSystem has modes (gap 3 from step 4), so it needs a state diagram:

    ```mermaid
    stateDiagram-v2
        [*] --> Waiting
        Waiting --> FadingOut : player died
        FadingOut --> Respawning : fade out finished
        Respawning --> FadingIn : player moved and health reset
        FadingIn --> Waiting : fade in finished
        note right of FadingOut
            Deaths are ignored in every
            state except Waiting
        end note
    ```

---

## Step 7: Design It Twice

**You'll produce:** one different alternative, a short trade-off table, and a decision.

Your first design is rarely your best one, it's just the first one you thought of. So before you commit, sketch an actual alternative (so not a small tweak) and seriously scrutinize and compare them.

The comparison matters more than just picking one or the other. Writing down *why* you picked a design is what lets someone change it later without breaking the reasons it was built that way. This whole process is super great in informing others how you came to a decision, so documentation is highly encouraged!

???+ example "Worked example: two designs"
    **Design A: checkpoints do it themselves.** No RespawnSystem. Each checkpoint listens for the player's death, and whichever checkpoint was activated most recently (tracked in a `static` field shared by all checkpoints) runs the respawn.

    **Design B: one coordinator.** The design we've been talking about: checkpoints report being reached, and RespawnSystem owns remembering and respawning.

    | | A: checkpoints | B: coordinator |
    |---|---|---|
    | Number of classes | One fewer | One more |
    | Where the respawn sequence lives | Inside every checkpoint, but only one runs it at a time | In one place |
    | Level start with no checkpoint | Needs a special case | Just a checkpoint that starts active |
    | "Already respawning" state | A `static` field, which is global state in disguise | A normal field on one object |
    | Adding "reset enemies on respawn" | Edit Checkpoint | Enemies listen for `RespawnFinished`; nothing else changes |
    | Figuring out what happened when it breaks | Every checkpoint is a suspect | One class to look at |

    **Decision: B.** Respawning is one process, so it should have one owner. Design A may look smaller, but it spreads that one process across every checkpoint in the level and glues it together with shared static state, which is a massive code smell that could cause issues in the future if anything needs to change or be injected in.

---

## Step 8: Draw the Class Diagram

**You'll produce:** a diagram of your classes and how they connect.

Typically, you'll see boxes for classes, arrows for relationships, and a label on each arrow saying what it means. If you want something you can paste into docs later, this site renders [Mermaid](https://mermaid.js.org/syntax/classDiagram.html) diagrams, which are written as text. These five arrows cover almost everything:

```text
A --> B     association: A uses or knows about B
A ..> B     dependency: A depends on B loosely (listens to it, takes it as a parameter)
B <|-- A    inheritance: A inherits from B
B <|.. A    realization: A implements interface B
A *-- B     composition: A is made of B, and B can't exist without A
```

Inside a class, `+` means public and `-` means private. You don't need every field and method, just the ones that explain the design.

???+ example "Worked example: the class diagram"
    ```mermaid
    classDiagram
        class RespawnSystem {
            -Transform player
            -Checkpoint activeCheckpoint
            -bool isRespawning
            +ActivateCheckpoint(Checkpoint checkpoint)
            +CheckpointActivated
            +RespawnStarted
            +RespawnFinished
        }
        class Checkpoint {
            -Transform spawnPoint
            +SpawnPosition
            +SetActiveVisual(bool isActive)
        }
        class PlayerHealth {
            +Died
            +ResetToFull()
        }
        class ScreenFader {
            -float fadeDuration
            +FadeOut(Action onFinished)
            +FadeIn(Action onFinished)
        }
        class CheckpointMessage {
            -float displayDuration
        }
        class PlayerController

        Checkpoint --> RespawnSystem : reports reached
        RespawnSystem --> Checkpoint : remembers active
        RespawnSystem ..> PlayerHealth : listens for Died, resets
        RespawnSystem --> ScreenFader : fades
        CheckpointMessage ..> RespawnSystem : listens
        PlayerController ..> RespawnSystem : listens
    ```

    Look closely and you'll notice one pair of arrows going both ways: `Checkpoint` reports to `RespawnSystem`, and `RespawnSystem` remembers a `Checkpoint`. It's fine here, since RespawnSystem only reads the checkpoint's position and toggles its visuals, but it's exactly the kind of thing the Skeptic should point at and ask about. That's what the diagram is for.

    **Still open:** do enemies reset on respawn? Should checkpoints survive quitting the game? (That second one would mean talking to whoever builds the save system.)

---

## Step 9 (Optional): Spike the Riskiest Part

**You'll produce:** a throwaway prototype, and something you learned from it.

If you have time left, find the part of your design you're *least* sure about and build just that, as fast and messily as you like, in a blank project or scene. This is called a **spike**: a quick experiment to answer one question, which you throw away afterwards. Don't build the whole system, just use this as a controlled prototype.

For the checkpoint example, the risky part could be "does the fade feel okay at 0.5 seconds, and does disabling input actually stop the player mid-jump?" Testing this specific part out first before committing might be a good idea.

Then compare what you learned against your design. Did it hold up? What would you change? 

Designing a system is an ever-changing process, as you'll encounter a lot of issues in the process of implementation that you may need to tackle on the fly.

---

## Design Smells

Things that should make you stop and look again in your own design or someone else's:

- **The god class.** I swear this is a real term; one card with eight responsibilities, and every other card lists it as a collaborator.
- **The do-everything Manager.** `GameManager` is where responsibilities go when nothing owns them.
- **Arrows both ways.** Two classes that each depend on the other can't change independently and are forever coupled.
- **Everyone talks to everyone.** If your diagram looks like a spider web, some of those conversations probably want to be events.
- **Data baked into behavior.** Numbers a designer might need to tune that lives inside a method.
- **A class that only forwards.** If a card's only responsibility is "passes things along to another card," you can probably merge them.
- **Singletons as glue.** `Something.Instance` everywhere means every class secretly depends on it, which is really easy to turn into a god object.

---

## Next Steps

- [Data-Driven Design](data-driven-design.md): what to do with everything you marked as "data" in step 5.
- [The OOP Toolkit](oop-toolkit.md): more tools for step 6, like interfaces, state machines, and commands.
- [Thinking Like an Engineer](thinking-like-an-engineer.md): the ideas behind this process, in more depth.

---

## Further Reading

- [A Laboratory for Teaching Object-Oriented Thinking](http://c2.com/doc/oopsla89/paper.html): Kent Beck and Ward Cunningham's original 1989 paper on CRC cards. It's short, and they found that "even weaker programmers" could contribute to designs with them.
- [On the Criteria To Be Used in Decomposing Systems into Modules](https://cacm.acm.org/research/on-the-criteria-to-be-used-in-decomposing-systems-into-modules/): David Parnas's 1972 paper behind step 5.
- [A Philosophy of Software Design](https://web.stanford.edu/~ouster/cgi-bin/book.php): John Ousterhout's book, where "design it twice" comes from.
- [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/): how design docs work at a big company, including the "alternatives considered" section.
- [Mermaid class diagram syntax](https://mermaid.js.org/syntax/classDiagram.html): everything you can draw in text.
