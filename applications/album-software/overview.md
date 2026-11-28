# Hand-Coding a Windows Music Player for My Own Music in 2007

In 2007, I built a Windows application so people could listen to music I had written. It brought my recordings, artwork, and playback controls into a custom interface that I programmed by hand.

This was before AI-assisted coding was part of my development process. The application was simple in purpose, but getting it together took several weeks of work. The music already existed; the next project was building the software around it.

## Giving the music its own application

The goal was to give people a way to play the music through an interface I had designed. Album and track selection, artwork, playback, and sound controls became parts of the same project.

That meant moving beyond making the recordings. The listener needed a way to choose an album, select a song, start playback, pause or stop it, and adjust the sound. Each of those interactions needed visible controls and the code behind them.

The preserved application includes multiple album selections and individual track controls. Its files contain the recordings, custom graphics, interface sounds, source code, and Windows executable.

It was a small piece of software built around a personal creative project. The music and the presentation belonged together, and making the player gave me control over both.

## Building the interface by hand

The application used a custom graphical interface with separate artwork for buttons, panels, and different control states. The archive retains graphics for play, pause, stop, album selection, track selection, volume, and pitch, along with information panels and background artwork.

Those visual pieces needed to be connected to behavior. A button needed to respond to the mouse, select the intended track, or change the appropriate part of the interface. Selecting music also had its own interface sound.

The code contains separate functions for opening album selections, handling controls, displaying information, and managing playback. Much of the work was explicit: track selections were connected to their corresponding audio files, and the interface had to reflect those choices.

The finished interaction could look straightforward while still requiring a considerable amount of work underneath it.

## Playback, volume, and pitch

The player included play, pause, and stop controls, with volume and pitch adjustments presented through sliders.

The retained source shows a running loop applying the selected volume and pitch to the active music. The graphical controls and the audio behavior were connected through those values, so changing a control affected playback.

This was part of making the application feel like its own listening environment. The project combined the recorded music with a visual presentation and controls someone could use while listening.

My contribution extended across those parts. The original project readme credits me with creating the music and assets, and the preserved source records the hand-coded application that connected them.

## A simple application still took time

Looking back, the size of the task is interesting because the intended result was modest. It was a music player with a custom interface, not a large software platform.

Even so, it required time to put the pieces together, connect the controls, work through problems, and get the application behaving as intended. Development happened by writing the code, checking what it did, and making corrections by hand.

The old readme records 22 programming hours and 2,164 lines of code. The preserved main source file also contains 2,164 lines. Those figures describe the recorded programming work and source size; the overall project occupied several weeks.

That distinction captures the experience better than the apparent simplicity of the application. A small finished interface can conceal a substantial amount of implementation work, especially when one person is also creating the content and artwork around it.

## Connecting music, art, and software

This project sits at the intersection of several interests I was already pursuing: writing music, making visual material, and building interactive software.

The application gave those activities a shared destination. The songs became content for a player, the artwork became an interface, and the code made the package interactive.

The preserved release is a useful record of that period. It shows a Windows music application built by hand in 2007, years before AI became part of how I develop software. Its scope was small, but completing it meant taking responsibility for the music, the presentation, and the behavior of the program together.

## Related commentary

- [Musical Background and Production](https://github.com/syndicatdotai/daniel-powell/blob/main/background/music.md)
- [My Technical Stack: From Early Web Development to AI-Assisted Systems](https://github.com/syndicatdotai/daniel-powell/blob/main/background/technical-stack.md)
