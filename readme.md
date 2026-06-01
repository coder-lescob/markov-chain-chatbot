# How to make a chatbot with the fewest lines of codes possible ?

Well, would you look at that, it turns out I'm not building the next generation of ChatGPT, but instead I'll use a different approach that is 100% simpler, but also 100% less efficient (but it does not require to have a lot of GPUs and money). The basic idea is much more to make a gmail autocompletion software that autocompletes itself. And what we need to do that is the consept of **Markov Chains**.

## What is a Markov Chain

Invented at the start of the XX in russia, **Markov chains** offer a way to do probabilities with dependent events. The basic idea is to think about this as a literal chain of events, for example back then Markov used a poem to make a chain, it had two states vowel and consomne then the change is represented as lines or arrows with a probability. For example, we might (I actually don't know) find a probability of 47% to have after a vowel a consomne.

## Well then let's do that with words

The basic idea is to then do that with words. So a Word has a list of next words possible after, with their repected probability, then it chooses the next word randomly based on the probability.

## How to get this probability

Use the law of large numbers. Basically you want to have a text then take the first word, look at the next one and count the frequences of apparition after this word then divide it by the frequency of apparition of that original word and you done.

## Still gebrish

Event with all of that it is still gebrish but that is normal because it only looks at the previous word to generate the next but the next word might (will always) depend on a cetain context.

### Gebrish example

Trained on [this wikipedia article]("https://en.wikipedia.org/wiki/Complex_number") it gives gebrish but cool one

in real numbers have no solutions to say: a specific element denoted by either of the symbols c ( \re ( blackboard bold ) is always a number by rené descartes . } or i ) 2 = − 3 i b are congruent . addition and satisfying the complex numbers with real number has no real numbers with real number has a complex plane . it is called the real numbers with increasing values to display the above equation i {\displaystyle i^{2}=-1}; because the origin to the equation with real numbers do . despite the imaginary unit and x + bi , r ( blackboard bold ) 2 π {\displaystyle i^{2}=-1}; because no real solution which may be expressed in particular , and satisfying the scientific description of a + 1 − 9 {\displaystyle i^{2}=-1} , along with { ( upright bold ) 2 ⋅ 3 i } or r e ( x+iy ) i = u y + d i , the original complex conjugate of dimension two , with the absolute value , the distance from any ( 2 + jb . a complex solutions to as the rectangular form the associative , while the square of a complex number system that | z ¯ = 3 i .

see your new math teacher, it is gebrish (well no offences on math teachers that is just for a joke) !
