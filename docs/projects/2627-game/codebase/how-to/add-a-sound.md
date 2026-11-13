---
title: Add a Sound Effect
description: "Get a new FMOD event from the audio team's project into Space Jam and play it from code."
tags:
  - project
  - programming
  - audio
---

# Add a Sound Effect

--8<-- "includes/2627-game/milestone.md"

The audio team adds the event in FMOD Studio and builds the banks. A programmer then refreshes the generated `AudioEvents` class and adds one line of code. For how the pipeline works, see [Audio](../systems/audio.md).

---

## Audio Team: Add and Build the Event

1. Open `FMODProject/SpaceJam_FMOD/SpaceJam_FMOD.fspro` in **FMOD Studio 2.03**. The game runs FMOD for Unity 2.03.14, and FMOD only loads banks built by the same 2.03 version line.
2. Create the event in the folder that matches where it's used, such as `Sound Effects/Player/Gun/`. The folder path becomes the C# name, so `Sound Effects/Player/Gun/Sniper_Shoot` becomes `AudioEvents.Sound_Effects.Player.Gun.Sniper_Shoot`.
3. Assign the event to a bank (usually `Sound Effects` or `Music`).
4. **File > Build**. The project is set to write banks to `FMOD/` at the repo root, which updates the files in `FMOD/Desktop/`.
5. Commit the changed `FMODProject/` files and the rebuilt `.bank` files together, and say in the PR which event is new and where it should play.

## Programmer: Refresh the Event List

1. Pull the audio team's change and open Unity. FMOD for Unity notices the new banks on its own.
2. Choose **Tools > Audio > Refresh Audio Events**.
3. The Console should say `Wrote N audio events to Assets/Audio/AudioEvents.cs`. If it says they're already up to date, Unity hasn't picked up the new banks yet. Check that the pull included the `.bank` files, then refresh again.

## Programmer: Play It

Call `AudioManager.PlayOneShot` with the new field wherever the sound should happen:

```csharp
AudioManager.PlayOneShot(AudioEvents.Sound_Effects.Player.Gun.Sniper_Shoot);
```

`AudioManager`'s methods are static, so there's nothing to look up or assign first. If the audio team made the event 3D, pass a position so it plays from the right place:

```csharp
AudioManager.PlayOneShot(AudioEvents.Sound_Effects.Boss_1.Boss_1_Hurt, transform.position);
```

Commit the regenerated `AudioEvents.cs` in the same PR as the code that uses it.

---

## Troubleshooting

=== "The field doesn't exist"
    **Symptom:** `AudioEvents` has no field for the event, so the code doesn't compile.

    **Fix:** Refresh the event list (above). If it's still missing, the event isn't in a bank, or the banks weren't rebuilt after it was added. Ask the audio team to check its bank assignment and build again.

=== "No sound plays"
    **Symptom:** The code runs, but you hear nothing.

    **Fix:** Check the Console for an `[FMOD] Event not found` warning, or an `EventNotFoundException` for music. Either one means the generated class is newer than the banks you have, so pull the latest banks. Then check that MasterScene's Main Camera still has its `StudioListener`.

=== "Music plays twice"
    **Symptom:** Starting a second music track doesn't stop the first.

    **Fix:** That's a [known bug](../systems/audio.md#known-issues) in `AudioManager.PlayTrack` at v0.1.0, not your event.
