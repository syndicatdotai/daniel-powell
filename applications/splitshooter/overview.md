# SplitShooter: Learning to Program by Changing the Game

SplitShooter began in 2005 as an existing demo project from 3D Game Studio. It became one of my first substantial experiences learning to program: reading someone else's code, changing values, copying and modifying sections, and seeing what happened when the game ran.

The moment that stayed with me came while playing and testing it with a friend. We wanted some additional features, so we stopped playing. About an hour later, after I had worked on the code, we could try those changes in the game.

That was an eye-opening experience. Something we had just wished the game could do had become something we could actually play. I still remember that moment fondly, and it remains one of the reasons this project matters to me.

## Starting with someone else's working example

The original single-player demo gave me a functioning starting point. There was already code to read, a game to run, and behavior that could be changed and compared with the original.

My contribution grew through modifying that foundation. Copying a section, changing a value, or duplicating a behavior gave me a way to connect the code with something visible on screen.

The learning happened through those connections. Movement settings affected how a character felt. Weapon behavior changed an encounter. A camera change altered what the player could see. Each adjustment made another part of the program easier to understand.

Over time, the work expanded well beyond small changes to the demo. It became a project with its own multiplayer behavior, levels, textures, sounds, and different ways to play.

## Turning one player into two

Moving from a single-player game to local multiplayer created a different set of problems. There were now two players to control, two viewpoints to display, and interactions that had to account for both people.

The screen needed to be split so each player could follow their own character. The surviving code contains two side-by-side camera views and separate update routines that follow the corresponding players.

It also contains distinct player routines and health displays. In that preserved version, one player uses keyboard and mouse input while the other uses joystick controls. Working out movement, firing, weapon selection, and the arrangement of those inputs was part of making the game usable by two people on one computer.

Those additions changed the structure of the game. Systems that had previously assumed one player now needed to distinguish between two participants, each with their own position, health, movement, and actions.

## Making enemies respond to multiple players

Enemy behavior was another substantial part of the work. I added line-of-sight behavior so enemies could respond to whether they could see a player.

With two players in the game, choosing a target also became more complicated. The enemies needed to account for who was closer and who presented the greater threat at a given moment.

That introduced a different kind of programming problem. It involved deciding what information an enemy should use and how that information should change its behavior during play.

The project developed into both player-versus-player combat and two players facing computer-controlled opponents, with a story-mode direction as well. Each way of playing introduced further interactions to consider.

## Weapons, effects, and the feel of the game

Different weapon types and switching between them became part of the implementation. The preserved source includes primary and secondary weapon modes, ammunition checks, reload timing, and separate routines for different projectiles and grenade behavior.

One visible example is the input logic for changing weapon modes. The code tracks whether the switching key has already been pressed so holding it down does not repeatedly cycle the selection every frame.

That is a small detail, but it illustrates the work behind an ordinary game interaction. A control has to behave the way the player expects, including what happens when a button is held rather than tapped.

The source also contains impact sounds, smoke and particle effects, explosions, and damage calculations based on distance from an explosion. Those systems connect an action with the response someone sees and hears while playing.

Alongside the programming, I spent time on level design, textures, and sound design. Those choices helped the modified demo develop its own identity. The project involved shaping the environment and the experience as well as changing the rules underneath it.

## The moment programming became personal

The playtesting session with my friend brought those possibilities together. We were already enjoying something I had modified, and then a conversation about additional features became another development session.

We could pause the game, change its behavior, and return to playing with the result. For me, that made the power of programming tangible.

This was years before AI-assisted coding became part of my workflow. The changes came from working through the source myself, understanding enough to attempt an adjustment, and testing what it did.

Being able to make those changes in about an hour mattered because of the learning behind it. The earlier experimentation had given me enough familiarity with the project to act on an idea while the conversation was still fresh.

## A project that continued for years

SplitShooter remained a project I worked on over several years. The archive preserves a later source snapshot, level files, models, textures, sounds, development notes, and a demonstration video. Those materials document parts of that longer development history, rather than one complete record of every version.

The project gave me a practical introduction to programming through modification. An existing example made it possible to begin, and repeated changes gradually gave me more control over what the game could do.

It is still a project I think about. A great deal of work went into it, but the memory that stands out is simple: playing a game with a friend, deciding we wanted something more, and being able to go into the code and make it happen.

## Related commentary

- [Hand-Coding a Windows Music Player for My Own Music in 2007](https://github.com/syndicatdotai/daniel-powell/blob/main/applications/album-software/overview.md)
- [My Technical Stack: From Early Web Development to AI-Assisted Systems](https://github.com/syndicatdotai/daniel-powell/blob/main/background/technical-stack.md)
