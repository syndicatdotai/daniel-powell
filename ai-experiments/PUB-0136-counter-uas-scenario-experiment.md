# Testing Counter-Drone Scenarios with an Adversary, a Defender, and a Judge

While working on C-UAS Systems, I built an experiment using the OpenAI API to run three AI roles against the same counter-drone problem. One generated an adversarial scenario, one developed a defensive response, and a third judged how the two accounts would play out together.

The experiment grew out of the public reporting behind the counter-UAS research. Reports of drone incursions and attacks describe a wide range of operating environments and responses. I wanted to explore whether separate AI roles could use that material to produce a scenario, reason through a response, and compare their assumptions.

## Giving each AI a different job

The adversarial AI received skills and instructions informed by public articles about drone incidents worldwide. Its job was to generate a hypothetical scenario involving unauthorized or unlawful drone activity.

Those instructions operated within OpenAI's content and safety constraints. That affected the scenarios the model could generate, including the extent to which it could explore novel harmful uses. Public reporting gave the experiment a starting point for examining situations within those boundaries.

The generated scenarios served as inputs to the defensive exercise. They remained part of a software experiment.

## Controlling what the defender received

The defensive AI did not automatically receive the adversarial AI's entire response. I controlled what information passed between the roles.

That made the handoff part of the experiment. The defender had to respond to the information it received, while the judge could compare both accounts. The setup let me explore a defensive response without automatically giving that role every detail from the adversarial side.

## Building a response around the setting and available authority

The defensive role had to consider the environment, jurisdiction, and legal methods represented in the scenario. Its response depended on what the actor in that setting was authorized and equipped to do.

Some scenarios involved monitoring, detection, identification, and reporting. Others involved coordinating with police or the relevant public authorities, or efforts to identify the operator. Some considered physical or kinetic interdiction where the scenario represented it as legally authorized.

These differences were central to the exercise. A response had to account for the setting and authority supplied to the model as well as the incursion itself.

## Having a third AI compare the accounts

The judge received both the adversarial scenario and the defensive response. It rated their effectiveness and assessed which side would be more likely to succeed if events unfolded as described.

This created a three-part workflow. The first AI developed the challenge, the second answered it under a different set of instructions and information, and the third compared the two.

The judge's result was a model-generated assessment of hypothetical events. The experiment did not establish how a real encounter would end or validate the legal conclusions produced by the models.

## What I built and where it stopped

My work was designing the roles and instructions, connecting them through the API, controlling the information passed to the defensive role, and using a separate judge to evaluate the resulting accounts.

This was an unpublished AI experiment developed alongside the counter-drone website work. It explored how models with different roles could generate and assess competing scenarios. The outputs were hypothetical scenarios, defensive responses, and comparative judgments.

[Read about the Counter-UAS Research Catalog](../research/PUB-0113-developing-a-counter-uas-research-catalog.md)
