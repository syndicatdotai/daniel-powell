# An Early AI Experiment in Generating Creative Excuses

One of my early AI experiments was a small, private application running locally on my computer to generate funny excuses. The application was not exposed online. The idea was to produce something that sounded somewhat plausible at first, then became recognizably absurd.

The interface gave the user a button to generate a line, a space to read it, and an option to carry it into a social post. That simple interaction put the experiment around a specific output and made it easy to request another attempt.

## Defining the task in the prompt

The local server made outbound requests to GPT-3.5 Turbo through the OpenAI API. A system instruction gave the model its role as a creative excuse generator and described the intended balance of plausibility, obvious fabrication, brevity, and humor.

A separate user instruction requested a creative excuse. Both instructions were fixed in the code, so each click sent the same task to the model.

That made the prompt wording central to the experiment. The user could ask for another result, while changes to the kind of excuse or the intended humor happened in the application's instructions.

The request also set a small output allowance. Together with the instruction to stay brief, that kept the task focused on a short response that could be read immediately.

## Connecting the model to a small application

The implementation used JavaScript and Express as a local server and a plain HTML page opened in my browser. The server loaded the API key from an environment variable and handled the request to OpenAI.

Clicking the generation button sent a request from the browser to the local application's endpoint. The page displayed a generating message while it waited. When the response arrived, the server returned the model's text as JSON, and the browser put it into the result area.

The application included error handling on both sides. A failed server request returned an error response, and the interface displayed a message inviting the user to try again.

This was a compact example of connecting a model to a complete interaction: request something, wait for the response, display it, and handle a failure.

## Letting the user decide what to share

The sharing button took the text in the result area and opened an X post composer in my browser with that text already filled in.

The user could then review the wording and decide whether to post it. The implementation used the platform's browser-based sharing link, keeping that decision in the user's interaction with the composer.

Generation and sharing were separate actions. A line could be requested and read before the user chose to carry it further.

## The experiment was in the wording as much as the code

The technical structure was small, but the requested result contained a tension. The excuse needed enough plausibility to establish a recognizable situation and enough absurdity to make the fabrication funny.

Those qualities were expressed through natural-language instructions. The application provided a way to turn that instruction into an output someone could read and judge.

This early project connected prompt design, API integration, interface behavior, and a user-controlled sharing step. It captures a simple form of AI experimentation: give a model a narrow creative task, build a small interaction around it, and use the resulting text as the material for judgment.
