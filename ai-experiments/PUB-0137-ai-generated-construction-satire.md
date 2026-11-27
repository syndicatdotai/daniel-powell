# An Ongoing Experiment in AI-Generated Construction Satire

I’m working on an AI experiment that generates short satirical commentary about the construction industry. The application takes a few inputs, builds a prompt on the server, calls the OpenAI API, and returns the generated line to the interface.

The results are mixed. So far, I’d put the usable, genuinely funny outputs at roughly 10–20%. Other responses have decent premises, but they need to be developed before the humor works.

The humor I’m looking for comes from knowing construction well enough to recognize something about the work, then abstracting it a little. A familiar behavior, expectation, or contradiction can become funny when it is exaggerated or moved into a different situation. Someone who knows the industry should recognize the connection without needing it explained.

Getting AI to make that connection consistently has been difficult.

## Turning a few inputs into a prompt

The implementation takes a descriptive word, a scenario, and an intensity setting. The server checks that the required inputs are present and translates the intensity setting into one of several tone descriptions.

Those descriptions range from playful and mildly absurd to sharper and more exaggerated. The application combines the selected tone with the supplied scenario, the descriptive word, a requested language style, and a short output limit.

A separate system instruction establishes the model’s comedic role and stylistic direction. The response is read as text and returned to the interface. The server also handles missing inputs, unsuccessful API responses, and failures while processing the request.

That gives me a structure for experimenting with the wording. The scenario supplies the situation, the descriptive input gives the line a particular quality, and the intensity setting changes the tone language sent to the model.

## Construction knowledge gives the satire somewhere to start

Construction has its own language, habits, and expectations. The humor I’m interested in depends on understanding what happens in the work and recognizing the gap between what people expect and what they encounter.

The prompt has to communicate enough of that context for the model to find a useful observation. Then the output has to carry it somewhere interesting.

Instructions such as “make it absurd” or “make it sharper” describe a direction, but getting a funny result depends on the connection underneath the wording. There has to be something recognizable about the subject for the exaggeration to land.

Abstraction is part of that balance. The line can move away from a literal construction situation while retaining something that people in the industry recognize.

## A promising premise still needs development

The difference between a usable line and a promising premise has become a large part of the experiment.

Some outputs contain an observation worth working with, but the wording has not developed it into something funny. There is still work to do with the premise, the phrasing, and how the idea is delivered.

My estimate of roughly 10–20% usable results reflects that distinction. It describes the outputs I find both usable and funny. The remaining material can still contain ideas worth revisiting.

That makes reviewing the output part of the creative work. A response needs to be read for the observation it contains and whether the finished line actually works.

## Keeping the result short adds another constraint

The implementation asks for a very short response and places a small limit on the generated output.

That leaves little room to establish a situation, make the connection, and deliver the line. Explaining too much can use the space the humor needs. Leaving too much out can lose the connection to the subject.

The prompt has to carry enough direction for the result to stand on its own. Finding language that communicates the intended humor remains the difficult part.

## Where the experiment stands

The input handling, prompt construction, API request, and response processing are implemented. The ongoing work is trying to improve the construction satire those components produce.

Based on the results so far, AI does not handle this kind of humor very well at the moment. It can contribute premises and occasionally produce a line that works, but consistently turning subject knowledge into usable satire still takes substantial editorial judgment.

That mixed result is where the experiment currently stands.
